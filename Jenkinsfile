pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Backend Image') {
            steps {
                bat 'docker build -t backend ./backend'
            }
        }

        stage('Build Frontend Image') {
            steps {
                bat 'docker build -t frontend ./frontend'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'docker run --rm backend pytest'
            }
        }

        // 🔐 STEP 4.2 — TRIVY SECURITY SCAN
        stage('Security Scan (Trivy)') {
            steps {
                bat '''
                docker run --rm ^
                  -v //var/run/docker.sock:/var/run/docker.sock ^
                  aquasec/trivy:0.50.1 image ^
                  --severity HIGH,CRITICAL ^
                  --exit-code 1 ^
                  backend

                docker run --rm ^
                  -v //var/run/docker.sock:/var/run/docker.sock ^
                  aquasec/trivy:0.50.1 image ^
                  --severity HIGH,CRITICAL ^
                  --exit-code 1 ^
                  frontend
                '''
            }
        }

        stage('Deploy (Docker Compose)') {
            steps {
                bat 'docker compose down'
                bat 'docker compose up -d --build'
            }
        }

        stage('Verify Health Endpoint') {
            steps {
                bat '''
                timeout /t 5
                curl http://localhost:5000/health
                '''
            }
        }
    }
}
