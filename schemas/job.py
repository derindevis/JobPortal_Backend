from pydantic import BaseModel
from typing import Optional

class JobCreate(BaseModel):
    title:str
    company:str
    location:str
    salary:Optional[str]=None
    description:str
    deadline:str

class JobUpdate(BaseModel):
    title:Optional[str]=None
    company:Optional[str]=None
    location:Optional[str]=None
    salary:Optional[str]=None
    description:Optional[str]=None
    deadline:Optional[str]=None

class JobOut(BaseModel):
    id:int
    company:str
    location:str
    salary:Optional[str]
    description:str
    deadline:str
    active:bool

    class Config:
        from_attributes=True