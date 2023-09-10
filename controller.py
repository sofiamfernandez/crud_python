from model import ListaElementos
from view import Vista
import tkinter as tk


class Controlador:
    def __init__(self):
        self.lista_elementos = ListaElementos()
        self.vista = Vista()

        # Conectar eventos a funciones
        self.vista.agregar_button.config(command=self.agregar_elemento)
        self.vista.actualizar_button.config(command=self.actualizar_elemento)
        self.vista.eliminar_button.config(command=self.eliminar_elemento)
        self.vista.elementos_listbox.bind(
            "<<ListboxSelect>>", self.mostrar_elemento_seleccionado
        )

        self.actualizar_lista_elementos()
        self.vista.iniciar_aplicacion()

    def agregar_elemento(self):
        nombre = self.vista.nombre_entry.get()
        descripcion = self.vista.descripcion_entry.get()
        self.lista_elementos.agregar_elemento(nombre, descripcion)
        self.actualizar_lista_elementos()

    def actualizar_elemento(self):
        elemento_seleccionado = self.vista.elementos_listbox.get(tk.ACTIVE)
        nuevo_nombre = self.vista.nombre_entry.get()
        nueva_descripcion = self.vista.descripcion_entry.get()

        if elemento_seleccionado:
            elemento = self.obtener_elemento_por_nombre(elemento_seleccionado)
            self.lista_elementos.actualizar_elemento(
                elemento, nuevo_nombre, nueva_descripcion
            )
            self.actualizar_lista_elementos()

    def eliminar_elemento(self):
        elemento_seleccionado = self.vista.elementos_listbox.get(tk.ACTIVE)
        if elemento_seleccionado:
            elemento = self.obtener_elemento_por_nombre(elemento_seleccionado)
            self.lista_elementos.eliminar_elemento(elemento)
            self.actualizar_lista_elementos()

    def mostrar_elemento_seleccionado(self, event):
        elemento_seleccionado = self.vista.elementos_listbox.get(tk.ACTIVE)
        if elemento_seleccionado:
            elemento = self.obtener_elemento_por_nombre(elemento_seleccionado)
            self.vista.nombre_entry.delete(0, tk.END)
            self.vista.nombre_entry.insert(0, elemento.nombre)
            self.vista.descripcion_entry.delete(0, tk.END)
            self.vista.descripcion_entry.insert(0, elemento.descripcion)

    def obtener_elemento_por_nombre(self, nombre):
        for elemento in self.lista_elementos.obtener_elementos():
            if elemento.nombre == nombre:
                return elemento

    def actualizar_lista_elementos(self):
        self.vista.elementos_listbox.delete(0, tk.END)
        for elemento in self.lista_elementos.obtener_elementos():
            self.vista.elementos_listbox.insert(tk.END, elemento.nombre)


if __name__ == "__main__":
    app = Controlador()
