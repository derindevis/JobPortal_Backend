from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ApplicationCreate(BaseModel):
    job_id: int = Field(..., description="The Id of the job being applied for")
    cover_letter: str = Field(..., min_length=20, description="The applicant's cover letter")

#Admin only (updating app status)
class ApplicationStatusUpdate(BaseModel):
    status: str = Field(...,description="New status like 'Interviewing' or 'Hired'")

class ApplicationResponse(BaseModel):
    id: int
    job_id: int
    user_id: int
    cover_letter: str
    applied_at: datetime
    status: str

    class Config:
        from_attributes = True