pipeline {
  agent any

  environment {
    TOKEN = credentials('TOKEN')
  }

  stages {
    stage('Clean Workspace') {
      steps {
        deleteDir()
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
        sh 'docker run -d -e TOKEN=$TOKEN -p 8082:8082 ecomus_image'
      }
    }
  }
}
