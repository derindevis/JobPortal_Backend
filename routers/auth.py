from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session 
from dependencies import get_current_user
from database import get_db
from models.user import User
from schemas.user import UserCreate, Token, UserOut
from utils.hashing import hash_password, verify_password
from utils.jwt import create_access_token

router = APIRouter()

@router.post("/register", status_code=201)
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already taken")
    
    # Create new user with hashed password
    new_user = User(
        username=user.username,
        hashed_password=hash_password(user.password),
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"Message" : f"Account created for {new_user.username} successfully"}

@router.post("/login", response_model=Token)
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": db_user.username, "role": db_user.role})
    return {"access_token": access_token, "token_type": "Bearer", "role": db_user.role}

@router.get("/me", response_model=UserOut)
def get_me(current_user: User=Depends(get_current_user)):
    return current_user