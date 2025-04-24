pipeline {
  agent any

  environment {
    TOKEN = credentials('TOKEN')
  }

  stages {
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
        sh 'docker run -d --name jenkins-docker -e TOKEN=$TOKEN -p 8082:8082 ecomus_image'
        sh 'docker exec jenkins-docker pytest --html=ecomus/report/report.html --self-contained-html || true'
        sh 'docker exec -d jenkins-docker python3 -m http.server 8082 --directory ecomus/report/'
      }
    }
  }
}