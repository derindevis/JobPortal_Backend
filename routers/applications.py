from fastapi import APIRouter, HTTPException, Depends,status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.application import Application
from schemas.application import ApplicationCreate, ApplicationResponse, ApplicationStatusUpdate
from dependencies import get_current_user, require_admin, require_user
from models.job import Job

router=APIRouter()

@router.get("/me", response_model=List[ApplicationResponse])
def get_dashboard(db: Session=Depends(get_db), current_user=Depends(get_current_user)):
    if current_user.role=="admin":
        return db.query(Application).all()
    return db.query(Application).filter(Application.user_id==current_user.id).all()
    

@router.post("/", response_model=ApplicationResponse, status_code=201)
def apply_for_job(data: ApplicationCreate, db: Session=Depends(get_db), current_user:User=Depends(require_user)):
    job=db.query(Job).filter(Job.id==data.job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="The job doesn't exist.")
    if not job.active:
        raise HTTPException(status_code=400, detail="This job is no longer accepting applications.")
    
    existing=db.query(Application).filter(Application.job_id==data.job_id, Application.user_id==current_user.id).first()
    if existing:
        raise HTTPException(status_code=400, detail="You have already applied!")

    new_app=Application(job_id=data.job_id, user_id=current_user.id, cover_letter=data.cover_letter)
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    return new_app


@router.put("/{app_id}", response_model=ApplicationResponse)
def update_app_status(app_id:int, payload: ApplicationStatusUpdate, db: Session=Depends(get_db),admin=Depends(require_admin)):
    application=db.query(Application).filter(Application.id==app_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application Not Found!")
    application.status=payload.status
    db.commit()
    db.refresh(application)
    return application


@router.delete("/{app_id}")
def withdraw_application(
    app_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_user)
):
    application=db.query(Application).filter(Application.id==app_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application Not Found")
    
    if application.user_id!=current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="You are not authorized to withdraw this application.")

    db.delete(application)
    db.commit()
    return {"Message":"Application Withdrawn Successfully!"}