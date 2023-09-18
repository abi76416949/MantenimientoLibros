class Persona():
    def __init__(self,cod_persona,nombre, apellidoPaterno,apellidoMaterno, fecha_nacimieto):
        self.cod_persona = cod_persona
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.fecha_nacimieto = fecha_nacimieto
    
    def __str__(self) -> str:
        return f"{self.cod_persona}, {self.nombre}, {self.apellidoPaterno} ,{self.apellidoMaterno} ,{self.fecha_nacimieto}"

    #-------------IMPLEMENTACION DE GET Y SET-------------------

    def get_cod_persona(self):
        return self.cod_persona
    def set_cod_persona(self, cod_persona):
        self.cod_persona = cod_persona

    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_apellidoPaterno(self):
        return self.apellidoPaterno
    def set_apellidoPaterno(self,apellidoPaterno):
        self.apellidoPaterno = apellidoPaterno

    def get_apellidoMaterno(self):
        return self.apellidoMaterno
    def set_apellidoMaterno(self,apellidoMaterno):
        self.apellidoMaterno = apellidoMaterno
        
    def get_fecha_nacimieto(self):
        return self.fecha_nacimieto