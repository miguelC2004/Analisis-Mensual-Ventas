import mysql.connector
import matplotlib.pyplot as plt

# Conexión a la base de datos
cnx = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="nombre_de_la_base_de_datos"
)

# Función para obtener los datos de ventas por mes
def obtener_ventas_por_mes():
    query = "SELECT MONTH(fecha), SUM(monto) FROM ventas GROUP BY MONTH(fecha)"
    cursor = cnx.cursor()
    cursor.execute(query)
    datos = cursor.fetchall()
    cursor.close()
    return datos

# Función para generar el gráfico de ventas por mes
def generar_grafico_ventas(datos):
    meses = [mes for mes, _ in datos]
    montos = [monto for _, monto in datos]

    plt.bar(meses, montos)
    plt.xlabel('Mes')
    plt.ylabel('Ventas')
    plt.title('Análisis de Ventas por Mes')
    plt.show()

# Interfaz de usuario
while True:
    print("1. Mostrar análisis de ventas por mes")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        ventas = obtener_ventas_por_mes()
        generar_grafico_ventas(ventas)
    elif opcion == '2':
        break
    else:
        print("Opción inválida. Intente nuevamente.")

# Cierre de la conexión a la base de datos
cnx.close()
