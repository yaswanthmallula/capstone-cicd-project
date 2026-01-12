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

        stage('Run Unit Tests') {
            steps {
                bat 'docker run --rm backend pytest'
            }
        }

        stage('Security Scan (Trivy)') {
            steps {
                bat '''
                echo Scanning BACKEND image...
                docker run --rm aquasec/trivy:latest image ^
                --severity HIGH,CRITICAL ^
                --exit-code 0 ^
                backend

                echo Scanning FRONTEND image...
                docker run --rm aquasec/trivy:latest image ^
                --severity HIGH,CRITICAL ^
                --exit-code 0 ^
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
                timeout /t 10
                curl http://localhost:5000/health
                '''
            }
        }
    }

    post {
        success {
            echo ' CI/CD Pipeline completed successfully!'
        }
        failure {
            echo ' Pipeline failed. Check logs.'
        }
    }
}
