from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.application import Application
from schemas.application import ApplicationCreate, ApplicationResponse, ApplicationStatusUpdate
from dependencies import get_current_user, require_admin

router=APIRouter()

@router.get("/me", response_model=List[ApplicationResponse])
def get_my_applications(db: Session=Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(Application).filter(Application.user_id==current_user.id).all()

@router.get("/", response_model=List[ApplicationResponse])
def get_all_applications(db: Session=Depends(get_db), admin=Depends(require_admin)):
    return db.query(Application).all()

@router.post("/", response_model=ApplicationResponse, status_code=201)
def apply_for_job(data: ApplicationCreate, db: Session=Depends(get_db), current_user=Depends(get_current_user)):
    existing=db.query(Application).filter(Application.job_id==data.job_id, Application.user_id==current_user.id).first()

    if existing:
        raise HTTPException(status_code=400, detail="You have already applied!")

    new_app=Application(job_id=data.job_id, user_id=current_user.id, cover_letter=data.cover_letter)
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    return new_app

@router.put("/{app_id}", response_model=ApplicationResponse)
def update_app_status(app_id:int, status_code: ApplicationStatusUpdate, db: Session=Depends(get_db),admin=Depends(require_admin)):
    application=db.query(Application).filter(Application.id==app_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application Not Found!")
    application.status=status_data.status
    db.commit()
    db.refresh(application)
    return application