pipeline {
    agent any

    environment {
        IMAGE_NAME = "akshayms18/microdegree"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('git checkout'){
            steps {
                echo "Checking out code from gill repository"
            }
        }
        stage("building docker images"){
            steps {
                echo "Building docker image using Dockerfile"
                sh "docker build -t $IMAGE_NAME:$IMAGE_TAG ."
            }
        }
        stage("pushing docker image to dockerhub"){
            steps{
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                    sh "echo $DOCKER_PASS | $DOCKER_USER --password-stdin"
                    //sh "docker tag $IMAGE_NAME:latest $DOCKER_USER/$IMAGE_NAME:$IMAGE_TAG"
                    sh "docker push $IMAGE_NAME:$IMAGE_TAG"
                }
            }
        }
        stage("Deploy Docker containers to EC2"){
            steps {
                sh '''
                    echo "Deploying Docker containers to EC2 instance"
                    echo "Pulling Docker image from Docker HUb"
                    sh "docker pull $IMAGE_NAME:$IMAGE_TAG"

                    echo "Running Docker container on EC2 instance"
                    sh "docker run -d -p 8080:8080 $IMAGE_NAME:$IMAGE_TAG"
                   '''
            }
        }
    }
}