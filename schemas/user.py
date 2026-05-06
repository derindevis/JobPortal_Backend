from pydantic import BaseModel
from typing import Optional

# Data sent when registering
class UserCreate(BaseModel):
    username: str
    password: str
    role: Optional[str] = "user"

# Data sent when logging in
class UserLogin(BaseModel):
    username: str
    password: str

# Data sent back to the user (Safe: no password!)
class UserOut(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        from_attributes = True