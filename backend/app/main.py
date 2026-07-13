"""
    starting point of backend
    responsibilities
    - Create the FastAPI application.
    - Register all API routes.
    - Configure global settings.
"""

from fastapi import FastAPI
from app.routers import companies, resumes

app = FastAPI(
    title="JobTracker Backend", 
    description="Backend API for JobTracker application")

app.include_router(companies.router)
app.include_router(resumes.router)

@app.get("/")#handles http GET requests to the root endpoint ("/") of the API http://localhost:8000/

def root():
    return {"message": "Welcome to the JobTracker Backend API!"}