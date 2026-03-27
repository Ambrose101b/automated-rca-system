pipeline {
    // This tells Jenkins it can run on any available worker machine
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Pulls the latest code from your GitHub repository
                checkout scm
                echo 'Code successfully checked out!'
            }
        }

        stage('Syntax Check (Linting)') {
            steps {
                dir('rca_engine') {
                    // A quick check to make sure our Python code doesn't have fatal typos
                    echo 'Checking Python syntax for RCA Engine...'
                    sh 'python3 -m py_compile monitor.py collector.py'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('app') {
                    // Automatically build the new Docker image for our Target App
                    echo 'Building the Target App Docker Container...'
                    sh 'docker build -t rca-target-app:latest .'
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully! The new Docker image is ready.'
        }
        failure {
            echo 'Pipeline failed! Check the logs to see what broke.'
        }
    }
}