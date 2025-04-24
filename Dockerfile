# Usa la imagen base oficial de Jenkins
FROM jenkins/jenkins:lts

# Cambia al usuario root para poder instalar cosas
USER root

# Actualiza los repositorios y luego instala Docker CLI y Python 3
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    docker.io

# Da permisos al usuario de Jenkins para usar Docker
RUN usermod -aG docker jenkins

# Cambia al usuario de Jenkins
USER jenkins
