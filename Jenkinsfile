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
           
            sh 'C:\\Users\\Abdul Musawir\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip3 install -r requirements.txt'
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
