from sqlalchemy import Column, Integer, Text, DateTime, String, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Application(Base):
    __tablename__="applications"
    
    id=Column(Integer, primary_key=True, index=True, autoincrement=True) 
    job_id=Column(Integer, ForeignKey("jobs.id"), nullable=False) 
    user_id=Column(Integer, ForeignKey("users.id"), nullable=False) 
    cover_letter=Column(Text, nullable=False)
    #func.now() uses the database's internal clock.
    #sever um user um diff place il annel, datetime.now() time confusin undakkum.
    applied_at=Column(DateTime(timezone=True),server_default=func.now()) 
    status=Column(String(20), default='Applied')
    