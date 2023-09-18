
from base_de_datos import BaseDeDatos
class Mantenimiento():

    def __init__(self):
        pass


#------------------AGREGAR_LIBRO--------------------------------------------

    def agregar_libro(self,cod_libroo, titulo, year, tomo ):
        libros_a_guardar = [
            {'codigo_libro': cod_libroo, 
             'titulo': titulo,
             'aho': year, 
             'tomo': tomo}
        ]

        bd= BaseDeDatos('base.xls')
        bd.guardar_libros(libros_a_guardar)


    #------------------ELIMINAR_LIBRO--------------------------------------------
    def eliminar_libro(self, codigo_libro):
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
        bd = BaseDeDatos('base.xls')
        return bd.eliminar_autor(codigo_autor)
    #------------------EDITAR AUTORES------------------------------
    def editar_autor(self, codigo_autor, nuevo_nombre, nuevo_apellido):
        bd = BaseDeDatos('base.xls')
        return bd.editar_autor(codigo_autor, nuevo_nombre, nuevo_apellido)



##########################CATEGORIAS#####################################################


    #------------------Asignar_categoria_a_libro------------------
    def asignar_categoria_a_libro(self, codigo_libro, codigo_categoria):
        bd = BaseDeDatos('base.xls')
        bd.asignar_categoria_a_libro(codigo_libro, codigo_categoria)
    #---------------------OBTENER CATEGORIAS----------------------------
    def obtener_categorias(self):
        bd = BaseDeDatos('base.xls')
        return bd.obtener_categorias()