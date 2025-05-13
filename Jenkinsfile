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

    stage('Dependencies Installation') {
            steps {
                sh 'pip install --break-system-packages -r requirements.txt'
            }
        }

    stage('Playwright Installation') {
        steps {
            sh 'playwright install && playwright install-deps'
        }
    }

    stage('Run tests') {
      steps {
        sh 'pytest ecomus/test/test_login.py --html=ecomus/report/report.html --self-contained-html || true'
        // sh 'python3 -m http.server 8082 --directory ecomus/report/'
      }
    }
  }
}