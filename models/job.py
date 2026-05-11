from sqlalchemy import Column,Integer,String,Text,Boolean  
from database import  Base

class Job(Base):
    __tablename__="jobs"

    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    title=Column(String(150),nullable=False)
    company=Column(String(100),nullable=False)
    location=Column(String(100),nullable=False)
    salary=Column(String(50),nullable=True)
    description=Column(Text,nullable=False)
    deadline=Column(String(50),nullable=False)
    active=Column(Boolean,default=True)
    
