
#from autor import Autor
#from categoria import Categoria
#from base_de_datos import BaseDeDatos

class Libro():
    def __init__(self, codigo_libro, titulo, ano, tomo):
            self.codigo_libro = codigo_libro
            self.titulo= titulo
            self.aho = ano
            self.tomo= tomo
            self.autor = None
            self.categoria = None
    
    def __str__(self):
        return f"Código: {self.codigo_libro}, Título: {self.titulo}, Año: {self.ano}, Tomo: {self.tomo}"
    
    #---------------Agregar set y get-------------------------------------------
    def set_codigo_libro (self, codigo_libro):
        self.codigo_libro = codigo_libro
    def get_codigo_libro (self):
        return self.codigo_libro
    
    def set_titulo (self, titulo):
        self.titulo = titulo
    def get_titulo (self):
        return self.titulo
    
    def set_aho (self, aho):
        self.aho = aho
    def get_aho (self):
        return self.aho
    
    def set_tomo (self, tomo):
        self.tomo = tomo
    def get_tomo (self):
        return self.tomo

   #-----------------Asignar autor a libros-------------------------
    def asignar_autor(self, autor):
        self.autor = autor

    def asignar_categoria(self, categoria):
        self.asignar_categoria = categoria







""" #------------------AGREGAR_LIBRO--------------------------------------------
    def agregar_libro(self):
        self.codigo_libro=print("agrega el codi del libro")
        self.titulo=print("agrega el titulo del libro")
        self.aho=print("agrega el año del libro")
        self.tomo=print("agrega el tomo del libro")

       
        libros_a_guardar = [
            {'codigo_libro': self.codigo_libro, 'titulo': self.titulo, 'aho': self.aho, 'tomo': self.tomo}
        ]

        bd= BaseDeDatos('base.xls')
        bd.guardar_libros(libros_a_guardar) """

   


