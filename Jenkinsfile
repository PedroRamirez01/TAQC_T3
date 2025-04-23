pipeline {
  agent any

  environment {
    TOKEN = credentials('TOKEN')
  }

  stages {
    stage('Verificar Docker') {
      steps {
        sh 'docker --version'
      }
    }
    stage('Build Docker') {
      steps {
        sh 'docker build --build-arg TOKEN=$TOKEN -t ecomus_image .'
      }
    }
  }
}