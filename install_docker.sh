#!/bin/bash

echo "🔧 Eliminando paquetes conflictivos..."
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do
  apt-get remove -y $pkg
done

echo "📦 Instalando paquetes necesarios..."
apt-get update
apt-get install -y ca-certificates curl gnupg

echo "🔐 Agregando clave GPG de Docker..."
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
chmod a+r /etc/apt/keyrings/docker.asc

echo "📋 Agregando repositorio de Docker..."
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
  https://download.docker.com/linux/debian $(. /etc/os-release && echo "$VERSION_CODENAME") stable" \
  > /etc/apt/sources.list.d/docker.list

echo "🔄 Actualizando lista de paquetes..."
apt-get update

echo "📥 Instalando Docker Engine y complementos..."
apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

echo "✅ Docker instalado correctamente. Verifica con: docker --version"
