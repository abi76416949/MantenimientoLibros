from Mantenimiento import Mantenimiento
from openpyxl import Workbook
from base_de_datos import BaseDeDatos

# Crear una instancia de Mantenimiento
Mantenimiento = Mantenimiento()

# Función para registrar un libro
def registrar_libro():
    print("Registro de un nuevo libro:")
    codigo_libro = Mantenimiento.generar_codigo_libro()
    titulo = input("Ingrese el título del libro: ")
    year = input("Ingrese el año de publicación: ")
    tomo = input("Ingrese el número de tomo: ")
    Mantenimiento.agregar_libro(codigo_libro, titulo, year, tomo)
    print(f'Registro exitoso del libro con código {codigo_libro}')

def obtener_libros():
    listado_libros = Mantenimiento.obtener_libros()
    for libro in listado_libros:
        print(f'Código: {libro["codigo_libro"]}, Título: {libro["titulo"]}, Año: {libro["aho"]}, Tomo: {libro["tomo"]}')

def editar_libro():
    codigo_libro = input('Ingrese el código del libro a editar: ')
    nuevo_titulo = input('Ingrese el nuevo título del libro: ')
    nuevo_ano = input('Ingrese el nuevo año del libro: ')
    nuevo_tomo = input('Ingrese el nuevo tomo del libro: ')
    
    if Mantenimiento.editar_libro(codigo_libro, nuevo_titulo, nuevo_ano, nuevo_tomo):
        print(f'Libro con código {codigo_libro} editado correctamente.')
    else:
        print(f'No se encontró un libro con código {codigo_libro}.')

def eliminar_libro():
    codigo_libro = input('Ingrese el código del libro a eliminar: ')
    if Mantenimiento.eliminar_libro(codigo_libro):
        print(f'Libro con código {codigo_libro} eliminado correctamente.')
    else:
        print(f'No se encontró un libro con código {codigo_libro}.')

opciones = {
    "1": registrar_libro,
    "2": obtener_libros,
    "3": editar_libro,
    "4": eliminar_libro,
    "5": exit
}

while True:
    print("##########################")
    print("Menú:")
    print("1. Registrar libro")
    print("2. Listar libros")
    print("3. Editar libro")
    print("4. Eliminar libro")
    print("5. Salir")
    print("##########################")
    
    seleccion = input("Seleccione una opción: ")

    if seleccion in opciones:
        opciones[seleccion]()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

