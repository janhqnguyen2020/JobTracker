# REST API Design

## Overview

The backend will expose RESTful endpoints that allow the frontend to create, read, update, and delete data stored in PostgreSQL.

---

# Dashboard

## Get Dashboard Information

GET /dashboard

Returns:

- Total Applications
- Total Favorites
- Total Interviews
- Recent Applications
- Upcoming Interviews

---

# Users

## Get User

GET /users/{id}

Returns user information.

---

## Update User

PUT /users/{id}

Updates profile information.

---

# Companies

## Get All Companies

GET /companies

Returns every company.

---

## Get Company

GET /companies/{id}

Returns one company.

---

## Create Company

POST /companies

Creates a new company.

---

## Update Company

PUT /companies/{id}

Updates company information.

---

## Delete Company

DELETE /companies/{id}

Deletes a company.

---

# Resumes

## Get All Resumes

GET /resumes

---

## Get Resume

GET /resumes/{id}

---

## Upload Resume

POST /resumes

---

## Update Resume

PUT /resumes/{id}

---

## Delete Resume

DELETE /resumes/{id}

---

# Job Applications

## Get All Applications

GET /applications

---

## Get Application

GET /applications/{id}

---

## Create Application

POST /applications

---

## Update Application

PUT /applications/{id}

---

## Delete Application

DELETE /applications/{id}

---

## Update Status

PATCH /applications/{id}/status

Updates only the application status.

---

## Favorite Application

PATCH /applications/{id}/favorite

Updates the favorite flag.

---

# Interviews

## Get All Interviews

GET /interviews

---

## Get Interview

GET /interviews/{id}

---

## Create Interview

POST /interviews

---

## Update Interview

PUT /interviews/{id}

---

## Delete Interview

DELETE /interviews/{id}

---

# Future Endpoints

## Search Applications

GET /applications/search

---

## Filter Applications

GET /applications/filter

---

## Parse Job Posting

POST /applications/parse

Accepts a job posting URL and automatically extracts:

- Company
- Position
- Location
- Salary
- Employment Type

---

## Dashboard Analytics

GET /analytics