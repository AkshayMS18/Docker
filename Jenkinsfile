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
            }
        }
    }
}