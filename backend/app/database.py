"""
    backend needs to know:
    - database, username, password, and port
    - create databse connection and sessions
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.orm import declarative_base

Base = declarative_base()

DATABASE_URL = "postgresql://postgres:password@localhost:5432/job_tracker"

#object used to connect to database
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind = engine)

class Base(DeclarativeBase):
    pass