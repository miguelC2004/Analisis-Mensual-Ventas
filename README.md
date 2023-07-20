# Análisis de Ventas con Interfaz de Usuario y Base de Datos MySQL

Este es un proyecto de análisis de ventas que utiliza Python como lenguaje de programación, una base de datos MySQL para almacenar la información de ventas y la biblioteca Matplotlib para generar gráficos interactivos.

El objetivo principal del proyecto es brindar una interfaz de usuario intuitiva que permita a los usuarios analizar las ventas por mes y visualizar los resultados en forma de gráfico de barras.

## Características

- Conexión a una base de datos MySQL para almacenar y recuperar los datos de ventas.
- Análisis de ventas por mes utilizando consultas SQL.
- Generación de gráficos de barras utilizando la biblioteca Matplotlib.
- Interfaz de usuario sencilla con un menú de opciones.

## Requisitos del Sistema

- Python 3.x
- Módulo `mysql-connector-python` instalado (puedes instalarlo con `pip install mysql-connector-python`)

## Configuración

1. Clona este repositorio en tu máquina local.

2. Asegúrate de tener una instancia de MySQL en ejecución.

3. Crea una base de datos en MySQL y configura los parámetros de conexión en el archivo `control_ventas.py`:

   ```python
   cnx = mysql.connector.connect(
       host="localhost",
       user="root",
       password="",
       database="ventas_db"
   )```
   
4. Ejecuta el script control_ventas.py para iniciar la aplicación de análisis de ventas.
