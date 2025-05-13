FROM jenkins/jenkins:lts

LABEL maintainer="TAQC - Team 3"
LABEL description="Jenkins with Python3, pip and Playwright"

USER root

# Instalar Python, pip y dependencias necesarias para Playwright
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Crear el directorio para los reportes
RUN mkdir -p /var/jenkins_home/workspace/ecomus/report && \
    chown -R jenkins:jenkins /var/jenkins_home/workspace

# Volver al usuario jenkins para mayor seguridad
USER jenkins

# No es necesario añadir CMD o ENTRYPOINT ya que usaremos los predeterminados de la imagen jenkins