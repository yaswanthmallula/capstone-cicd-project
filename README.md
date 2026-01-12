 CI/CD Capstone Project – Docker & Jenkins
 Project Overview

This project demonstrates a complete end-to-end CI/CD pipeline that automatically builds, tests, scans, deploys, and verifies a containerized 2-tier web application using Docker, Jenkins, and Trivy.

The pipeline ensures:

Code quality through automated testing

Security through container vulnerability scanning

Reliable deployments using Docker Compose

Health verification after deployment

 Architecture Overview
Application Architecture
Frontend (Nginx / Static UI)
        ↓
Backend (Flask API)
        ↓
PostgreSQL Database

CI/CD Flow
GitHub
   ↓
Jenkins Pipeline
   ↓
Docker Build
   ↓
Unit Tests
   ↓
Trivy Security Scan
   ↓
Docker Compose Deployment
   ↓
Health Check Verification

 Tech Stack
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
  Best Practices Used

Non-root users inside containers

Layer caching for faster builds

Environment variables via .env files

Lightweight base images

Docker Compose Services

frontend

backend

db (PostgreSQL)

Named volumes for DB persistence

Custom bridge network

  Environment Configuration

Example: config/staging.env

DB_HOST=db
DB_PORT=5432
DB_NAME=appdb
DB_USER=appuser
DB_PASSWORD=apppass

  CI/CD Pipeline (Jenkins)
Pipeline Stages

Checkout code from GitHub

Build Docker images

Run unit tests inside container

Trivy vulnerability scan (HIGH & CRITICAL)

Deploy using Docker Compose

Verify /health endpoint

Mark build SUCCESS / FAILURE

  Security Scanning (Trivy)

Scans Docker images for:

OS vulnerabilities

Language dependencies

Fails pipeline on HIGH / CRITICAL issues

Uses Docker image archive scanning for reliability

  Health Check

Endpoint:

GET http://localhost:5000/health


Successful Response:

{
  "status": "UP",
  "database": "CONNECTED"
}

  How to Run Locally
docker compose up -d --build


Verify:

Frontend → http://localhost

Backend → http://localhost:5000

Health → http://localhost:5000/health

  Troubleshooting Guide
Issue	Fix
Container name conflict	Remove container_name
DB not connecting	Check env files
Trivy image not found	Ensure image built before scan
Pipeline fails	Check Jenkins console logs
  Key Deliverables Achieved

✅ Working 2-tier application with DB

✅ Optimized Docker images

✅ Full CI/CD pipeline

✅ Security scanning

✅ Automated deployment

✅ Health verification

✅ Production-ready project structure

  Author

Yaswanth Mallula
DevOps Capstone Project
CI/CD | Docker | Jenkins | Security