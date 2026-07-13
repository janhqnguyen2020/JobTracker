"""
companies.py

Defines all HTTP endpoints related to companies.

Responsibilities:
- Receive HTTP requests
- Call CRUD functions
- Return validated HTTP responses
"""

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import app.crud as crud
import app.schemas as schema
from app.database import SessionLocal

router = APIRouter(
    prefix="/companies",
    tags=["Companies"]
)


# ==========================================================
# Database Dependency
# ==========================================================

def get_db():
    """
    Creates a database session for each request and
    automatically closes it when the request finishes.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==========================================================
# GET /companies
# SELECT * FROM companies;
# ==========================================================

@router.get("/", response_model=List[schema.CompanyResponse])
def get_companies(db: Session = Depends(get_db)):
    return crud.get_companies(db)


# ==========================================================
# GET /companies/{company_id}
# SELECT * FROM companies WHERE id = ?;
# ==========================================================

@router.get("/{company_id}", response_model=schema.CompanyResponse)
def get_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    company = crud.get_company(db, company_id)

    if company is None:
        raise HTTPException(
            status_code=404,
            detail="Company not found"
        )

    return company


# ==========================================================
# POST /companies
# INSERT INTO companies (...);
# ==========================================================

@router.post("/", response_model=schema.CompanyResponse)
def create_company(
    company: schema.CompanyCreate,
    db: Session = Depends(get_db)
):
    return crud.create_company(db, company)


# ==========================================================
# PUT /companies/{company_id}
# UPDATE companies SET ... WHERE id = ?;
# ==========================================================

@router.put("/{company_id}", response_model=schema.CompanyResponse)
def update_company(
    company_id: int,
    company_update: schema.CompanyUpdate,
    db: Session = Depends(get_db)
):
    updated_company = crud.update_company(
        db,
        company_id,
        company_update
    )

    if updated_company is None:
        raise HTTPException(
            status_code=404,
            detail="Company not found"
        )

    return updated_company


# ==========================================================
# DELETE /companies/{company_id}
# DELETE FROM companies WHERE id = ?;
# ==========================================================

@router.delete("/{company_id}", response_model=schema.CompanyResponse)
def delete_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    deleted_company = crud.delete_company(db, company_id)

    if deleted_company is None:
        raise HTTPException(
            status_code=404,
            detail="Company not found"
        )

    return deleted_company