import os
from fastapi import FastAPI
from database import engine, Base
from routers import jobs,auth,applications
from dotenv import load_dotenv
load_dotenv()
#eathanu sherikkum olla SQL Tables ninghalude model vechu indakkunnathu
Base.metadata.create_all(bind=engine)
app = FastAPI(title="JobPortal")
#auth.py nirmicha routes upayogikkan fastapi node parayum
app.include_router(auth.router, prefix="/auth",tags=["Authentication"]) 
app.include_router(jobs.router,prefix="/jobs",tags=["Jobs"])
app.include_router(applications.router,prefix="/app",tags=["Applications"])
@app.get("/")
def read_root():
    return {"message": "The Job portal is running!"}


