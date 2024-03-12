pipeline {
    agent any

    stages {
        stage('Cloning repository') {
            steps {
                git 'https://github.com/musawir696/mlops_cs.git'
            }
        }

        stage('Installation of dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Execution of test.py') {
            steps {
                sh 'python test.py'
            }
        }

       
    }
}
