import tkinter as tk
from tkinter import ttk
from base_de_datos import BaseDeDatos

class InterfazLibros:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Libros")
        self.root.geometry("400x350")

        # Instancia a base de datos
        self.bd = BaseDeDatos('base.xls')

        # Menú de opciones
        self.accion_label = ttk.Label(root, text="Selecciona una acción:")
        self.accion_label.pack()

        self.acciones = ["Registrar", "Buscar", "Editar", "Eliminar", "Salir"]
        self.accion_combobox = ttk.Combobox(root, values=self.acciones)
        self.accion_combobox.pack()
        self.accion_combobox.bind("<<ComboboxSelected>>", self.seleccionar_accion)

        # Crear frames para organizar widgets
        self.registrar_frame = ttk.Frame(root)
        self.buscar_frame = ttk.Frame(root)
        self.editar_frame = ttk.Frame(root)
        self.eliminar_frame = ttk.Frame(root)

        # Llamar a los métodos para configurar los frames
        self.configurar_registrar_frame()
        self.configurar_buscar_frame()
        self.configurar_editar_frame()
        self.configurar_eliminar_frame()

        # Inicializar status_label
        self.status_label = ttk.Label(root, text="")
        self.status_label.pack()

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

        self.bd.guardar_libros([{'codigo_libro': codigo, 'titulo': titulo, 'aho': year, 'tomo': tomo}])

        self.limpiar_controles()
        self.status_label.config(text="Libro registrado exitosamente.")

    def buscar_libro(self):
        codigo = self.codigo_entry.get()
        libros = self.bd.obtener_libros()
        for libro in libros:
            if libro['codigo_libro'] == codigo:
                self.titulo_entry.delete(0, tk.END)
                self.titulo_entry.insert(0, libro['titulo'])
                self.year_entry.delete(0, tk.END)
                self.year_entry.insert(0, libro['aho'])
                self.tomo_entry.delete(0, tk.END)
                self.tomo_entry.insert(0, libro['tomo'])
                self.status_label.config(text="Libro encontrado.")
                return
        self.limpiar_controles()
        self.status_label.config(text="Libro no encontrado.")

    def editar_libro(self):
        codigo = self.codigo_entry.get()
        nuevo_titulo = self.titulo_entry.get()
        nuevo_ano = self.year_entry.get()
        nuevo_tomo = self.tomo_entry.get()

        if self.bd.editar_libro(codigo, nuevo_titulo, nuevo_ano, nuevo_tomo):
            self.limpiar_controles()
            self.status_label.config(text="Libro editado correctamente.")
        else:
            self.limpiar_controles()
            self.status_label.config(text="Libro no encontrado.")

    def eliminar_libro(self):
        codigo = self.codigo_entry.get()
        if self.bd.eliminar_libro(codigo):
            self.limpiar_controles()
            self.status_label.config(text="Libro eliminado correctamente.")
        else:
            self.limpiar_controles()
            self.status_label.config(text="Libro no encontrado.")

    def seleccionar_accion(self, event):
        accion = self.accion_combobox.get()

        # Ocultar todos los frames
        self.registrar_frame.pack_forget()
        self.buscar_frame.pack_forget()
        self.editar_frame.pack_forget()
        self.eliminar_frame.pack_forget()

        if accion == "Registrar":
            self.registrar_frame.pack()
        elif accion == "Buscar":
            self.buscar_frame.pack()
        elif accion == "Editar":
            self.editar_frame.pack()
        elif accion == "Eliminar":
            self.eliminar_frame.pack()
        elif accion == "Salir":
            self.root.quit()

    def configurar_registrar_frame(self):
        self.registrar_frame.pack()
        codigo_label = ttk.Label(self.registrar_frame, text="Código del libro:")
        codigo_label.pack()
        self.codigo_entry = ttk.Entry(self.registrar_frame)
        self.codigo_entry.pack()

        titulo_label = ttk.Label(self.registrar_frame, text="Título:")
        titulo_label.pack()
        self.titulo_entry = ttk.Entry(self.registrar_frame)
        self.titulo_entry.pack()

        year_label = ttk.Label(self.registrar_frame, text="Año:")
        year_label.pack()
        self.year_entry = ttk.Entry(self.registrar_frame)
        self.year_entry.pack()

        tomo_label = ttk.Label(self.registrar_frame, text="Tomo:")
        tomo_label.pack()
        self.tomo_entry = ttk.Entry(self.registrar_frame)
        self.tomo_entry.pack()

        guardar_button = ttk.Button(self.registrar_frame, text="Guardar", command=self.guardar_libro)
        guardar_button.pack()

    def configurar_buscar_frame(self):
        self.buscar_frame.pack()
        codigo_label = ttk.Label(self.buscar_frame, text="Código del libro a buscar:")
        codigo_label.pack()
        self.codigo_entry = ttk.Entry(self.buscar_frame)
        self.codigo_entry.pack()

        buscar_button = ttk.Button(self.buscar_frame, text="Buscar", command=self.buscar_libro)
        buscar_button.pack()

    def configurar_editar_frame(self):
        self.editar_frame.pack()
        codigo_label = ttk.Label(self.editar_frame, text="Código del libro a editar:")
        codigo_label.pack()
        self.codigo_entry = ttk.Entry(self.editar_frame)
        self.codigo_entry.pack()

        titulo_label = ttk.Label(self.editar_frame, text="Nuevo Título:")
        titulo_label.pack()
        self.titulo_entry = ttk.Entry(self.editar_frame)
        self.titulo_entry.pack()

        year_label = ttk.Label(self.editar_frame, text="Nuevo Año:")
        year_label.pack()
        self.year_entry = ttk.Entry(self.editar_frame)
        self.year_entry.pack()

        tomo_label = ttk.Label(self.editar_frame, text="Nuevo Tomo:")
        tomo_label.pack()
        self.tomo_entry = ttk.Entry(self.editar_frame)
        self.tomo_entry.pack()

        editar_button = ttk.Button(self.editar_frame, text="Editar", command=self.editar_libro)
        editar_button.pack()

    def configurar_eliminar_frame(self):
        self.eliminar_frame.pack()
        codigo_label = ttk.Label(self.eliminar_frame, text="Código del libro a eliminar:")
        codigo_label.pack()
        self.codigo_entry = ttk.Entry(self.eliminar_frame)
        self.codigo_entry.pack()

        eliminar_button = ttk.Button(self.eliminar_frame, text="Eliminar", command=self.eliminar_libro)
        eliminar_button.pack()

        # Botón "Salir" en el frame de eliminación
        salir_button = ttk.Button(self.eliminar_frame, text="Salir", command=self.root.quit)
        salir_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazLibros(root)
    root.mainloop()

