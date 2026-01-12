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

        stage('Run Unit Tests (Backend)') {
            steps {
                bat 'docker run --rm backend pytest'
            }
        }

        stage('Security Scan (Trivy)') {
            steps {
                bat '''
                docker run --rm aquasec/trivy:latest image ^
                --severity HIGH,CRITICAL ^
                --exit-code 1 ^
                backend

                docker run --rm aquasec/trivy:latest image ^
                --severity HIGH,CRITICAL ^
                --exit-code 1 ^
                frontend
                '''
            }
        }

        stage('Deploy (Docker Compose)') {
            steps {
                bat 'docker compose down -v'
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

    post {
        always {
            echo 'Pipeline execution completed'
        }
        success {
            echo 'Deployment successful '
        }
        failure {
            echo 'Pipeline failed '
        }
    }
}
