from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime

def validate_date(value: Optional[str]):
    if value is None:
        return value
    try:
        parsed_date=datetime.strptime(value, '%Y-%m-%d').date()
        return value
    except ValueError:
        raise ValueError("Deadline must be in 'YYYY-MM-DD' format")

class JobCreate(BaseModel):
    title:str = Field(..., min_length=3, max_length=150)
    company:str = Field(..., min_length=2, max_length=100)
    location:str = Field(..., min_length=2, max_length=100)
    salary:Optional[str]=None
    description:str = Field(...,min_length=10)
    deadline:str = Field(..., max_length=20)

    @field_validator("deadline")
    def check_deadline(cls, v):
        return validate_date(v)

class JobUpdate(BaseModel):
    title:Optional[str]=None
    company:Optional[str]=None
    location:Optional[str]=None
    salary:Optional[str]=None
    description:Optional[str]=None
    deadline:Optional[str]=None
    active: Optional[bool]=None

    @field_validator("deadline")
    def check_deadline(cls, v):
        return validate_date(v)

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
        