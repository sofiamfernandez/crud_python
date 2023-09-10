import tkinter as tk
from tkinter import ttk


class Vista:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Aplicación CRUD")

        self.frame = ttk.Frame(self.root)
        self.frame.grid(row=0, column=0, padx=10, pady=10)

        self.nombre_label = ttk.Label(self.frame, text="Nombre:")
        self.nombre_label.grid(row=0, column=0, padx=5, pady=5)

        self.nombre_entry = ttk.Entry(self.frame)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5)

        self.descripcion_label = ttk.Label(self.frame, text="Descripción:")
        self.descripcion_label.grid(row=1, column=0, padx=5, pady=5)

        self.descripcion_entry = ttk.Entry(self.frame)
        self.descripcion_entry.grid(row=1, column=1, padx=5, pady=5)

        self.agregar_button = ttk.Button(self.frame, text="Agregar")
        self.agregar_button.grid(row=2, column=0, padx=5, pady=5)

        self.elementos_listbox = tk.Listbox(self.frame)
        self.elementos_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.actualizar_button = ttk.Button(self.frame, text="Actualizar")
        self.actualizar_button.grid(row=4, column=0, padx=5, pady=5)

        self.eliminar_button = ttk.Button(self.frame, text="Eliminar")
        self.eliminar_button.grid(row=4, column=1, padx=5, pady=5)

    def iniciar_aplicacion(self):
        self.root.mainloop()
