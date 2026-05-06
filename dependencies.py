from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError
from sqlalchemy.orm import Session

#database and user table check cheyann vendi import cheyunnu
from database import get_db
from models.user import User
from utils.jwt import verify_access_token

#bearer_scheme tool headerill olla token "bearer" undho ennu nokkum 
bearer_scheme = HTTPBearer()

def get_current_user(
        #react app sherikkum ayakkunna token that captures credentials 
        credentials : HTTPAuthorizationCredentials = Depends(bearer_scheme),
        db : Session = Depends(get_db)
):
    #token credentials ill ninnu string neh verthirichu edukkum(extract)
    token = credentials.credentials
    try:
        #utility function upayogichu token ill hidden username neh vayikkum 
        username = verify_access_token(token)
    except JWTError:
        #eppo token ill kayakalli nadanall, request nirthum
        raise HTTPException(status_code=401, detail="Token is invalid or expired")
    #user neh kandupidichu database ill undh enghil enthayalum undh ennu orappu varuthum
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    #user object neh thirichu kodukkum, appol adutha function nn arriyam araa vilichathu ennu
    return user

def require_admin(current_user: User = Depends(get_current_user)):
    #admin nte role ollavarkum mathram proceed cheyann pattum ennu check cheyunnnu
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user