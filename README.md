CI/CD Capstone Project – Docker & Jenkins
Project Overview

This project demonstrates a complete end-to-end CI/CD pipeline that automatically builds, tests, scans, deploys, and verifies a containerized two-tier web application using Docker, Jenkins, and Trivy.

The project follows real-world DevOps best practices and is suitable for:

Academic capstone submission

DevOps fresher interviews

CI/CD demonstrations

System Architecture
Application Architecture

Frontend (Static UI / Nginx)
Backend (Flask API)
Database (PostgreSQL)

Flow:
Frontend communicates with Backend, and Backend communicates with PostgreSQL.

CI/CD Pipeline Flow

Code is pushed to GitHub

Jenkins pipeline is triggered

Docker images are built

Unit tests are executed inside containers

Security scanning is performed using Trivy

Application is deployed using Docker Compose

Health endpoint is verified

Technology Stack
Category	Technology
Frontend	HTML / Nginx
Backend	Python (Flask)
Database	PostgreSQL
Containers	Docker
Orchestration	Docker Compose
CI/CD	Jenkins
Security	Trivy
Version Control	GitHub
Project Structure
capstone-cicd-project/
│
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── tests/
│       └── test_app.py
│
├── frontend/
│   └── Dockerfile
│
├── config/
│   ├── dev.env
│   ├── staging.env
│   └── prod.env
│
├── deploy/
│   ├── dev.sh
│   ├── staging.sh
│   └── prod.sh
│
├── docker-compose.yml
├── Jenkinsfile
└── README.md

Docker Implementation
Best Practices Followed

Separate Dockerfiles for frontend and backend

Lightweight base images

Efficient Docker layer caching

Environment variables managed through env files

No hard-coded secrets

Docker Compose Services

Frontend service

Backend service

PostgreSQL database

Persistent volume for database storage

Custom bridge network

Environment Configuration

Example: config/staging.env

DB_HOST=db
DB_PORT=5432
DB_NAME=appdb
DB_USER=appuser
DB_PASSWORD=apppass


Environment files support development, staging, and production deployments.

CI/CD Pipeline Using Jenkins
Pipeline Stages

Checkout source code from GitHub

Build Docker images for frontend and backend

Run unit tests inside backend container

Perform vulnerability scanning using Trivy

Deploy application using Docker Compose

Verify application health endpoint

Mark pipeline as success or failure

Security Scanning

Trivy is used to scan Docker images for operating system and application dependency vulnerabilities.
High and critical severity vulnerabilities are detected during the pipeline execution.
Image archive scanning is used for Windows Jenkins compatibility.

Health Check

Endpoint:

GET http://localhost:5000/health


Expected Response:

{
  "status": "UP",
  "database": "CONNECTED"
}


The pipeline proceeds only if the health check is successful.

How to Run Locally
docker compose up -d --build


Verification:

Frontend: http://localhost

Backend: http://localhost:5000

Health endpoint: http://localhost:5000/health

Troubleshooting
Container name conflict

Issue: Container already exists
Fix: Removed container_name from docker-compose.yml

Trivy scan failure on Windows

Issue: Docker socket not accessible
Fix: Used Docker image archive scanning

Database connection error

Issue: Backend cannot connect to database
Fix: Used service name db and environment variables

Jenkins pipeline failure

Fix: Checked Jenkins console output and resolved stage-specific errors

Key Deliverables Achieved

Working two-tier web application with database

Optimized Docker images

Complete CI/CD pipeline using Jenkins

Automated testing and security scanning

Docker Compose based deployment

Health verification

Professional documentation

Author

Yaswanth Mallula
DevOps Capstone Project

## Demo Video

A short demo video showing Jenkins pipeline execution and application health verification is available here:

Video Link:
https://drive.google.com/file/d/1spipO5loG2fZ1yr4oYaIUiaG9-occzAc/view?usp=sharing
