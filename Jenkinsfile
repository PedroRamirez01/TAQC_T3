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

    // Las dependencias ya están instaladas en la imagen Docker
    // pero podemos actualizar si es necesario
    stage('Update Dependencies') {
      steps {
        sh 'pip install --break-system-packages -r requirements.txt'
      }
    }

    // Playwright ya está instalado en la imagen Docker
    stage('Run tests') {
      steps {
        sh 'TOKEN=$TOKEN pytest ecomus/test -k "end_to_end" --html=ecomus/report/report.html --self-contained-html || true'
        // sh 'python3 -m http.server 8082 --directory ecomus/report/'
      }
    }
  }
}