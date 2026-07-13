"""
    this file describes what your database tables look like
    - define one python class for each table in your database
""" 

from sqlalchemy import Column, Integer, String, DateTime, func, Text, ForeignKey
from sqlalchemy.sql import func

from app.database import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key = True, index = True)
    company_name = Column(Text, nullable = False)
    website = Column(String(255), nullable = True)
    industry = Column(String(255), nullable = True)
    headquarters = Column(String(255), nullable = True)
    company_size = Column(String(255), nullable = True)
    glassdoor_url = Column(String(255), nullable = True)
    linkedin_url = Column(String(255), nullable = True)

    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), server_default = func.now(), onupdate = func.now())

    def __repr__(self):
        return f"<Company(id={self.id}, company_name='{self.company_name}', website='{self.website}')>" 

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False,index=True)
    resume_name = Column(Text, nullable=False)
    version = Column(String(255), nullable=False)
    file_path = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column( DateTime(timezone=True), server_default=func.now())
    updated_at = Column( DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return (
            f"<Resume(id={self.id}, "
            f"resume_name='{self.resume_name}')>"
        )
    