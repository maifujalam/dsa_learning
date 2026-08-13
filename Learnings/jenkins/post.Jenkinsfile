pipeline {
    agent any
    environment {
        HELM_VALUES_FILE = 'values.yaml'
        HELM_REPO_NAME= 'dev-apps'
    }
    parameters {
        string(name: 'GIT_REPO_NAME', defaultValue: 'https://github.com/maifujalam/k8s_aws_lite.git', description: 'Enter the git remote name')
        string(name: 'GIT_BRANCH_NAME', defaultValue: 'main', description: 'Enter the branch name to pull from')
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                script {
                    def abc = sh(script: 'echo "Hello World"', returnStdout: true).trim()
                    echo "${abc}"
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
    post {
        always {
            echo "This will always run"
            archiveArtifacts artifacts: 'target/*.jar',
                       fingerprint: true,
                       allowEmptyArchive: false
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
    }
}
