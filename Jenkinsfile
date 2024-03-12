pipeline {
    agent any
    
    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/musawir696/mlops_cs.git'
            }
        }
        
        stage('Install dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        
        stage('Run tests') {
            steps {
                script {
                    sh 'pytest test.py'
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
