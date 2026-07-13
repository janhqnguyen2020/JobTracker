# Architecture

## Overview

Job Tracker is a full-stack web application that helps users organize and track their job search.

The application consists of four major layers:

1. React Frontend
2. FastAPI Backend
3. SQLAlchemy ORM
4. PostgreSQL Database

Every action a user performs follows the same request lifecycle.

---

# High-Level Architecture

+-----------------------+
|      React UI         |
+-----------------------+
           |
           | HTTP Request
           v
+-----------------------+
|      FastAPI API      |
+-----------------------+
           |
           | SQLAlchemy
           v
+-----------------------+
|      PostgreSQL       |
+-----------------------+

The frontend never communicates directly with PostgreSQL.

All communication goes through the backend.

---

# Request Lifecycle

Example:

User creates a new application.

React
    │
    ▼
POST /applications
    │
    ▼
FastAPI Router
    │
    ▼
Validation
    │
    ▼
SQLAlchemy
    │
    ▼
PostgreSQL
    │
    ▼
Application Saved
    │
    ▼
JSON Response
    │
    ▼
React updates UI

---

# Project Structure

jobTracker/

├── README.md
│
├── docs/
│   ├── Architecture.md
│   ├── API.md
│   ├── ProjectPlan.md
│   ├── UserStories.md
│   └── ERD.png
│
├── database/
│   ├── schema.sql
│   ├── seed.sql
│   └── queries/
│
├── backend/
│
├── frontend/
│
└── .gitignore

---

# Backend Architecture

backend/

app/

main.py

database.py

models.py

schemas.py

crud.py

routers/

services/

The backend is organized into several layers.

React

↓

Router

↓

Service

↓

Database

---

## main.py

Purpose

Starts the FastAPI application.

Responsibilities

- Create FastAPI app
- Register routes
- Start server

---

## database.py

Purpose

Creates the PostgreSQL connection.

Responsibilities

- Database Engine
- Session Management

---

## models.py

Purpose

Represents PostgreSQL tables using SQLAlchemy models.

Example

Users

Companies

JobApplications

Interviews

Resumes

---

## schemas.py

Purpose

Defines request and response models using Pydantic.

Example

CreateCompanyRequest

ApplicationResponse

ResumeResponse

---

## routers/

Purpose

Defines API endpoints.

Example

GET /companies

POST /applications

PUT /interviews/{id}

DELETE /resumes/{id}

Routers should only receive requests and return responses.

Business logic belongs elsewhere.

---

## services/

Purpose

Contains business logic.

Examples

- Create Application
- Validate Resume
- Update Status
- Calculate Dashboard Statistics

---

## crud.py

Purpose

Executes database operations.

Examples

SELECT

INSERT

UPDATE

DELETE

This layer communicates with PostgreSQL.

---

# Frontend Architecture

frontend/

app/

components/

hooks/

pages/

services/

types/

---

## pages/

Represents each page in the application.

Dashboard

Applications

Companies

Interviews

Profile

---

## components/

Reusable UI.

Examples

Navbar

Sidebar

ApplicationTable

CompanyCard

ResumeCard

StatisticsCard

Modal

Button

SearchBar

Dropdown

---

## hooks/

React hooks.

Examples

useApplications()

useCompanies()

useDashboard()

---

## services/

Responsible for calling the backend API.

Examples

getApplications()

createCompany()

updateResume()

deleteInterview()

These functions communicate with FastAPI.

---

## types/

Stores shared TypeScript types.

Application

Company

Resume

Interview

Dashboard

---

# Database Architecture

Tables

Users

↓

Resumes

↓

Job Applications

↓

Interviews

Companies

↓

Job Applications

Relationships

Users

1 → Many Resumes

Users

1 → Many Job Applications

Companies

1 → Many Job Applications

Resumes

1 → Many Job Applications

Job Applications

1 → Many Interviews

---

# Page Architecture

Dashboard

Displays

- Statistics
- Recent Applications
- Upcoming Interviews

API

GET /dashboard

---

Applications

Displays

Application Table

Features

- Search
- Favorite
- Edit
- Delete

Endpoints

GET /applications

POST /applications

PUT /applications/{id}

DELETE /applications/{id}

PATCH /applications/{id}/favorite

PATCH /applications/{id}/status

---

Companies

Displays

Company Table

Endpoints

GET /companies

POST /companies

PUT /companies/{id}

DELETE /companies/{id}

---

Resumes

Displays

Resume Cards

Endpoints

GET /resumes

POST /resumes

PUT /resumes/{id}

DELETE /resumes/{id}

---

Interviews

Displays

Interview Table

Endpoints

GET /interviews

POST /interviews

PUT /interviews/{id}

DELETE /interviews/{id}

---

# Data Flow

Example

Create Application

User

↓

Clicks

"New Application"

↓

Application Modal Opens

↓

User Completes Form

↓

React validates fields

↓

POST /applications

↓

FastAPI validates request

↓

Business Logic

↓

SQLAlchemy

↓

PostgreSQL

↓

Application Created

↓

JSON Response

↓

React Refreshes Table

---

# Development Workflow

Phase 1

Planning

✓ User Stories

✓ ERD

✓ Database Schema

✓ API Design

✓ Architecture

---

Phase 2

Backend

- Connect PostgreSQL
- Build CRUD Endpoints
- Test using FastAPI Swagger

---

Phase 3

Frontend

- Build Pages
- Build Components
- Connect API

---

Phase 4

Dashboard

- Statistics
- Charts
- Analytics

---

Phase 5

Future Features

- AI Job Parsing
- Resume Recommendation
- Authentication
- Calendar Integration
- Notifications

---

# Design Principles

Keep business logic out of the frontend.

Frontend should display data.

Backend should process data.

Database should store data.

Every page should communicate only through REST APIs.

Every database operation should be validated before being committed.

All features should be built as complete vertical slices (Database → API → Frontend).
