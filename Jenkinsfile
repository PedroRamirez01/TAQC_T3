pipeline {
  agent any
  // environment {
  //   TOKEN = credentials('TOKEN')
  // }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Activate venv') {
      steps {
        script {
          sh '. ./venv/bin/activate'
        }
      }
    }

    stage('Install Dependencies') {
      steps {
        sh 'pip install --break-system-packages -r requirements.txt'
        sh 'python -m playwright install --with-deps'
      }
    }

    stage('Run tests') {
      steps {
        sh 'pytest --html=ecomus/report/report.html --self-contained-html || true'
        sh 'python3 -m http.server 8082 --directory ecomus/report/'
      }
    }
  }
}