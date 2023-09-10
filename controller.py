from model import ListaElementos, BaseDatos
from view import Vista
import tkinter as tk


class Controlador:
    def __init__(self):
        self.base_datos = BaseDatos()
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
        codigo = self.vista.codigo_entry.get()
        detalle = self.vista.codigo_entry.get()
        stock_min = self.vista.stock_min_entry.get()
        preciou = self.vista.preciou_entry
        self.lista_elementos.agregar_elemento(codigo, detalle, stock_min, preciou)
        self.actualizar_lista_elementos()

    def actualizar_elemento(self):
        elemento_seleccionado = self.vista.elementos_listbox.get(tk.ACTIVE)
        nuevo_detalle = self.vista.detalle_entry.get()
        nueva_descripcion = self.vista.descripcion_entry.get()

        if elemento_seleccionado:
            elemento = self.obtener_elemento_por_detalle(elemento_seleccionado)
            self.lista_elementos.actualizar_elemento(
                elemento, nuevo_detalle, nueva_descripcion
            )
            self.actualizar_lista_elementos()

    def eliminar_elemento(self):
        elemento_seleccionado = self.vista.elementos_listbox.get(tk.ACTIVE)
        if elemento_seleccionado:
            elemento = self.obtener_elemento_por_detalle(elemento_seleccionado)
            self.lista_elementos.eliminar_elemento(elemento)
            self.actualizar_lista_elementos()

    def mostrar_elemento_seleccionado(self, event):
        elemento_seleccionado = self.vista.elementos_listbox.get(tk.ACTIVE)
        if elemento_seleccionado:
            elemento = self.obtener_elemento_por_detalle(elemento_seleccionado)
            self.vista.detalle_entry.delete(0, tk.END)
            self.vista.detalle_entry.insert(0, elemento.detalle)
            self.vista.descripcion_entry.delete(0, tk.END)

    def obtener_elemento_por_detalle(self, detalle):
        for elemento in self.lista_elementos.obtener_elementos():
            if elemento.detalle == detalle:
                return elemento

    def actualizar_lista_elementos(self):
        self.vista.elementos_listbox.delete(0, tk.END)
        for elemento in self.lista_elementos.obtener_elementos():
            self.vista.elementos_listbox.insert(tk.END, elemento.detalle)


if __name__ == "__main__":
    app = Controlador()
