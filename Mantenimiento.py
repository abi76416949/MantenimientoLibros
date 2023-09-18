from base_de_datos import BaseDeDatos
import datetime

class Mantenimiento():

    def __init__(self):
        self.libro_counter = 1
        self.libro_categoria_counter =1
        self.autor_counter = 1
        self.libros_eliminados=[]
        self.autores_eliminados= []
        self.categorias_eliminadas = []
        pass
    
######################GENERAR UN CODIGO ALEATORIO PARA LIBRO Y CATEGORIA####################
    def generar_codigo_libro(self):
        #generamos un codigo de libro único asegurandonos que no se repita
        codigo_libro = f'L{self.libro_counter: 004}'
        self.libro_counter += 1
        print(codigo_libro)
        return codigo_libro 

    def generar_codigo_categoria(self):
        #generamos un codigo de categoria único asegurandonos que no se repita
        codigo_categoria = f'C{self.libro_categoria_counter: 004}'
        self.libro_categoria_counter += 1
        return codigo_categoria
    
    def generar_codigo_autor(self):
        #generamos un codigo de autor único asegurandonos que no se repita
        codigo_autor = f'A{self.autor_counter: 004}'
        self.autor_counter += 1
        return codigo_autor
    
#------------------AGREGAR_LIBRO--------------------------------------------

    def agregar_libro(self, cod_libro, titulo, year, tomo):
        
        # Crear un diccionario con los datos del libro
        libro_nuevo = {'codigo_libro': cod_libro,
                        'titulo': titulo,
                        'aho': year,
                        'tomo': tomo}

        # Crear una instancia de la base de datos
        bd = BaseDeDatos('base.xlsx')

        # Llamar al método de la base de datos para guardar el libro
        bd.guardar_libros([libro_nuevo])

    #------------------ELIMINAR_LIBRO--------------------------------------------
    def eliminar_libro(self, codigo_libro):
        #guardamos los codigos de libros eliminados para una retulizacion de codigos
        self.libros_eliminados.append(codigo_libro)

        bd = BaseDeDatos('base.xlsx')
        return bd.eliminar_libro(codigo_libro)
        
        
    #-------------------EDITAR LIBROS------------------------------
    def editar_libro(self, codigo_libro, nuevo_titulo, nuevo_ano, nuevo_tomo):
        bd = BaseDeDatos('base.xlsx')
        return bd.editar_libro(codigo_libro, nuevo_titulo, nuevo_ano, nuevo_tomo)
    #---------------OBTENER LIBROS -------------------------------------------------

    def obtener_libros(self):
        bd = BaseDeDatos('base.xlsx')
        return bd.obtener_libros()
    
    #-----------------BUSCAR LIBROS-----------------------------------------------------------
    def buscar_libro(self, codigo_libro):
        bd = BaseDeDatos('base.xlsx')
        return bd.buscar_libro(codigo_libro)
    
#-----------------------GENERAR INFORME DE LIBROS-----------------------------------------
    def generar_informe_libros(self, libros):
    # Obtener la fecha actual
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Crear el nombre del archivo de informe usando la fecha
        nombre_archivo = f"reporte_{fecha_actual}.txt"

        try:
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                # Escribir el encabezado del informe con la fecha
                archivo.write(f"Informe de Libros - {fecha_actual}\n\n")

                # Recorrer la lista de libros y escribir la información de cada libro
                for libro in libros:
                    archivo.write(f"Código: {libro['codigo_libro']}\n")
                    archivo.write(f"Título: {libro['titulo']}\n")
                    archivo.write(f"Año de Publicación: {libro['aho']}\n")
                    archivo.write(f"Tomo: {libro['tomo']}\n")
                    archivo.write("\n")  # Separador entre libros

            print(f"Informe de libros generado y guardado en '{nombre_archivo}'.")

        except Exception as e:
            print(f"Error al generar el informe: {str(e)}")
    ################################AUTOR#####################################
    def agregar_autor(self, codigo_autor, nombre, apellido):
        codigo_autor = self.generar_codigo_autor()
        autores_a_guardar = [
            {'codigo_autor': codigo_autor, 'nombre': nombre, 'apellido': apellido}
        ]

        bd = BaseDeDatos('base.xlsx')
        bd.guardar_autores(autores_a_guardar)

    #.....................ASIGNAR UN AUTOR A LIBRO..............................}
    def asignar_autor_a_libro(self, codigo_libro, codigo_autor):
        bd = BaseDeDatos('base.xlsx')
        bd.asignar_autor_a_libro(codigo_libro, codigo_autor)


    
    
    #---------------------OBTENER AUTORES----------------------------
    def obtener_autores(self):
        bd = BaseDeDatos('base.xlsx')
        return bd.obtener_autores()
    #------------------ELIMINAR AUTORES------------------------------
    def eliminar_autor(self, codigo_autor):
        self.autores_eliminados.append(codigo_autor)
        bd = BaseDeDatos('base.xlsx')
        return bd.eliminar_autor(codigo_autor)
    #------------------EDITAR AUTORES------------------------------
    def editar_autor(self, codigo_autor, nuevo_nombre, nuevo_apellido):
        bd = BaseDeDatos('base.xlsx')
        return bd.editar_autor(codigo_autor, nuevo_nombre, nuevo_apellido)



##########################CATEGORIAS#####################################################




    #------------------AGREGAR_CATEGORIA--------------------------------------------
    def agregar_categoria(self, codigo_categoria, categoria):
        codigo_categoria = self.generar_codigo_categoria()
        categorias_a_guardar = [
            {'codigo_categoria': codigo_categoria, 'categoria': categoria}
        ]

        bd = BaseDeDatos('base.xlsx')
        bd.guardar_categorias(categorias_a_guardar)
    #------------------Asignar_categoria_a_libro------------------
    def asignar_categoria_a_libro(self, codigo_libro, codigo_categoria):
        bd = BaseDeDatos('base.xlsx')
        bd.asignar_categoria_a_libro(codigo_libro, codigo_categoria)
    #---------------------OBTENER CATEGORIAS----------------------------
    def obtener_categorias(self):
        bd = BaseDeDatos('base.xls')
        return bd.obtener_categorias()

md = Mantenimiento()
md.generar_codigo_libro()