pipeline {
    agent any

    stages {
        stage('Cloning repository') {
            steps {
                git 'https://github.com/your/repository.git'
            }
        }

        stage('Installation of dependencies') {
            steps {
                sh 'your_dependency_installation_command_here'
            }
        }

        stage('Execution of test.py') {
            steps {
                sh 'python test.py'
            }
        }

        stage('Deploying step') {
            steps {
                script {
                    def branchName = sh(script: 'git rev-parse --abbrev-ref HEAD', returnStdout: true).trim()
                    if (branchName == 'main') {
                        echo 'Deploying to production'
                        // Add deployment to production steps here
                    } else {
                        echo 'Deploying to UAT'
                        // Add deployment to UAT steps here
                    }
                }
            }
        }
    }
}
