# interfaz.py
import tkinter as tk
from tkinter import ttk
from Mantenimiento import Mantenimiento

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

        self.obtener_button = ttk.Button(root, text="Listar Libros", command=self.listar_libros)
        self.obtener_button.pack()

        self.buscar_button = ttk.Button(root, text="Buscar Libro", command=self.buscar_libro)
        self.buscar_button.pack()

        # Inicializar status_label
        self.status_label = ttk.Label(root, text="")
        self.status_label.pack()

        # Instancia a base de datos
        self.negocio_libro = Mantenimiento()

    def limpiar_controles(self):
        self.codigo_entry.delete(0, tk.END)
        self.titulo_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.tomo_entry.delete(0, tk.END)

    def guardar_libro(self):
        cod_libro = self.codigo_entry.get()
        titulo = self.titulo_entry.get()
        year = self.year_entry.get()
        tomo = self.tomo_entry.get()

        self.negocio_libro.agregar_libro(cod_libro, titulo, year, tomo)
        self.limpiar_controles()
        self.status_label.config(text="Libro registrado exitosamente.")

    def eliminar_libro(self):
        cod_libro = self.codigo_entry.get()
        if self.negocio_libro.eliminar_libro(cod_libro):
            self.limpiar_controles()
            self.status_label.config(text="Libro eliminado correctamente.")
        else:
            self.limpiar_controles()
            self.status_label.config(text="Libro no encontrado.")

    def editar_libro(self):
        codigo_libro = self.codigo_entry.get()
        nuevo_titulo = self.titulo_entry.get()
        nuevo_ano = self.year_entry.get()
        nuevo_tomo = self.tomo_entry.get()

        if self.negocio_libro.editar_libro(codigo_libro, nuevo_titulo, nuevo_ano, nuevo_tomo):
            self.limpiar_controles()
            self.status_label.config(text="Libro editado correctamente.")
        else:
            self.limpiar_controles()
            self.status_label.config(text="Libro no encontrado.")

    def listar_libros(self):
        listado_libros = self.negocio_libro.obtener_libros()
        self.limpiar_controles()
        self.status_label.config(text="Listado de Libros:")
        for libro in listado_libros:
            self.status_label.config(
                text=self.status_label.cget("text") + f"\nCódigo: {libro['codigo_libro']}, Título: {libro['titulo']}, Año: {libro['aho']}, Tomo: {libro['tomo']}")

    def buscar_libro(self):
        codigo_libro = self.codigo_entry.get()
        libro = self.negocio_libro.buscar_libro(codigo_libro)
        self.limpiar_controles()
        if libro:
            self.status_label.config(
                text=f"Código: {libro['codigo_libro']}, Título: {libro['titulo']}, Año: {libro['aho']}, Tomo: {libro['tomo']}")
        else:
            self.status_label.config(text="Libro no encontrado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazLibros(root)
    root.mainloop()


