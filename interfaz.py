import tkinter as tk
from tkinter import ttk
from base_de_datos import BaseDeDatos

class InterfazLibros:
    def __init__(self, root):
        self.root = root
        self.root.title("Mantenimiento de Libros")
        self.root.geometry("400x400")

        # Etiquetas y campos de entrada
        self.codigo_label = ttk.Label(root, text="Código del Libro:")
        self.codigo_label.pack()
        self.codigo_entry = ttk.Entry(root)
        self.codigo_entry.pack()

        self.titulo_label = ttk.Label(root, text="Título:")
        self.titulo_label.pack()
        self.titulo_entry = ttk.Entry(root)
        self.titulo_entry.pack()

        self.year_label = ttk.Label(root, text="Año:")
        self.year_label.pack()
        self.year_entry = ttk.Entry(root)
        self.year_entry.pack()

        self.tomo_label = ttk.Label(root, text="Tomo:")
        self.tomo_label.pack()
        self.tomo_entry = ttk.Entry(root)
        self.tomo_entry.pack()

        # Botones para operaciones
        self.guardar_button = ttk.Button(root, text="Guardar Libro", command=self.guardar_libro)
        self.guardar_button.pack()

        self.eliminar_button = ttk.Button(root, text="Eliminar Libro", command=self.eliminar_libro)
        self.eliminar_button.pack()

        self.editar_button = ttk.Button(root, text="Editar Libro", command=self.editar_libro)
        self.editar_button.pack()

        self.obtener_button = ttk.Button(root, text="Obtener Libros", command=self.obtener_libros)
        self.obtener_button.pack()

        self.buscar_button = ttk.Button(root, text="Buscar Libro", command=self.buscar_libro)
        self.buscar_button.pack()

        # Inicializar status_label
        self.status_label = ttk.Label(root, text="")
        self.status_label.pack()

        # Instancia a base de datos
        self.bd = BaseDeDatos('base.xls')

    def limpiar_controles(self):
        self.codigo_entry.delete(0, tk.END)
        self.titulo_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.tomo_entry.delete(0, tk.END)

    def guardar_libro(self):
        codigo = self.codigo_entry.get()
        titulo = self.titulo_entry.get()
        year = self.year_entry.get()
        tomo = self.tomo_entry.get()

        self.bd.agregar_libro(codigo, titulo, year, tomo)

        self.limpiar_controles()
        self.status_label.config(text="Libro registrado exitosamente.")

    def eliminar_libro(self):
        codigo = self.codigo_entry.get()
        if self.bd.eliminar_libro(codigo):
            self.limpiar_controles()
            self.status_label.config(text="Libro eliminado correctamente.")
        else:
            self.limpiar_controles()
            self.status_label.config(text="Libro no encontrado.")

    def editar_libro(self):
        codigo = self.codigo_entry.get()
        titulo = self.titulo_entry.get()
        year = self.year_entry.get()
        tomo = self.tomo_entry.get()

        if self.bd.editar_libro(codigo, titulo, year, tomo):
            self.limpiar_controles()
            self.status_label.config(text="Libro editado correctamente.")
        else:
            self.limpiar_controles()
            self.status_label.config(text="Libro no encontrado.")

    def obtener_libros(self):
        libros = self.bd.obtener_libros()
        self.limpiar_controles()
        self.status_label.config(text="Listado de Libros:")
        for libro in libros:
            self.status_label.config(text=self.status_label.cget("text") + f"\nCódigo: {libro['codigo_libro']}, Título: {libro['titulo']}, Año: {libro['aho']}, Tomo: {libro['tomo']}")

    def buscar_libro(self):
        codigo = self.codigo_entry.get()
        libro = self.bd.buscar_libro(codigo)
        self.limpiar_controles()
        if libro:
            self.status_label.config(text=f"Código: {libro['codigo_libro']}, Título: {libro['titulo']}, Año: {libro['aho']}, Tomo: {libro['tomo']}")
        else:
            self.status_label.config(text="Libro no encontrado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazLibros(root)
    root.mainloop()


