import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import mysql.connector
import pandas as pd

def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ventas_db"
        )
        cursor = connection.cursor()
        return connection, cursor
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error connecting to the database: {err}")
        return None, None

def create_table():
    connection, cursor = connect_db()
    if connection and cursor:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ventas (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    fecha DATE NOT NULL,
                    monto DECIMAL(10, 2) NOT NULL,
                    producto VARCHAR(50) NOT NULL,
                    cliente VARCHAR(100) NOT NULL
                );
            """)
            connection.commit()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error creating table: {err}")
        finally:
            connection.close()

# insert para la base de datos
def insert_sale():
    fecha = entry_fecha.get()
    monto = entry_monto.get()
    producto = entry_producto.get()
    cliente = entry_cliente.get()

    if fecha and monto and producto and cliente:
        connection, cursor = connect_db()
        if connection and cursor:
            try:
                cursor.execute("""
                    INSERT INTO ventas (fecha, monto, producto, cliente)
                    VALUES (%s, %s, %s, %s)
                """, (fecha, monto, producto, cliente))
                connection.commit()
                messagebox.showinfo("Success", "Sale added successfully!")
                clear_entries()
                show_sales()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error inserting sale: {err}")
            finally:
                connection.close()
    else:
        messagebox.showwarning("Warning", "Please fill in all the fields.")

# ver la lista
def show_sales():
    connection, cursor = connect_db()
    if connection and cursor:
        try:
            cursor.execute("SELECT * FROM ventas")
            result = cursor.fetchall()

            columns = ["ID", "Fecha", "Monto", "Producto", "Cliente"]
            df = pd.DataFrame(result, columns=columns)

            # elimina los entries cuando acaba
            for item in tree.get_children():
                tree.delete(item)

            # Insert
            for i, row in df.iterrows():
                tree.insert("", "end", values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error fetching sales data: {err}")
        finally:
            connection.close()

# esto genera la grafica
def generate_chart():
    connection, cursor = connect_db()
    if connection and cursor:
        try:
            cursor.execute("SELECT producto, SUM(monto) FROM ventas GROUP BY producto")
            result = cursor.fetchall()

            # Usar pandas para el data handling
            columns = ["Producto", "Total Ventas"]
            df = pd.DataFrame(result, columns=columns)

            # Extraer data
            products = df["Producto"]
            total_sales = df["Total Ventas"]

            # Crear el matplotlib
            fig = Figure(figsize=(6, 4), dpi=100)
            ax = fig.add_subplot(111)

            # graficas 1
            ax.bar(products, total_sales, color='blue')
            ax.set_xlabel('Producto')
            ax.set_ylabel('Total Ventas')
            ax.set_title('Ventas por Producto')

            # Tkinter para el canvas
            canvas = FigureCanvasTkAgg(fig, master=chart_frame)
            canvas_widget = canvas.get_tk_widget()

            canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error fetching sales data: {err}")
        finally:
            connection.close()

def clear_entries():
    entry_fecha.delete(0, tk.END)
    entry_monto.delete(0, tk.END)
    entry_producto.delete(0, tk.END)
    entry_cliente.delete(0, tk.END)

root = tk.Tk()
root.title("Sales CRUD Application")

create_table()

style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", font=('Helvetica', 12))

label_fecha = ttk.Label(root, text="Fecha:")
label_monto = ttk.Label(root, text="Monto:")
label_producto = ttk.Label(root, text="Producto:")
label_cliente = ttk.Label(root, text="Cliente:")

entry_fecha = ttk.Entry(root)
entry_monto = ttk.Entry(root)
entry_producto = ttk.Entry(root)
entry_cliente = ttk.Entry(root)

button_insert = ttk.Button(root, text="Insertar Venta", command=insert_sale)
button_show = ttk.Button(root, text="Mostrar Ventas", command=show_sales)
button_generate_chart = ttk.Button(root, text="Generar Gráfico", command=generate_chart)

# ver la data de las ventas
columns = ("ID", "Fecha", "Monto", "Producto", "Cliente")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Set column headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=80)

chart_frame = ttk.Frame(root)


label_fecha.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_fecha.grid(row=0, column=1, padx=10, pady=5, sticky="w")
label_monto.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_monto.grid(row=1, column=1, padx=10, pady=5, sticky="w")
label_producto.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_producto.grid(row=2, column=1, padx=10, pady=5, sticky="w")
label_cliente.grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_cliente.grid(row=3, column=1, padx=10, pady=5, sticky="w")

button_insert.grid(row=4, column=0, columnspan=2, pady=10)
button_show.grid(row=5, column=0, columnspan=2, pady=10)
button_generate_chart.grid(row=6, column=0, columnspan=2, pady=10)

tree.grid(row=0, column=2, rowspan=7, padx=10, pady=10, sticky="nsew")
chart_frame.grid(row=0, column=3, rowspan=7, padx=10, pady=10, sticky="nsew")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

root.mainloop()
