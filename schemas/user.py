from typing import Optional
from pydantic import BaseModel, Field, field_validator

class UserCreate(BaseModel):
    username: str
    password: str
    role: Optional[str] = "user"

    @field_validator("username")
    def username_must(cls, value):
        if not all(c.islower() or c.isalnum() or c=='_' for c in value.strip()):
            raise ValueError("Username must contain lowercase letters, numbers and underscores only")
        if ' ' in value:
            raise ValueError("Spaces are not allowed")
        return value

class UserOut(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "Bearer"