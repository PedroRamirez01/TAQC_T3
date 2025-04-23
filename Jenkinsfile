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
        sh 'docker build --build-arg TOKEN=$TOKEN -t ecomus_image .'
      }
    }

    stage('Run Docker') {
      steps {
        sh 'docker run -it -p 8081:80 ecomus_image'
      }
    }
  }
}
