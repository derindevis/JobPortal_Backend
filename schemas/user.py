from pydantic import BaseModel

class UserSchema(BaseModel):
    username : str
    password : str
    role : str = "user"

class UserOut(BaseModel):
    id : int
    username : str
    role : str
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token : str
    token_type : str