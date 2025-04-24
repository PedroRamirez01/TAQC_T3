
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
  pytest --html=ecomus/report/report.html --self-contained-html
```
