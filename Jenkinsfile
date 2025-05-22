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
        sh 'TOKEN=$TOKEN pytest ecomus/test -k "end_to_end" --html=ecomus/report/report.html --self-contained-html || true'
      }
    }
    
    stage('Test') {
      steps {
        sh """. ../venv/bin/activate
        pytest --junitxml=results.xml"""
      }
      post {
        always {
          junit 'results.xml'
        }
      }
    }
  }
}