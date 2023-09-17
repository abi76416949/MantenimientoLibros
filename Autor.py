from Persona import Persona

class Autor(Persona):
    cod_autor = ''
    pais = ''
    editorial = ''
    
    #Definimos el constructor
    def __init__(self, nombre, ap_paterno, ap_materno, codigo, pais, editorial):
        super().__init__(nombre, ap_paterno, ap_materno)
        self.cod_autor = codigo
        self.pais = pais
        self.editorial = editorial

    def get_codigo(self):
        return self.cod_autor

    def set_codigo(self, codigo):
        self.cod_autor = codigo

    def get_pais(self):
        return self.pais

    def set_pais(self, pais):
        self.pais = pais

    def get_editorial(self):
        return self.editorial

    def set_editorial(self, editorial):
        self.editorial = editorial

    def imprimir(self):
        per_data = super().imprimir()
        codigo = self.cod_autor
        pais = self.pais
        editorial = self.editorial
        return f'Datos del autor es : {per_data}, Codigo de ingreso: {codigo}, Pais: {pais}, Editorial: {editorial}'