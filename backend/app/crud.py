"""
    CRUD: (Create, Read, Update, Delete)
    actual databse operations

"""
from sqlalchemy.orm import Session
from app.models import Company, Resume
from app.schemas import CompanyCreate, CompanyUpdate, ResumeCreate, ResumeUpdate

# SELECT * FROM companies;
def get_companies(db: Session):
    return db.query(Company).all()

# SELECT * FROM companies WHERE id = []
def get_company(db: Session, company_id : int):
    return db.query(Company).filter(Company.id == company_id).first()

# INSERT INTO companies (company_name, website, industry, headquarters, company_size, glassdoor_url, linkedin_url) 
# VALUES ([], [], [], [], [], [], []);
def create_company(db: Session, company: CompanyCreate):
    db_company = Company(**company.model_dump())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

# UPDATE companies SET company_name = [], website = [], industry = [], headquarters = [], company_size = [], glassdoor_url = [], linkedin_url = [] 
# WHERE id = [];
def update_company(db: Session, company_id: int, company_update: CompanyUpdate):
    db_company = db.query(Company).filter(Company.id == company_id).first()
    if db_company:
        for key, value in company_update.model_dump(exclude_unset=True).items():
            setattr(db_company, key, value)
        db.commit()
        db.refresh(db_company)
    return db_company

# DELETE FROM companies WHERE id = [];
def delete_company(db: Session, company_id: int):
    db_company = db.query(Company).filter(Company.id == company_id).first()
    if db_company is None:
        return None
    
    db.delete(db_company)
    db.commit()

    return db_company

#SELECT * FROM resumes
def get_resumes(db: Session):
    return db.query(Resume).all()

#SELECT * FROM resumes WHERE id = []
def get_resume(db: Session, resume_id: int):
    return db.query(Resume).filter(Resume.id == resume_id).first()

#INSERT INTO resumes () VALUE ()
def create_resume(db: Session, resume: ResumeCreate):
    db_resume = Resume(**resume.model_dump())
    db.add(db_resume)
    db.commit()
    db.refresh(db_resume)
    return db_resume

#UPDATE resume SET .... WHERE id = []
def update_resume(db: Session, resume_id: int, resume_update: ResumeUpdate):
    db_resume = db.query(Resume).filter(Resume.id == resume_id).first()
    if db_resume:
        for key, value in resume_update.model_dump(exclude_unset = True).items():
            setattr(db_resume, key, value)
        db.commit()
        db.refresh(db_resume)
    return db_resume

# DELETE FROM Resumes WHERE id = []
def delete_resume(db: Session, resume_id: int):
    db_resume = db.query(Resume).filter(Resume.id == resume_id).first()
    if db_resume is None:
        return None

    db.delete(db_resume)
    db.commit()

    return db_resume