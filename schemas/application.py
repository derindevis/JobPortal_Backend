from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional

class ApplicationCreate(BaseModel):
    job_id: int = Field(description="The Id of the job being applied for")
    cover_letter: str = Field(min_length=20, description="The applicant's cover letter")

#Admin only (updating app status)
class ApplicationStatusUpdate(BaseModel):
    status: str = Field(description="New status like 'Applied', 'Shortlisted', 'Interviewed' or 'Rejected'")

    @field_validator("status")
    @classmethod
    def validate_status(cls, value):
        allowed = ['Applied', 'Shortlisted', 'Interviewed', 'Rejected']
        if value not in allowed:
            raise ValueError(f"Status must be one of {allowed}")
        return value

class ApplicationResponse(BaseModel):
    id: int
    job_id: int
    user_id: int
    cover_letter: str
    applied_at: datetime
    status: str
    ai_score: Optional[int] = None
    ai_reasoning: Optional[str] = None
    resume_path: Optional[str] = None

    class Config:
        from_attributes = True