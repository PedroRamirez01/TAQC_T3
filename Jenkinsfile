pipeline {
  agent any

  environment {
    TOKEN = credentials('TOKEN')
  }

  stages {
    stage('Configurar Git safe.directory') {
      steps {
        sh 'git config --global --add safe.directory /var/jenkins_home/workspace/ecomus'
      }
    }
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