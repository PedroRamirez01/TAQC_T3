FROM jenkins/jenkins:lts

LABEL maintainer="TAQC - Team 3"
LABEL description="Jenkins with Python3, pip and Playwright"

USER root

# Establecer directorio de trabajo
WORKDIR /var/jenkins_home/workspace

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    gnupg \
    ca-certificates \
    && dpkg --configure -a \
    && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Crear entorno virtual Python
RUN python3 -m venv venv

# Actualizar pip e instalar dependencias
COPY requirements.txt /var/jenkins_home/workspace/
RUN venv/bin/pip install --upgrade pip \
    && venv/bin/pip install -r requirements.txt

# Instalar Playwright y sus dependencias
RUN venv/bin/pip install playwright \
    && venv/bin/playwright install --with-deps chromium

# Asegurar que el usuario jenkins tenga permisos sobre los directorios de trabajo
RUN mkdir -p /var/jenkins_home/workspace/ecomus \
    && chown -R jenkins:jenkins /var/jenkins_home/workspace \
    && chmod -R 755 /var/jenkins_home/workspace

# Volver al usuario jenkins para mejor seguridad
USER jenkins