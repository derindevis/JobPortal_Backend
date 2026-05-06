from fastapi import FastAPI
from database import engine, Base
from routers import auth

#eathanu sherikkum olla SQL Tables ninghalude model vechu indakkunnathu
Base.metadata.create_all(bind=engine)

app = FastAPI()
#auth.py nirmicha routes upayogikkan fastapi node parayum
app.include_router(auth.router, prefix="/auth")