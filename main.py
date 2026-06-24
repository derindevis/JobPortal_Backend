import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from database import engine, Base
from routers import jobs, auth, applications

load_dotenv()

#eathanu sherikkum olla SQL Tables ninghalude model vechu indakkunnathu
Base.metadata.create_all(bind=engine)
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
    