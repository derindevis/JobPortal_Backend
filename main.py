from fastapi import FastAPI
from database import engine, Base
from routers import auth

# This creates the actual database tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Team 13 Job Portal")

# Include your auth routes
app.include_router(auth.router)

@app.get("/")
def home():
    return {"message": "Job Portal API is running"}