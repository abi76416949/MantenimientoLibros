import random
import string
from Libro import Libro

class Categoria():
    cod_categoria = ''
    categoria = ''

    def __init__(self, cod_categoria, categoria):
        self.cod_categoria = cod_categoria
        self.categoria = categoria

    def set_cod_categoria(self, cod_categoria):
        self.cod_categoria = cod_categoria

    def get_cod_categoria(self):
        return self.cod_categoria
    
    def generar_codigo_categoria(self, length=3):
        # Genera un código aleatorio de números
        characters = string.digits
        codigo_categoria = ''.join(random.choice(characters) for _ in range(length))
        self.cod_categoria = codigo_categoria
    
    def asignar_libro(self, libro):
        self.libro = libro
    
    def mostrar_libro(self):
        return self.libro
    
    def reporte(self):
        return f"Reporte del libro: {self.libro}\nCodigo de la categoria: {self.cod_categoria}\nCategoria: {self.categoria}"