from fastapi import FastAPI
from database import engine, Base
from routers import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Portal API")

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

@app.get("/")
def read_root():
    return {"message": "The Job portal is running!"}