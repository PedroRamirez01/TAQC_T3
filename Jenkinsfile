pipeline {
  agent any

  environment {
    TOKEN = credentials('TOKEN')
  }

  stages {
    stage('Install Docker') {
      steps {
        sh 'sudo docker exec -it <nombre_o_id_del_contenedor> bash'
        sh 'apt-get update && apt-get upgrade'

        sh '''
          echo "🔧 Eliminando paquetes conflictivos..."
          for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do
            apt-get remove -y $pkg
          done

          echo "📦 Instalando paquetes necesarios..."
          apt-get update
          apt-get install -y ca-certificates curl gnupg lsb-release

          echo "🔐 Agregando clave GPG de Docker..."
          install -m 0755 -d /etc/apt/keyrings
          curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
          chmod a+r /etc/apt/keyrings/docker.asc

          echo "📋 Agregando repositorio de Docker..."
          echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
          https://download.docker.com/linux/debian $(. /etc/os-release && echo "$VERSION_CODENAME") stable" \
          > /etc/apt/sources.list.d/docker.list

          echo "🔄 Actualizando lista de paquetes..."
          apt-get update

          echo "📥 Instalando Docker Engine y complementos..."
          apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

          echo "✅ Docker instalado correctamente:"
          docker --version
        '''

        // sh 'chmod +x docker-install.sh'
        // sh './docker-install.sh'
      }
    }
    stage('Clean Workspace') {
      steps {
        deleteDir()
        sh 'docker stop container_ecomus_image || true'
        sh 'docker rm container_ecomus_image || true'
      }
    }

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
        sh 'docker run -d --name container_ecomus_image -e TOKEN=$TOKEN -p 8082:8082 ecomus_image'
        sh 'docker exec container_ecomus_image pytest --html=ecomus/report/report.html --self-contained-html || true'
        sh 'docker exec -d container_ecomus_image python3 -m http.server 8082 --directory ecomus/report/'
      }
    }
  }
}
