import openpyxl
from openpyxl import Workbook
from libro import Libro
from openpyxl.worksheet.worksheet import Worksheet

from categoria import Categoria
from autor import Autor


class BaseDeDatos:
    def __init__(self, archivo):
        self.archivo = archivo
    
    def _abrir_archivo():
        
        libro = openpyxl.Workbook()
        hoja = libro.active
        hoja.append(["Código Libro", "Título", "Año", "Tomo", "Código Autor", "Nombre Autor", "País", "Editorial", "codigo_categoria", "categoria"])




    def agregar_libro(self, libro):
        libroExcel = self._abrir_archivo()

        if libroExcel is None:
            libroExcel = Workbook()
            hoja = libroExcel.active
            hoja.append(["Código Libro", "Título", "Año", "Tomo", "Código Autor", "Nombre Autor", "País", "Editorial", "codigo_categoria", "categoria"])
        else:
            hoja = libroExcel.active

        # Agregar los datos del libro
        hoja.append([libro.codigo_libro, libro.titulo, libro.aho, libro.tomo, "", "", "", "", "", ""])
        
        libroExcel.save(self.archivo)
        libroExcel.close()



    def eliminar_libro(self, codigo_libro):
        libroExcel = self._abrir_archivo()
        if libroExcel is not None:
            hoja = libroExcel.active
            for row in hoja.iter_rows(min_row=2, values_only=True):
                if row[0] == codigo_libro:
                    hoja.delete_rows(row[0])
                    libroExcel.save(self.archivo)
                    libroExcel.close()
                    return True
        libroExcel.close()
        return False
    





















    #---------------------ABRIR LIBROS--------------------------------
    def _abrir_archivo(self):
        try:
            libro = openpyxl.load_workbook(self.archivo)
            return libro
        except FileNotFoundError:
            return None
        




    #---------------------------OBTENER_LIBROS------------------------------------
    def obtener_libros(self):

        libro, hoja = self._abrir_archivo()
        
        if hoja is None:
            return []

        datos = []
        for row in hoja.iter_row(values_only=True):
            if row[0] != 'codigo_libro ':
                datos.append(
                    {'codigo_libro': row[0], 'titulo': row[1], 'aho': row[2], 'tomo': row[3]})
        libro.close()
        return datos
    #------------------------GUARDAR_lIBROS--------------------------------------
    def guardar_libros(self, libros):
        libro = openpyxl.load_workbook(self.archivo)
        hoja = libro.active

        # Asegúrate de que los encabezados estén en la primera fila
        if hoja.cell(row=1, column=1).value is None:
            hoja.append(['codigo_libro', 'titulo', 'ano', 'tomo', 'codigo_autor', 'nombre_autor', 'pais_autor', 'editorial_autor'])
        libro_obj = Libro()
        for libro_obj in libros:
            autor = libro_obj.mostrar_autor()
            hoja.append([
                libro_obj.get_codigo_libro(),
                libro_obj.get_titulo(),
                libro_obj.get_year(),
                libro_obj.get_tomo(),
                autor.get_codigo(),
                autor.get_nombre(),
                autor.get_pais(),
                autor.get_editorial()
            ])

            libro.save(self.archivo)
            libro.close()


    #----------------------OBTENER-CATEGORIAS------------------------------------
    def obtener_categorias(self):

        libro, hoja = self._abrir_archivo()
        if hoja is None:
            return []
        
        datos = []
        for row in hoja.iter_row(values_only=True):
            if row[0] != 'cod_categoria':
                datos.append({'cod_categoria': row[0], 'categoria': row[1]})
        libro.close()
        return datos

    # -----------------GUARDAR CATEGORIAS--------------------------------------
    def guardar_categorias(self, categorias):
        libro = Workbook()
        hoja = libro.active
        hoja.append(['cod_categoria', 'categoria'])
        for categoria in categorias:
            hoja.append([categoria.cod_categoria, categoria.categoria])
        libro.save(self.archivo)

    # --------------------------OBTENER PERSONAS----------------------------------------------------
    def obtener_personas(self):

        libro, hoja = self._abrir_archivo()

        if hoja is None:
            return []
        datos = []
        for row in hoja.iter_row(values_only=True):
            if row[0] != 'cod_persona':
                datos.append({'cod_persona': row[0], 'nombre': row[1], 'apellidoPaterno': row[2],
                              'apellidoMaterno': row[3], 'fecha_nacimieto': row[4]})
        libro.close()
        return datos

    # -----------------GUARDAR PERSONAS--------------------------------------
    def guardar_personas(self, personas):
        libro = Workbook()
        hoja = libro.active
        hoja.append(['cod_persona', 'nombre', 'apellidoPaterno',
                     'apellidoMaterno', 'fecha_nacimieto'])
        for persona in personas:
            hoja.append([persona.cod_persona, persona.nombre, persona.apellidoPaterno,
                         persona.apellidoMaterno, persona.fecha_nacimieto])
        libro.save(self.archivo)

    def cerrar(self):
        pass
