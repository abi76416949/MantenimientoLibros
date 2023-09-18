from mantenimiento import Mantenimiento
from base_de_datos import BaseDeDatos
from openpyxl import load_workbook

def main():
    # Crear una instancia de Mantenimiento
    mantenimiento = Mantenimiento()
    
    while True:
        print("##########################")
        print("Menú:")
        print("1. Registrar libro")
        print("2. Listar libros")
        print("3. Editar libro")
        print("4. Eliminar libro")
        print("5. Generar informe")
        print("6. Salir")
        print("##########################")
        
        seleccion = input("Seleccione una opción: ")

        if seleccion == "1":
            registrar_libro(mantenimiento)
        elif seleccion == "2":
            obtener_libros(mantenimiento)
        elif seleccion == "3":
            editar_libro(mantenimiento)
        elif seleccion == "4":
            eliminar_libro(mantenimiento)
        elif seleccion == "5":
            exit()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def registrar_libro(mantenimiento):
    print("Registro de un nuevo libro:")
    codigo_libro = mantenimiento.generar_codigo_libro()
    titulo = input("Ingrese el título del libro: ")
    year = input("Ingrese el año de publicación: ")
    tomo = input("Ingrese el número de tomo: ")
    mantenimiento.agregar_libro(codigo_libro, titulo, year, tomo)
    print(f'Registro exitoso del libro con código {codigo_libro}')

def obtener_libros(mantenimiento):
    listado_libros = mantenimiento.obtener_libros()
    for libro in listado_libros:
        print(f'Código: {libro["codigo_libro"]}, Título: {libro["titulo"]}, Año: {libro["aho"]}, Tomo: {libro["tomo"]}')

def editar_libro(mantenimiento):
    codigo_libro = input('Ingrese el código del libro a editar: ')
    nuevo_titulo = input('Ingrese el nuevo título del libro: ')
    nuevo_ano = input('Ingrese el nuevo año del libro: ')
    nuevo_tomo = input('Ingrese el nuevo tomo del libro: ')
    
    if mantenimiento.editar_libro(codigo_libro, nuevo_titulo, nuevo_ano, nuevo_tomo):
        print(f'Libro con código {codigo_libro} editado correctamente.')
    else:
        print(f'No se encontró un libro con código {codigo_libro}.')

def eliminar_libro(mantenimiento):
    codigo_libro = input('Ingrese el código del libro a eliminar: ')
    if mantenimiento.eliminar_libro(codigo_libro):
        print(f'Libro con código {codigo_libro} eliminado correctamente.')
    else:
        print(f'No se encontró un libro con código {codigo_libro}.')

def generar_informe():
    # Obtener la lista de libros
    lista_de_libros = Mantenimiento.obtener_libros()
    
    # Llamar al metodo
    Mantenimiento().generar_informe_libros(lista_de_libros)

if __name__ == "__main__":
    main()


