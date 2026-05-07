from sqlalchemy import Column, Integer, Text, DateTime, String, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Application(Base):
    __tablename__="applications"
    #[cite:16] use ariyilla nokkanam
    id=Column(Integer, primary_key=True, index=True, autoincrement=True) [cite:16]
    job_id=Column(Integer, ForeignKey("jobs.id"), nullable=False) [cite:16]
    user_id=Column(Integer, ForeignKey("user.id"), nullable=False) [cite:16]
    cover_letter=Column(Text, nullable=False) [cite:16]
    #func.now() uses the database's internal clock.
    #sever um user um diff place il annel, datetime.now() time confusin undakkum.
    applied_at=Column(DataTime(timezone=True),sever_default=func.now()) [cite:16]
    status=Column(String(20), default='Applied') [cite:16]