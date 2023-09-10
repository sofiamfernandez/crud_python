import sqlite3


class BaseDatos:  # la base de datos
    def conexion(self):
        con = sqlite3.connect("Ventas.db")
        return con

    def crear_tabla(self):
        con = self.conexion()
        cursor = con.cursor()
        sql = """CREATE TABLE IF NOT EXISTS productos
             (codigo INTEGER PRIMARY KEY,
             descripcion varchar(50) NOT NULL,
             stock_m INTEGER,
             precio REAL)
             """

        cursor.execute(sql)
        con.commit()
        self.conexion()
        self.crear_tabla()


class Elemento:
    def __init__(self, codigo, detalle, stock_min, precio):
        self.codigo = codigo
        self.detalle = detalle
        self.stock_min = stock_min
        self.precio = precio


class ListaElementos:
    def __init__(self):
        self.elementos = []

    def agregar_elemento(self, codigo, detalle, stock_min, precio):
        elemento = Elemento(codigo, detalle, stock_min, precio)
        self.elementos.append(elemento)

    def obtener_elementos(self):
        return self.elementos

    def eliminar_elemento(self, elemento):
        self.elementos.remove(elemento)

    def actualizar_elemento(self, elemento, nuevo_nombre, nueva_descripcion):
        elemento.nombre = nuevo_nombre
        elemento.descripcion = nueva_descripcion
