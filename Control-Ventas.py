import mysql.connector
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

# CRUD
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ventas_db"
)

# datos mensuales
def obtener_ventas_por_mes():
    query = "SELECT MONTH(fecha), SUM(monto) FROM ventas GROUP BY MONTH(fecha)"
    cursor = cnx.cursor()
    cursor.execute(query)
    datos = cursor.fetchall()
    cursor.close()
    return datos

# Función para generar el gráfico de ventas por mes
def generar_grafico_ventas():
    ventas = obtener_ventas_por_mes()
    meses = [mes for mes, _ in ventas]
    montos = [monto for _, monto in ventas]

    plt.bar(meses, montos)
    plt.xlabel('Mes')
    plt.ylabel('Ventas')
    plt.title('Análisis de Ventas por Mes')
    plt.show()

# mostrar datos
def mostrar_datos_ventas():
    ventas = obtener_ventas_por_mes()
    mensaje = "Mes\tVentas\n"
    for mes, monto in ventas:
        mensaje += f"{mes}\t{monto}\n"
    showinfo("Datos de ventas por mes", mensaje)

# insertar el dato
def agregar_venta():
    fecha = entry_fecha.get()
    monto = float(entry_monto.get())
    producto = entry_producto.get()
    cliente = entry_cliente.get()

    query = "INSERT INTO ventas (fecha, monto, producto, cliente) VALUES (%s, %s, %s, %s)"
    cursor = cnx.cursor()
    cursor.execute(query, (fecha, monto, producto, cliente))
    cnx.commit()
    cursor.close()

    showinfo("Venta agregada", "La venta se ha registrado correctamente.")

    # Limpiar los campos de entrada después de agregar la venta
    entry_fecha.delete(0, END)
    entry_monto.delete(0, END)
    entry_producto.delete(0, END)
    entry_cliente.delete(0, END)

# ventana principal
ventana = Tk()
ventana.title("Análisis de Ventas")
ventana.geometry("400x300")

# Estilos personalizados
style = ttk.Style()
style.configure("TButton",
    font=("Arial", 12),
    padding=10,
    width=20
)
style.configure("TLabel",
    font=("Arial", 12),
    padding=10
)
style.configure("TEntry",
    font=("Arial", 12),
    padding=10,
    width=20
)

# Etiquetas y campos de entrada para ingresar datos de venta
label_fecha = ttk.Label(ventana, text="Fecha (YYYY-MM-DD):")
label_fecha.pack()
entry_fecha = ttk.Entry(ventana)
entry_fecha.pack()

label_monto = ttk.Label(ventana, text="Monto:")
label_monto.pack()
entry_monto = ttk.Entry(ventana)
entry_monto.pack()

label_producto = ttk.Label(ventana, text="Producto:")
label_producto.pack()
entry_producto = ttk.Entry(ventana)
entry_producto.pack()

label_cliente = ttk.Label(ventana, text="Cliente:")
label_cliente.pack()
entry_cliente = ttk.Entry(ventana)
entry_cliente.pack()

# Botones
frame_botones = Frame(ventana)
frame_botones.pack(pady=10)

boton_agregar = ttk.Button(frame_botones, text="Agregar Venta", command=agregar_venta)
boton_agregar.pack(side=LEFT, padx=5)

boton_grafico = ttk.Button(frame_botones, text="Mostrar gráfico de ventas", command=generar_grafico_ventas)
boton_grafico.pack(side=LEFT, padx=5)

boton_datos = ttk.Button(frame_botones, text="Mostrar datos de ventas", command=mostrar_datos_ventas)
boton_datos.pack(side=LEFT, padx=5)

# Iniciar bucle de eventos
ventana.mainloop()


cnx.close()
