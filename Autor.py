from persona import Persona
class Autor(Persona):
    def __init__(self, cod_persona, nombre, apellidoPaterno, apellidoMaterno, fecha_nacimieto,cod_autor,pais,editorial):
        super().__init__(cod_persona, nombre, apellidoPaterno, apellidoMaterno, fecha_nacimieto)
        self.cod_autor = cod_autor
        self.pais = pais
        self.editorial = editorial
    def __str__(self):
        return f"{super().__str__()}, {self.cod_autor}, {self.pais}, {self.editorial}"
#----------------IMPLEMENTACION DE GET Y SETTER--------------------------

    def set_cod_autor (self, cod_autor):
        self.cod_autor = cod_autor
    def get_cod_autor (self):
        return self.cod_autor
    
    def set_pais (self, pais):
        self.pais = pais
    def get_pais (self):
        return self.pais
    
    def set_editorial (self, editorial):
        self.editorial = editorial