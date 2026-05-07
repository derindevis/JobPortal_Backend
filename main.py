from fastapi import FastAPI
from database import engine, Base
from routers import jobs,auth
import models.job

#eathanu sherikkum olla SQL Tables ninghalude model vechu indakkunnathu
Base.metadata.create_all(bind=engine)
app = FastAPI(title="JobPortal")
#auth.py nirmicha routes upayogikkan fastapi node parayum
app.include_router(auth.router, prefix="/auth") 
app.include_router(jobs.router,prefix="/jobs",tags=["Jobs"])

@app.get("/")
def root():
    return{"message":"JonPortal API is running"}