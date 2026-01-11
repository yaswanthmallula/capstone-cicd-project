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

       stage('Deploy (Docker Compose)') {
    steps {
        bat 'docker compose up -d --build'
    }
}

    }
}
