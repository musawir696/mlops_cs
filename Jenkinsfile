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
           
            bat 'pip install -r requirements.txt'
        }
    }
}

        
        stage('Run tests') {
            steps {
                script {
                    bat 'pytest test.py'
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
