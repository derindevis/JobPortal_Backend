import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from database import engine, Base, SessionLocal
from routers import jobs, auth, applications

load_dotenv()

#eathanu sherikkum olla SQL Tables ninghalude model vechu indakkunnathu
Base.metadata.create_all(bind=engine)

def create_default_admin():
    from models.user import User
    from utils.hashing import hash_password
    db = SessionLocal()
    try:
        admin_username = os.getenv("ADMIN_USERNAME", "admin")
        admin_password = os.getenv("ADMIN_PASSWORD", "admin123")
        existing_admin = db.query(User).filter(User.role == "admin").first()
        if not existing_admin:
            existing_user = db.query(User).filter(User.username == admin_username).first()
            if existing_user:
                existing_user.role = "admin"
                existing_user.hashed_password = hash_password(admin_password)
                print(f"Updated existing user '{admin_username}' to admin role.")
            else:
                new_admin = User(
                    username=admin_username,
                    hashed_password=hash_password(admin_password),
                    role="admin"
                )
                db.add(new_admin)
                print(f"Created default admin user '{admin_username}' with role admin.")
            db.commit()
    except Exception as e:
        print(f"Failed to create default admin: {e}")
    finally:
        db.close()

def auto_seed_jobs():
    from models.job import Job
    from seed_jobs import seed_jobs
    db = SessionLocal()
    try:
        if db.query(Job).count() == 0:
            print("Jobs database is empty. Auto-seeding default jobs...")
            seed_jobs()
    except Exception as e:
        print(f"Failed to auto-seed jobs: {e}")
    finally:
        db.close()

create_default_admin()
auto_seed_jobs()

app = FastAPI(title="JobPortal")

# Mount uploads static folder
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

FRONTEND_URL = os.getenv("FRONTEND_URL", "")
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "https://job-portal-frontend-gamma-brown.vercel.app"
]

if FRONTEND_URL:
    for val in FRONTEND_URL.split(","):
        val = val.strip()
        if val:
            if val.endswith("/"):
                val = val[:-1]
            if val not in origins:
                origins.append(val)

print("Allowed CORS Origins:", origins)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#auth.py nirmicha routes upayogikkan fastapi node parayum
app.include_router(auth.router, prefix="/auth",tags=["Authentication"]) 
app.include_router(jobs.router,prefix="/jobs",tags=["Jobs"])
app.include_router(applications.router,prefix="/applications",tags=["Applications"])

@app.get("/")
def read_root():
    return {"message": "The Job portal is running!"}
    