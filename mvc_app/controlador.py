from modelo import Modelo
from vista import Vista
import tkinter as tk


class Controlador:
    def __init__(self, root):
        self.Modelo = Modelo()
        self.Vista = Vista(root)
        self.Vista.actualizar_treeview()


if __name__ == "__main__":
    root = tk.Tk()
    controlador = Controlador(root)
    root.mainloop()
