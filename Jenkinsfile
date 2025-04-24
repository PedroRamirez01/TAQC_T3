pipeline {
  agent any

  environment {
    TOKEN = credentials('TOKEN')
  }

  stages {
    stage('Clean Workspace') {
      steps {
        deleteDir()
        sh 'docker stop container_ecomus_image || true'
        sh 'docker rm container_ecomus_image || true'
      }
    }

    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build Docker') {
      steps {
        sh 'docker build -t ecomus_image .'
      }
    }

    stage('Run Docker') {
      steps {
        sh 'docker run -d --name container_ecomus_image -e TOKEN=$TOKEN -p 8082:8082 ecomus_image'
      }
    }
  }
}
