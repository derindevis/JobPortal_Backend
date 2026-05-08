from pydantic import BaseModel, Field
from typing import Optional

class JobCreate(BaseModel):
    title:str = Field(..., min_length=3, max_length=150)
    company:str = Field(..., min_length=2, max_length=100)
    location:str = Field(..., min_length=2, max_length=100)
    salary:Optional[str]=None
    description:str = Field(...,min_length=10)
    deadline:str = Field(..., max_length=20)

class JobUpdate(BaseModel):
    title:Optional[str]=None
    company:Optional[str]=None
    location:Optional[str]=None
    salary:Optional[str]=None
    description:Optional[str]=None
    deadline:Optional[str]=None
    active: Optional[bool]=None

class JobOut(BaseModel):
    id:int
    title:str
    company:str
    location:str
    salary:Optional[str]
    description:str
    deadline:str
    active:bool

    class Config:
        from_attributes=True