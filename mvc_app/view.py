import tkinter as tk
from tkinter import ttk
from model import Modelo


class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Productos")
        self.root.configure(bg="#064C71")

        # Título
        titulo = tk.Label(
            root,
            text="CRUD Productos",
            bg="#91D8F7",
            fg="black",
            font=("Arial", 14, "bold"),
        )
        titulo.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky=tk.W + tk.E)

        # Labels
        labels = ["Código", "Detalle", "Stock Minimo", "Precio Unitario"]
        self.entry_vars = [tk.StringVar() for _ in range(4)]

        for i, label_text in enumerate(labels):
            label = tk.Label(root, text=label_text, font=("None", 11))
            label.grid(row=i + 1, column=0, sticky=tk.W)
            entry = tk.Entry(root, textvariable=self.entry_vars[i], width=25)
            entry.grid(row=i + 1, column=1)

        # Treeview
        self.tree = ttk.Treeview(root)
        self.tree["columns"] = ("col1", "col2", "col3")
        self.tree.column("#0", width=50, minwidth=10, anchor=tk.W)
        self.tree.column("col1", width=200, minwidth=30, anchor=tk.W)
        self.tree.column("col2", width=100, minwidth=50, anchor=tk.W)
        self.tree.column("col3", width=90, minwidth=40, anchor=tk.W)
        self.tree.heading("#0", text="Código")
        self.tree.heading("col1", text="Detalle")
        self.tree.heading("col2", text="Stock Mínimo")
        self.tree.heading("col3", text="Precio")
        self.tree.grid(column=0, row=7, columnspan=3, padx=10, pady=10)

        # Botones
        cargar_btn = tk.Button(
            root,
            text="Cargar Producto",
            command=self.cargar_producto,
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5,
        )
        cargar_btn.grid(row=5, column=1, pady=5)

        eliminar_btn = tk.Button(
            root,
            text="Eliminar",
            command=self.eliminar_producto,
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5,
        )
        eliminar_btn.grid(row=8, column=1, pady=10)

    def cargar_producto(self):
        codigo = self.entry_vars[0].get()
        descripcion = self.entry_vars[1].get()
        stock_m = self.entry_vars[2].get()
        precio = self.entry_vars[3].get()
        Modelo.cargar_producto(codigo, descripcion, stock_m, precio)
        self.actualizar_treeview()

    def eliminar_producto(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return
        codigo = self.tree.item(selected_item, "text")
        Modelo.eliminar_producto(codigo)
        self.actualizar_treeview()

    def actualizar_treeview(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

            productos = self.model.obtener_productos()
        for producto in productos:
            self.tree.insert(
                "", 0, text=producto[0], values=(producto[1], producto[2], producto[3])
            )
