pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                sh 'ls -l'
                sh 'python web_app.py'
            }
        }
    }
}
