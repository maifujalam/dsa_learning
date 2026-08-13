pipeline {
    agent any;
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                script {
                output=sh 'ls -al', returnStdout: true
                echo "Output: ${output}"
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }

}