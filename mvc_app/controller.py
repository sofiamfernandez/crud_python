from model import Modelo
from view import Vista
import tkinter as tk


class Controlador:
    def __init__(self, root):
        self.model = Modelo()
        self.view = Vista(root)
        self.view.actualizar_treeview()


if __name__ == "__main__":
    root = tk.Tk()
    controller = Controlador(root)
    root.mainloop()
