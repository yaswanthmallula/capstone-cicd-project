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
                sh 'docker build -t backend-app ./backend'
            }
        }

        stage('Build Frontend Image') {
            steps {
                sh 'docker build -t frontend-app ./frontend'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --rm backend-app pytest'
            }
        }

        stage('Deploy (Docker Compose)') {
            steps {
                sh 'docker-compose up -d --build'
            }
        }
    }
}
