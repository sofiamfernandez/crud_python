class Elemento:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion


class ListaElementos:
    def __init__(self):
        self.elementos = []

    def agregar_elemento(self, nombre, descripcion):
        elemento = Elemento(nombre, descripcion)
        self.elementos.append(elemento)

    def obtener_elementos(self):
        return self.elementos

    def eliminar_elemento(self, elemento):
        self.elementos.remove(elemento)

    def actualizar_elemento(self, elemento, nuevo_nombre, nueva_descripcion):
        elemento.nombre = nuevo_nombre
        elemento.descripcion = nueva_descripcion
