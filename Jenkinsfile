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
        sh 'TOKEN=$TOKEN pytest ecomus/test -k "end_to_end" --junitxml=results.xml'
      }
      post {
        always {
          junit 'results.xml'
        }
      }
    }
  }
}