import modelo
import vista
import tkinter as tk


class Controlador:
    def __init__(self, root):
        self.modelo = modelo()
        self.vista = vista(root)
        self.vista.actualizar_treeview()


if __name__ == "__main__":
    root = tk.Tk()
    controlador = Controlador(root)
    root.mainloop()
