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

    stage('Activate venv') {
      steps {
        script {
          sh '. ../venv/bin/activate'
        }
      }
    }

    stage('Update Dependencies') {
      steps {
        sh 'pip install --break-system-packages -r requirements.txt'
      }
    }    

    stage('Run tests') {
      steps {
        sh 'TOKEN=$TOKEN pytest ecomus/test --junitxml=results.xml || true'
      }
      post {
        always {
          junit 'results.xml'
        }
      }
    }
  }
}