import tkinter as tk
from tkinter import N, S, E, W, ttk, Label


class Vista:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Control de Productos")
        self.root.configure(bg="#064C71")

        titulo = Label(
            self.root,
            text="CRUD Productos",
            bg="#91D8F7",
            fg="black",
            font=("Arial", 14, "bold"),
        )
        titulo.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky=W + E)

        self.frame = ttk.Frame(self.root)
        self.frame.grid(row=1, column=0, padx=20, pady=20)

        self.codigo_label = ttk.Label(self.frame, text="Código:")
        self.codigo_label.grid(row=0, column=0, padx=0, pady=5)
        self.codigo_entry = ttk.Entry(self.frame)
        self.codigo_entry.grid(row=0, column=1, padx=5, pady=5)

        self.detalle_label = ttk.Label(self.frame, text="Detalle:")
        self.detalle_label.grid(row=1, column=0, padx=5, pady=5)
        self.detalle_entry = ttk.Entry(self.frame)
        self.detalle_entry.grid(row=1, column=1, padx=5, pady=5)

        self.stock_min_label = ttk.Label(self.frame, text="Stock Mínimo:")
        self.stock_min_label.grid(row=2, column=0, padx=5, pady=5)
        self.stock_min_entry = ttk.Entry(self.frame)
        self.stock_min_entry.grid(row=2, column=1, padx=5, pady=5)

        self.preciou_label = ttk.Label(self.frame, text="Precio Unitario:")
        self.preciou_label.grid(row=3, column=0, padx=5, pady=5)
        self.preciou_entry = ttk.Entry(self.frame)
        self.preciou_entry.grid(row=3, column=1, padx=5, pady=5)

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
