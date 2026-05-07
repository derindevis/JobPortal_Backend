from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from database import get_db
from models.job import Job
from schemas.job import JobCreate,JobUpdate,JobOut
from dependencies import get_current_user,require_admin
from typing import List

router= APIRouter()

@router.get('/',response_model=List[JobOut])
def list_jobs(db: Session=Depends(get_db), user=Depends(get_current_user)):
    return db.query(Job).filter(Job.active==True).all()

@router.get("/{job_id}",response_model=JobOut)
def get_jobs(job_id:int,db:Session=Depends(get_db),user=Depends(get_current_user)):
    job=db.query(Job).filter(Job.id==job_id).first()
    if not job:
        raise HTTPException(status_code=404,detail="job not found")
    return  job

@router.post("/",response_model=JobOut)
def create_job(job:JobCreate,db:Session=Depends(get_db),admin=Depends(require_admin)):
    new_job=Job(**job.dict())
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

@router.put("/{job_id}",response_model=JobOut)
def update_job(job_id: int,updates:JobUpdate,db:Session=Depends(get_db),admin=Depends(require_admin)):
    job=db.query(Job).filter(Job.id==job_id).first()
    if not job:
        raise HTTPException(status_code=404,detail="job not found")
    for key,value in updates.dict(exclude_unset=True).items():
        setattr(job,key,value)
    db.commit()
    db.refresh(job)
    return job
 
@router.delete("/{job_id}")
def delete_job(job_id:int,db:Session=Depends(get_db),admin=Depends(require_admin)):
    job=db.query(Job).filter(Job.id==job_id).first()
    if not job:
        raise HTTPException(status_code=404,detail="job not found")
    db.delete(job)
    db.commit()
    return {"message":"Job deleted successfully"}
  