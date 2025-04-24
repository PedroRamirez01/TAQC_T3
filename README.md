
# TAQC_T3

Automatización de pruebas utilizando Playwright para realizar un flujo completo de compra en una tienda en línea.


## Objetivo

El objetivo de este proyecto es automatizar el proceso de compra de un producto en una tienda en línea, desde el registro de un nuevo usuario hasta la finalización de la compra, asegurando que cada paso funcione correctamente.

## Tecnologías utilizadas

* Playwright - Framework de automatización de pruebas
* Python - Lenguaje de programación

## Flujo de automatización
1. **Registro de usuario:** Creación de una nueva cuenta en la tienda en línea.
2. **Inicio de sesión:** Autenticación con las credenciales del usuario registrado.
3. **Búsqueda de producto:** Localización de un producto específico en la tienda.
4. **Añadir al carrito:** Agregar una cantidad específica del producto al carrito de compras.
5. **Finalizar compra:** Completar el proceso de compra del producto.

##  Instalación y Ejecución
1. Clonar este repositorio:

```bash
  git clone https://github.com/tu-usuario/TAQC_T3.git
  cd TAQC_T3
```
2. Instalar dependencias:
```
  pip install -r requirements.txt
```

3. Ejecutar las pruebas:
```
  pytest --html=login/report/report.html --self-contained-html
```

##  Jenkins
1. Traer imagen desde Docker y levantar contenedor:

```bash
  sudo docker run --name jenkins-docker -u root -d -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkins/jenkins:lts 
```

2. Ingresar a la terminal de jenkins para instalar Docker dentro del contenedor:
```bash
  sudo docker exec -it jenkins-docker /bin/bash
  apt-get update
  apt-get upgrade
  apt-get install nano
```

3. Copiar script docker-install.sh dentro de archivo docker-install.sh:
```bash
  nano docker-install.sh
  ./docker-install.sh
```

4. Ingresar a Jenkins, añade TOKEN como credencial

5. Crea Job, pipeline ingresando url del proyecto

6. Ejecuta pipeline