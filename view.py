import tkinter as tk
from tkinter import ttk


class Vista:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Control de Productos")
        self.configure(bg="#064C71")

        self.frame = ttk.Frame(self.root)
        self.frame.grid(row=0, column=0, padx=20, pady=20)

        self.nombre_label = ttk.Label(self.frame, text="Código:")
        self.nombre_label.grid(row=0, column=0, padx=0, pady=5)
        self.nombre_entry = ttk.Entry(self.frame)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5)

        self.descripcion_label = ttk.Label(self.frame, text="Detalle:")
        self.descripcion_label.grid(row=1, column=0, padx=5, pady=5)
        self.nombre_entry = ttk.Entry(self.frame)
        self.nombre_entry.grid(row=1, column=1, padx=5, pady=5)

        self.descripcion_label = ttk.Label(self.frame, text="Stock Mínimo:")
        self.descripcion_label.grid(row=2, column=0, padx=5, pady=5)
        self.nombre_entry = ttk.Entry(self.frame)
        self.nombre_entry.grid(row=2, column=1, padx=5, pady=5)

        self.descripcion_label = ttk.Label(self.frame, text="Precio Unitario:")
        self.descripcion_label.grid(row=3, column=0, padx=5, pady=5)
        self.nombre_entry = ttk.Entry(self.frame)
        self.nombre_entry.grid(row=3, column=1, padx=5, pady=5)

        self.descripcion_entry = ttk.Entry(self.frame)
        self.descripcion_entry.grid(row=1, column=1, padx=5, pady=5)

        self.agregar_button = ttk.Button(self.frame, text="Cargar Producto")
        self.agregar_button.grid(row=4, column=1, padx=5, pady=5)

        self.elementos_listbox = tk.Listbox(self.frame)
        self.elementos_listbox.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.actualizar_button = ttk.Button(self.frame, text="Modificar")
        self.actualizar_button.grid(row=4, column=2, padx=5, pady=5)

        self.eliminar_button = ttk.Button(self.frame, text="Eliminar")
        self.eliminar_button.grid(row=6, column=1, padx=5, pady=5)

    def iniciar_aplicacion(self):
        self.root.mainloop()
