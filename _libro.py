
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
    
    ################################Autor#####################################
    