# TAQC_T3

Automatización de pruebas utilizando Playwright para realizar un flujo completo de compra en una tienda en línea.

---

## 🎯 Objetivo

El objetivo de este proyecto es automatizar el proceso de compra de un producto en una tienda en línea, desde el registro de un nuevo usuario hasta la finalización de la compra, asegurando que cada paso funcione correctamente.

---

## 🧰 Tecnologías utilizadas

- **Playwright** – Framework de automatización de pruebas.
- **Python** – Lenguaje de programación.

---

## 🔁 Flujo de automatización

1. **Registro de usuario:** Creación de una nueva cuenta en la tienda en línea.
2. **Inicio de sesión:** Autenticación con las credenciales del usuario registrado.
3. **Búsqueda de producto:** Localización de un producto específico en la tienda.
4. **Añadir al carrito:** Agregar una cantidad específica del producto al carrito de compras.
5. **Finalizar compra:** Completar el proceso de compra del producto.

---

## 💻 Instalación y Ejecución

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/TAQC_T3.git
cd TAQC_T3
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecutar las pruebas:

```bash
pytest --html=login/report/report.html --self-contained-html
```

---

## ⚙️ Jenkins + Docker Setup

Este proyecto utiliza Jenkins dentro de un contenedor Docker para automatizar integraciones y despliegues.

### 🔧 Paso 1: Levantar Jenkins con Docker

```bash
sudo docker-compose build
sudo docker-compose up -d
```

### 🖥️ Paso 2: Acceder a la terminal de Jenkins

```bash
sudo docker exec -it jenkins bash
```

> Asegúrate de que el nombre del contenedor coincida con el definido en tu `docker-compose.yml`.

### 🔐 Paso 3: Crear credencial 'TOKEN'

En la interfaz web de Jenkins (`http://localhost:8080`):

1. Ve a **"Manage Jenkins" > "Credentials"**.
2. Selecciona el almacén de credenciales (por ejemplo, "(global)").
3. Crea una nueva credencial:
   - Tipo: **Secret text**
   - ID: `TOKEN`
   - Secret: tu token personal de GitHub.

### 🛠️ Paso 4: Configurar un Job (Pipeline)

1. Crea un nuevo ítem en Jenkins y selecciona **"Pipeline"**.
2. Marca la opción **GitHub project** y coloca:
   ```
   https://github.com/tu-usuario/TAQC_T3.git
   ```
3. En la sección **Pipeline**:
   - **Definition**: `Pipeline script from SCM`
   - **SCM**: `Git`
   - **Repository URL**:
     ```
     https://github.com/tu-usuario/TAQC_T3.git
     ```
   - **Branches to build**:
     ```
     */main
     ```

### ▶️ Paso 5: Ejecutar el Job

Haz clic en **"Build Now"** para correr el pipeline.
