# Análisis de Ventas con Interfaz de Usuario y Base de Datos MySQL - Por Camilo Andrés Gonzales y Miguel Angel Cataño (@MiguelC2004)

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

3. Crea una base de datos en MySQL y configura los parámetros de conexión en el archivo `ventas.py`:

   ```python
   cnx = mysql.connector.connect(
       host="localhost",
       user="tu_usuario",
       password="tu_contraseña",
       database="nombre_de_la_base_de_datos"
   )```
   
4. Ejecuta el script ventas.py para iniciar la aplicación de análisis de ventas.

## USO

1. Al iniciar la aplicación, se mostrará un menú de opciones:
- Mostrar análisis de ventas por mes
- Salir

2. Selecciona la opción 1 para ver el análisis de ventas por mes.

3. El programa consultará la base de datos y generará un gráfico de barras que muestra las ventas por mes.

4. Para salir de la aplicación, selecciona la opción 2 en el menú.
