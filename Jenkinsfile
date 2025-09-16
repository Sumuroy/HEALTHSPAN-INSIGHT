pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'myapp:latest'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    echo 'Building the Docker image...'
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'Running tests...'
                    sh 'docker run --rm $DOCKER_IMAGE pytest'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying to Kubernetes...'
                    sh 'kubectl apply -f kubernetes/deployment.yaml'
                }
            }
        }
    }
}
