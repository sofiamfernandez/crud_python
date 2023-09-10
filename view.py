import tkinter as tk
from tkinter import E, W, ttk, Label


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

        # Definición y estilo del frame

        self.frame = ttk.Frame(self.root, style="color.TFrame")
        self.root.title("Control de Productos")
        style = ttk.Style()
        style.configure("color.TFrame", background="#064C71")
        self.frame = ttk.Frame(self.root, style="color.TFrame")
        self.frame.grid(row=1, column=0, padx=40, pady=40)

        self.codigo_label = ttk.Label(self.frame, text="Código:", font=("Arial", 11))
        self.codigo_label.grid(row=0, column=0, padx=0, pady=5)
        self.codigo_entry = ttk.Entry(self.frame)
        self.codigo_entry.grid(row=0, column=1, padx=5, pady=5)

        self.detalle_label = ttk.Label(self.frame, text="Detalle:", font=("Arial", 11))
        self.detalle_label.grid(row=1, column=0, padx=5, pady=5)
        self.detalle_entry = ttk.Entry(self.frame)
        self.detalle_entry.grid(row=1, column=1, padx=5, pady=5)

        self.stock_min_label = ttk.Label(
            self.frame, text="Stock Mínimo:", font=("Arial", 11)
        )
        self.stock_min_label.grid(row=2, column=0, padx=5, pady=5)
        self.stock_min_entry = ttk.Entry(self.frame)
        self.stock_min_entry.grid(row=2, column=1, padx=5, pady=5)

        self.preciou_label = ttk.Label(
            self.frame, text="Precio Unitario:", font=("Arial", 11)
        )
        self.preciou_label.grid(row=3, column=0, padx=5, pady=5)
        self.preciou_entry = ttk.Entry(self.frame)
        self.preciou_entry.grid(row=3, column=1, padx=5, pady=5)

        self.descripcion_entry = ttk.Entry(self.frame)
        self.descripcion_entry.grid(row=1, column=1, padx=5, pady=5)

        self.agregar_button = ttk.Button(self.frame, text="Cargar Producto")
        self.agregar_button.grid(row=4, column=0, padx=5, pady=5)

        self.elementos_treeview = ttk.Treeview(
            self.frame, columns=("Código", "Detalle", "Stock Mínimo", "Precio Unitario")
        )
        self.elementos_treeview.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        # Configuracion de las columnas del Treeview
        self.elementos_treeview.column("#0", width=50, minwidth=10, anchor=W)
        self.elementos_treeview.column("#1", width=200, minwidth=30, anchor=W)
        self.elementos_treeview.column("#2", width=100, minwidth=50, anchor=W)
        self.elementos_treeview.column("#3", width=90, minwidth=40, anchor=W)

        self.elementos_treeview.heading("#0", text="Código")
        self.elementos_treeview.heading("#1", text="Detalle")
        self.elementos_treeview.heading("#2", text="Stock Mínimo")
        self.elementos_treeview.heading("#3", text="Precio Unitario")

        self.actualizar_button = ttk.Button(self.frame, text="Modificar")
        self.actualizar_button.grid(row=4, column=1, padx=5, pady=5)

        self.eliminar_button = ttk.Button(self.frame, text="Eliminar")
        self.eliminar_button.grid(row=6, column=1, padx=5, pady=5)

    def iniciar_aplicacion(self):
        self.root.mainloop()
