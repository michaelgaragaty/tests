pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                sh 'ls -l'
                sh 'python3 web_app.py'
            }
        }
    }
}
