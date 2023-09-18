from libro import Libro
from base_de_datos import BaseDeDatos
import os 

class Mantenimiento():
    def __init__(self) -> None:
    
        self.bd = BaseDeDatos("Libros.xlsx") 
        self.contador_codLibros = "contadorcodLibros.txt"
        self.contador_codAutor = "contadorcodAutor.txt"
        self.contador_codCategoria = "contadorCategoria"
        self.libro_counter = self._cargar_contador(self.contador_codLibros)
        self.autor_counter = self._cargar_contador(self.contador_codAutor)
        self.categoria_counter = self._cargar_contador(self.contador_codCategoria)

    def _cargar_contador(self, contador_archivo):
        if os.path.exists(contador_archivo):
            with open(contador_archivo, "r") as archivo:
                return int(archivo.read())
        else:
            self.libro_counter = 1
        pass

    def _guardar_contador(self, contador_archivo, contador):
        with open(contador_archivo, "w") as archivo:
            archivo.write(str(contador))

    def generar_codigo_libro(self):
        #generamos un codigo de libro único asegurandonos que no se repita
        codigo_libro = f'L{self.libro_counter:001}'
        self.libro_counter += 1
        self._guardar_contador(self.contador_codLibros, self.libro_counter)  # Guardar el valor actual del contador en el 
        print(f"Su codig de libro es: {codigo_libro} ")
        return codigo_libro 


    def agregarLibros(self, titulo, ano, tomo):
       
       codigo_libro = self.generar_codigo_libro()
       lb = Libro(codigo_libro,titulo,ano, tomo)
       
       self.bd=BaseDeDatos("Libros.xlsx")
       self.bd.agregar_libro(lb)


    def eliminar_libro(self, codigo_libro):
        
        self.bd.eliminar_libro(codigo_libro)
       
    #def agregarAutores():
       
ma = Mantenimiento()
ma.generar_codigo_libro()