import pandas as pd
from Autor import Autor

class AutorNegocio(Autor):
    listado_Autor = []
    registros_docentes = 'C:/Users/Elia/Desktop/PROGRAMACION/Python/CICLO 3/Herencia/listado_alumno/listado_docente.xlsx'

    def __init__(self):
        self.listado_docentes = []

    def obtener_autor(self):
        df = pd.read_excel(self.registros_docentes)
        listado_docentes = []
        for index, row in df.iterrows():
            docente = Autor(row['Nombre'], row['Apellido_Paterno'], row['Apellido_Materno'], row['DNI'], row['Codigo'], row['Facultad'])
            listado_docentes.append(docente)
        return listado_docentes

    def registrar_docente(self, nombre, ap_paterno, ap_materno, dni, codigo, facultad):
        self.listado_docentes = self.obtener_docentes()
        docente = Autor(nombre, ap_paterno, ap_materno, dni, codigo, facultad)
        self.listado_docentes.append(docente)
        print(f'Se agregó un docente: {len(self.listado_docentes)}')

    def guardar_docentes(self):
        if len(self.listado_docentes) > 0:
            data = []
            for docente in self.listado_docentes:
                data.append([docente.nombre, docente.ap_paterno, docente.ap_materno, docente.dni, docente.codigo_docente, docente.facultad])
            columnas = ['Nombre', 'Apellido_Paterno', 'Apellido_Materno', 'DNI', 'Codigo', 'Facultad']
            df = pd.DataFrame(data, columns=columnas)
            df.to_excel(self.registros_docentes, index=False, engine='openpyxl')
            return f'Se registraron correctamente los datos del docente'
        else:
            return f'Se generó un error al registrar al docente'

    def editar_docente(self, indice, nombre, ap_paterno, ap_materno, dni, codigo, facultad):
        df = pd.read_excel(self.registros_docentes)
        df.loc[indice, 'Nombre'] = nombre
        df.loc[indice, 'Apellido_Paterno'] = ap_paterno
        df.loc[indice, 'Apellido_Materno'] = ap_materno
        df.loc[indice, 'DNI'] = dni
        df.loc[indice, 'Codigo'] = codigo
        df.loc[indice, 'Facultad'] = facultad
        df.to_excel(self.registros_docentes, index=False, engine='openpyxl')
        return f'Actualización correcta'