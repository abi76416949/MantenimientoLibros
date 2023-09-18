import tkinter as tk
from tkinter import ttk
from Mantenimiento import Mantenimiento

class InterfazLibros:
    def __init__(self, root):
        self.root = root
        self.root.title("Mantenimiento de Libros")
        self.root.geometry("400x400")

        self.negocio_libro = Mantenimiento()

        self.create_widgets()

    def create_widgets(self):
        self.codigo_label = ttk.Label(self.root, text="Código del Libro:")
        self.codigo_label.pack()
        self.codigo_entry = ttk.Entry(self.root)
        self.codigo_entry.pack()

        self.titulo_label = ttk.Label(self.root, text="Título:")
        self.titulo_label.pack()
        self.titulo_entry = ttk.Entry(self.root)
        self.titulo_entry.pack()

        self.year_label = ttk.Label(self.root, text="Año:")
        self.year_label.pack()
        self.year_entry = ttk.Entry(self.root)
        self.year_entry.pack()

        self.tomo_label = ttk.Label(self.root, text="Tomo:")
        self.tomo_label.pack()
        self.tomo_entry = ttk.Entry(self.root)
        self.tomo_entry.pack()

        self.guardar_button = ttk.Button(self.root, text="Guardar Libro", command=self.guardar_libro)
        self.guardar_button.pack()

        self.eliminar_button = ttk.Button(self.root, text="Eliminar Libro", command=self.eliminar_libro)
        self.eliminar_button.pack()

        self.editar_button = ttk.Button(self.root, text="Editar Libro", command=self.editar_libro)
        self.editar_button.pack()

        self.obtener_button = ttk.Button(self.root, text="Listar Libros", command=self.listar_libros)
        self.obtener_button.pack()

        self.buscar_button = ttk.Button(self.root, text="Buscar Libro", command=self.buscar_libro)
        self.buscar_button.pack()

        self.limpiar_button = ttk.Button(self.root, text="Limpiar Campos", command=self.limpiar_controles)
        self.limpiar_button.pack()

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
        self.mostrar_mensaje("Libro registrado exitosamente.")

    def eliminar_libro(self):
        cod_libro = self.codigo_entry.get()
        if self.negocio_libro.eliminar_libro(cod_libro):
            self.limpiar_controles()
            self.mostrar_mensaje("Libro eliminado correctamente.")
        else:
            self.mostrar_mensaje("Libro no encontrado.")

    def editar_libro(self):
        codigo_libro = self.codigo_entry.get()
        nuevo_titulo = self.titulo_entry.get()
        nuevo_ano = self.year_entry.get()
        nuevo_tomo = self.tomo_entry.get()

        if self.negocio_libro.editar_libro(codigo_libro, nuevo_titulo, nuevo_ano, nuevo_tomo):
            self.limpiar_controles()
            self.mostrar_mensaje("Libro editado correctamente.")
        else:
            self.mostrar_mensaje("Libro no encontrado.")

    def listar_libros(self):
        listado_libros = self.negocio_libro.obtener_libros()
        self.limpiar_controles()
        mensaje = "Listado de Libros:\n"
        for libro in listado_libros:
            mensaje += f'Código: {libro["codigo_libro"]}, Título: {libro["titulo"]}, Año: {libro["aho"]}, Tomo: {libro["tomo"]}\n'
        self.mostrar_mensaje(mensaje)

    def buscar_libro(self):
        codigo_libro = self.codigo_entry.get()
        libro = self.negocio_libro.buscar_libro(codigo_libro)
        self.limpiar_controles()
        if libro:
            mensaje = f'Código: {libro["codigo_libro"]}, Título: {libro["titulo"]}, Año: {libro["aho"]}, Tomo: {libro["tomo"]}'
            self.mostrar_mensaje(mensaje)
        else:
            self.mostrar_mensaje("Libro no encontrado.")


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazLibros(root)
    root.mainloop()


