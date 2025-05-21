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
        sh 'python3 ecomus/report/fix_report.py ecomus/report/report.html || true'
        sh 'mkdir -p /var/www/html/reports || true'
        sh 'cp ecomus/report/report.html /var/www/html/reports/ || true'
        sh 'python3 -m http.server 8082 --directory ecomus/report/ &'
        echo 'Informe disponible en: http://200.104.35.128:8082/report.html'
      }
    }
    
    stage('Publish HTML Reports') {
      steps {
        publishHTML(target: [
          allowMissing: false,
          alwaysLinkToLastBuild: true,
          keepAll: true,
          reportDir: 'ecomus/report',
          reportFiles: 'report.html',
          reportName: 'Report'
        ])
      }
    }
  }
}