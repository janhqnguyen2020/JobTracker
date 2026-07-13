"""
    this schema validates incoming data
    - if validation fails, fastAPI automatically returns error
    - describe what a request/ response should look like

"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# ==========================================================
# COMPANY SCHEMAS
# ==========================================================

"""
Returned to the frontend.

Represents a complete Company object returned by the API.
"""
class CompanyResponse(BaseModel):
    id: int
    company_name: str
    website: Optional[str] = None
    industry: Optional[str] = None
    headquarters: Optional[str] = None
    company_size: Optional[str] = None
    glassdoor_url: Optional[str] = None
    linkedin_url: Optional[str] = None

    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


"""
Used when creating a company.

Notice:
- No id
- No timestamps

Those are generated automatically by PostgreSQL.
"""
class CompanyCreate(BaseModel):
    company_name: str
    website: Optional[str] = None
    industry: Optional[str] = None
    headquarters: Optional[str] = None
    company_size: Optional[str] = None
    glassdoor_url: Optional[str] = None
    linkedin_url: Optional[str] = None


"""
Used when updating a company.

Everything is optional because the user might update
only a single field.
"""
class CompanyUpdate(BaseModel):
    company_name: Optional[str] = None
    website: Optional[str] = None
    industry: Optional[str] = None
    headquarters: Optional[str] = None
    company_size: Optional[str] = None
    glassdoor_url: Optional[str] = None
    linkedin_url: Optional[str] = None


# ==========================================================
# RESUME SCHEMAS
# ==========================================================

"""
Returned to the frontend.

Represents a complete Resume object returned by the API.
"""
class ResumeResponse(BaseModel):
    id: int
    user_id: int
    resume_name: str
    version: str
    file_path: str
    description: Optional[str] = None

    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


"""
Used when creating a resume.

Since authentication is not implemented yet,
the frontend supplies the user_id.

Later, once users log in,
the backend will determine the current user
and this field can be removed.
"""
class ResumeCreate(BaseModel):
    user_id: int
    resume_name: str
    version: str
    file_path: str
    description: Optional[str] = None


"""
Used when updating a resume.

Everything is optional because
the user may only update one field.
"""
class ResumeUpdate(BaseModel):
    resume_name: Optional[str] = None
    version: Optional[str] = None
    file_path: Optional[str] = None
    description: Optional[str] = None


