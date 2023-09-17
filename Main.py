from negocio_autor import AutorNegocio
from Libro import Libro
import pandas as pd
from openpyxl import Workbook

negocio_autor = AutorNegocio()

def registrar_libro():
    titulo = input('Ingrese titulo: ')

    nombre = input('Ingrese nombre: ')
    ap_paterno = input('Ingrese ap_paterno: ')
    ap_materno = input('Ingrese ap_materno: ')
    dni = input('Ingrese dni: ')
    codigo = input('Ingrese codigo: ')
    facultad = input('Ingrese facultad: ')
    negocio_autor.registrar_docente(nombre, ap_paterno, ap_materno, dni, codigo, facultad)
    negocio_autor.guardar_docentes()
    print(f'Registro exitoso del docente')

def obtener_docentes():
    listado_docentes = docente_negocio.obtener_docentes()
    for docente in listado_docentes:
        print(docente.imprimir())

def editar_docente():
    indice = int(input('Ingrese el índice del docente a editar: '))
    nombre = input('Ingrese nombre: ')
    ap_paterno = input('Ingrese ap_paterno: ')
    ap_materno = input('Ingrese ap_materno: ')
    dni = input('Ingrese dni: ')
    codigo = input('Ingrese codigo: ')
    facultad = input('Ingrese facultad: ')
    print(docente_negocio.editar_docente(indice, nombre, ap_paterno, ap_materno, dni, codigo, facultad))

opciones = {
    "1": registrar_docentes,
    "2": obtener_docentes,
    "3": editar_docente,
    "4": exit
}

while True:
    print("##########################")
    print("Menú:")
    print("1. Registrar docentes")
    print("2. Listar docentes")
    print("3. Editar docente")
    print("4. Salir")
    print("##########################")
    
    seleccion = input("Seleccione una opción: ")

    if seleccion in opciones:
        opciones[seleccion]()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")