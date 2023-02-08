pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                git 'https://github.com/Maze226/tests.git'
                sh 'ls -l'
                sh 'python web_app.py'
            }
        }
    }
}
