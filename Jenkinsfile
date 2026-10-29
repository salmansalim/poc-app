pipeline {
    agent any

    environment {
        DOCKER_HUB_USER = 'salmanvak'
        IMAGE_NAME      = 'poc-app'
        REGISTRY_CRED   = 'dockerhub-credentials-id' // ID from Jenkins Credential Store
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_HUB_USER}/${IMAGE_NAME}:${BUILD_NUMBER} ."
                sh "docker tag ${DOCKER_HUB_USER}/${IMAGE_NAME}:${BUILD_NUMBER} ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
            }
        }

        stage('Push to Registry') {
            steps {
                withCredentials([usernamePassword(credentialsId: "${REGISTRY_CRED}", usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                    sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:${BUILD_NUMBER}"
                    sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh "sed -i 's|<YOUR_DOCKERHUB_USERNAME>|${DOCKER_HUB_USER}|g' deployment.yaml"
                sh "kubectl apply -f deployment.yaml"
                sh "kubectl rollout restart deployment/poc-app"
            }
        }
    }
}