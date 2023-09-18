from base_de_datos import BaseDeDatos
class Mantenimiento():

    def __init__(self):
        self.libro_counter = 1
        self.libro_categoria_counter ='1'
        self.autor_counter = 1
        self.libros_eliminados=[]
        self.autores_eliminados= []
        self.categorias_eliminadas = []
        pass
######################GENERAR UN CODIGO ALEATORIO PARA LIBRO Y CATEGORIA####################
    def generar_codigo_libro(self):
        #generamos un codigo de libro único asegurandonos que no se repita
        codigo_libro = f'L{self.libro_counter: 04}'
        self.libro_counter += 1
        return codigo_libro 

    def generar_codigo_categoria(self):
        #generamos un codigo de categoria único asegurandonos que no se repita
        codigo_categoria = f'C{self.libro_categoria_counter: 04}'
        self.libro_categoria_counter += 1
        return codigo_categoria
    def generar_codigo_autor(self):
        #generamos un codigo de autor único asegurandonos que no se repita
        codigo_autor = f'A{self.autor_counter: 04}'
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
        bd = BaseDeDatos('base.xls')

        # Llamar al método de la base de datos para guardar el libro
        bd.guardar_libros([libro_nuevo])

    #------------------ELIMINAR_LIBRO--------------------------------------------
    def eliminar_libro(self, codigo_libro):
        #guardamos los codigos de libros eliminados para una retulizacion de codigos
        self.libros_eliminados.append(codigo_libro)

        bd = BaseDeDatos('base.xls')
        return bd.eliminar_libro(codigo_libro)
        
        
    #-------------------EDITAR LIBROS------------------------------
    def editar_libro(self, codigo_libro, nuevo_titulo, nuevo_ano, nuevo_tomo):
        bd = BaseDeDatos('base.xls')
        return bd.editar_libro(codigo_libro, nuevo_titulo, nuevo_ano, nuevo_tomo)

    def generar_codigo_libro(self):
        self.codigo_libro = print("genera el codigo del libro")
        return self.codigo_libro
    #---------------OBTENER LIBROS -------------------------------------------------

    def obtener_libros(self):
        bd = BaseDeDatos('base.xls')
        return bd.obtener_libros()
    
    #-----------------BUSCAR LIBROS-----------------------------------------------------------
    def buscar_libro(self, codigo_libro):
        bd = BaseDeDatos('base.xls')
        return bd.buscar_libro(codigo_libro)
    
    ################################AUTOR#####################################
    def agregar_autor(self, codigo_autor, nombre, apellido):
        codigo_autor = self.generar_codigo_autor()
        autores_a_guardar = [
            {'codigo_autor': codigo_autor, 'nombre': nombre, 'apellido': apellido}
        ]

        bd = BaseDeDatos('base.xls')
        bd.guardar_autores(autores_a_guardar)

    #.....................ASIGNAR UN AUTOR A LIBRO..............................}
    def asignar_autor_a_libro(self, codigo_libro, codigo_autor):
        bd = BaseDeDatos('base.xls')
        bd.asignar_autor_a_libro(codigo_libro, codigo_autor)


    
    
    #---------------------OBTENER AUTORES----------------------------
    def obtener_autores(self):
        bd = BaseDeDatos('base.xls')
        return bd.obtener_autores()
    #------------------ELIMINAR AUTORES------------------------------
    def eliminar_autor(self, codigo_autor):
        self.autores_eliminados(codigo_autor)
        bd = BaseDeDatos('base.xls')
        return bd.eliminar_autor(codigo_autor)
    #------------------EDITAR AUTORES------------------------------
    def editar_autor(self, codigo_autor, nuevo_nombre, nuevo_apellido):
        bd = BaseDeDatos('base.xls')
        return bd.editar_autor(codigo_autor, nuevo_nombre, nuevo_apellido)



##########################CATEGORIAS#####################################################




    #------------------AGREGAR_CATEGORIA--------------------------------------------
    def agregar_categoria(self, codigo_categoria, categoria):
        codigo_categoria = self.generar_codigo_categoria()
        categorias_a_guardar = [
            {'codigo_categoria': codigo_categoria, 'categoria': categoria}
        ]

        bd = BaseDeDatos('base.xls')
        bd.guardar_categorias(categorias_a_guardar)
    #------------------Asignar_categoria_a_libro------------------
    def asignar_categoria_a_libro(self, codigo_libro, codigo_categoria):
        bd = BaseDeDatos('base.xls')
        bd.asignar_categoria_a_libro(codigo_libro, codigo_categoria)
    #---------------------OBTENER CATEGORIAS----------------------------
    def obtener_categorias(self):
        bd = BaseDeDatos('base.xls')
        return bd.obtener_categorias()