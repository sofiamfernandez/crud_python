from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import sqlite3
import re


# funciones para la base de datos
def conexion():
    con = sqlite3.connect("Ventas.db")
    return con


def crear_tabla():
    con = conexion()
    cursor = con.cursor()
    sql = """CREATE TABLE IF NOT EXISTS productos
             (codigo INTEGER PRIMARY KEY,
             descripcion varchar(50) NOT NULL,
             stock_m INTEGER,
             precio REAL)
    """
    cursor.execute(sql)
    con.commit()


# funcion para alta,uso de condicional, regex y notificacion de evento realizado


def cargar(codigo, descripcion, stock_m, precio, tree):
    if not re.match(r"^[0-9\s]+$", codigo):
        showerror(
            "Error: No se puede cargar",
            "El codigo solo admite números y no puede quedar vacío",
        )
        return

    if not re.match(r"^[A-Za-z0-9\s]+$", descripcion):
        showerror(
            "Error: No se puede cargar",
            "El detalle no puede ser nulo ni contener caracteres especiales",
        )
        return

    if not re.match(r"^[0-9\s]+$", stock_m):
        showerror(
            "Error: No se puede cargar",
            "El stock mínimo debe ser un número no nulo",
        )
        return

    if not re.match(r"^[0-9.\s]+$", precio):
        showerror(
            "Error: No se puede cargar",
            "El precio debe ser un número no nulo",
        )
        return

    print(codigo, descripcion, stock_m, precio)
    con = conexion()
    cursor = con.cursor()
    data = (codigo, descripcion, stock_m, precio)
    sql = (
        "INSERT INTO productos(codigo, descripcion, stock_m, precio) VALUES(?, ?, ?, ?)"
    )
    cursor.execute(sql, data)
    con.commit()
    print("Producto registrado")
    actualizar_treeview(tree)


# funcion para la baja
def eliminar(tree):
    valor = tree.selection()
    print(valor)
    item = tree.item(valor)
    print(item)
    print(item["text"])
    mi_codigo = item["text"]

    con = conexion()
    cursor = con.cursor()

    data = (mi_codigo,)
    sql = "DELETE FROM productos WHERE codigo = ?;"
    cursor.execute(sql, data)
    con.commit()
    tree.delete(valor)


# consulta y uso de bucles
def actualizar_treeview(mitreview):
    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)

    sql = "SELECT * FROM productos ORDER BY codigo ASC"
    con = conexion()
    cursor = con.cursor()
    datos = cursor.execute(sql)

    resultado = datos.fetchall()
    for fila in resultado:
        print(fila)
        mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))


# definición de función modificación de producto
def modificar(codigo, descripcion, stock_m, precio, tree):
    valor = tree.selection()
    item = tree.item(valor)
    mi_codigo = item["text"]

    con = conexion()
    cursor = con.cursor()
    data = (codigo, descripcion, stock_m, precio, mi_codigo)
    sql = "UPDATE productos SET codigo=?, descripcion=?, stock_m=?, precio=? WHERE codigo=?"
    cursor.execute(sql, data)
    con.commit()
    print("Producto modificado")
    actualizar_treeview(tree)


# llamada a la funcion para conexion de base de datos y creacion de tabla
conexion()
crear_tabla()


# ventana
master = Tk()
master.title("Control de Productos")
master.configure(bg="#064C71")

# titulo

titulo = Label(
    master,
    text="CRUD Productos",
    bg="#91D8F7",
    fg="black",
    font=("Arial", 14, "bold"),
)
titulo.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky=W + E)

# variables
codigo = Label(master, text="Código", font=("None", 11))
codigo.grid(row=1, column=0, sticky=W)
detalle = Label(master, text="Detalle", font=("Arial", 11))
detalle.grid(row=2, column=0, sticky=W)
stock_m = Label(master, text="Stock Minimo", font=("Arial", 11))
stock_m.grid(row=3, column=0, sticky=W)
precio = Label(master, text="Precio Unitario", font=("Arial", 11))
precio.grid(row=4, column=0, sticky=W)

# variables de tkinter
var_codigo = StringVar()
var_detalle = StringVar()
var_stock_m = StringVar()
var_precio = StringVar()

# campos de entrada
entry_codigo = Entry(master, textvariable=var_codigo, width=25)
entry_codigo.grid(row=1, column=1)
entry_detalle = Entry(master, textvariable=var_detalle, width=25)
entry_detalle.grid(row=2, column=1)
entry_stock_m = Entry(master, textvariable=var_stock_m, width=25)
entry_stock_m.grid(row=3, column=1)
entry_precio = Entry(master, textvariable=var_precio, width=25)
entry_precio.grid(row=4, column=1)

# treeview
tree = ttk.Treeview(master)
tree["columns"] = ("col1", "col2", "col3")
tree.column("#0", width=50, minwidth=10, anchor=W)
tree.column("col1", width=200, minwidth=30, anchor=W)
tree.column("col2", width=100, minwidth=50, anchor=W)
tree.column("col3", width=90, minwidth=40, anchor=W)


tree.heading("#0", text="Código")
tree.heading("col1", text="Detalle")
tree.heading("col2", text="Stock Mínimo")
tree.heading("col3", text="Precio")


tree.grid(column=0, row=7, columnspan=3, padx=10, pady=10)

# botones con funciones lambda
boton_cargar = Button(
    master,
    text="Cargar Producto",
    command=lambda: cargar(
        var_codigo.get(), var_detalle.get(), var_stock_m.get(), var_precio.get(), tree
    ),
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
boton_cargar.grid(row=5, column=1, pady=5)

boton_eliminar = Button(
    master,
    text="Eliminar",
    command=lambda: eliminar(tree),
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
boton_eliminar.grid(row=8, column=1, pady=10)

boton_modificar = Button(
    master,
    text="Modificar",
    command=lambda: modificar(
        var_codigo.get(), var_detalle.get(), var_stock_m.get(), var_precio.get(), tree
    ),
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
boton_modificar.grid(row=5, column=2, pady=10)

actualizar_treeview(tree)
master.mainloop()
