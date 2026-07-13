"""
Defines all HTTP endpoints related to resumes.

Responsibilities:
- Receive HTTP requests
- Call CRUD functions
- Return HTTP responses
"""

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import app.crud as crud
import app.schemas as schema
from app.database import SessionLocal

router = APIRouter(
    prefix="/resumes",
    tags=["Resumes"]
)


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==========================================================
# GET /resumes
# SELECT * FROM resumes;
# ==========================================================

@router.get("/", response_model=List[schema.ResumeResponse])
def get_resumes(db: Session = Depends(get_db)):
    return crud.get_resumes(db)


# ==========================================================
# GET /resumes/{resume_id}
# SELECT * FROM resumes WHERE id = [];
# ==========================================================

@router.get("/{resume_id}", response_model=schema.ResumeResponse)
def get_resume(
    resume_id: int,
    db: Session = Depends(get_db)
):
    resume = crud.get_resume(db, resume_id)

    if resume is None:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    return resume


# ==========================================================
# POST /resumes
# INSERT INTO resumes (...);
# ==========================================================

@router.post("/", response_model=schema.ResumeResponse)
def create_resume(
    resume: schema.ResumeCreate,
    db: Session = Depends(get_db)
):
    return crud.create_resume(db, resume)


# ==========================================================
# PUT /resumes/{resume_id}
# UPDATE resumes SET ... WHERE id = [];
# ==========================================================

@router.put("/{resume_id}", response_model=schema.ResumeResponse)
def update_resume(
    resume_id: int,
    resume_update: schema.ResumeUpdate,
    db: Session = Depends(get_db)
):
    updated_resume = crud.update_resume(
        db,
        resume_id,
        resume_update
    )

    if updated_resume is None:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    return updated_resume


# ==========================================================
# DELETE /resumes/{resume_id}
# DELETE FROM resumes WHERE id = [];
# ==========================================================

@router.delete("/{resume_id}", response_model=schema.ResumeResponse)
def delete_resume(
    resume_id: int,
    db: Session = Depends(get_db)
):
    deleted_resume = crud.delete_resume(
        db,
        resume_id
    )

    if deleted_resume is None:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    return deleted_resume