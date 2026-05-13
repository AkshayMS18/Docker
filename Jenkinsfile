pipeline {
    agent any
    stages {
        stage('git checkout'){
            steps {
                echo "Checking out code from gill repository"
            }
        }
        stage("building docker images"){
            steps {
                echo "Building docker image using Dockerfile"
                sh "docker build -t microdegree:latest ."
            }
        }
        stage("pushing docker image to dockerhub"){
            steps{
                echo "Pushing docker image to dockerhub"
            }
        }
        stage("Deploy Docker containers"){
            steps {
                echo "Deploying docker containers using docker-compose"
            }
        }
    }
}