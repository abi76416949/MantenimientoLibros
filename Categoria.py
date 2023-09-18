class Categoria():
    def __init__(self,cod_categoria, categoria):
        self.cod_categoria = cod_categoria
        self.categoria = categoria 
    
    def __str__(self):
        return f"{self.cod_categoria}, {self.categoria}"
    
    #-----------------AGREGAR GET Y SET------------------------------------
    def set_cod_categoria (self, cod_categoria):
        self.cod_categoria = cod_categoria
    def get_cod_categoria (self):
        return self.cod_categoria
    
    def set_categoria (self, categoria):
        self.categoria = categoria
    def get_categoria (self):
        return self.categoria