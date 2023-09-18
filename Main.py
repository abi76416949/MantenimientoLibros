from mantenimiento import Mantenimiento

mt = Mantenimiento()

menu = {
    '1': 'Agregar Libro',
    '2': 'Eliminar Libro',
    '3': 'Editar Libro',
    '4': 'Listar Libros',
    '5': 'Buscar Libro',
    '6': 'Informe de Libros',
    '7': 'Salir'
}

def main():
    # Instancia a la clase Mantenimiento
    
    while True:
        print("\nMenú Principal:")
        
        # Itera sobre las opciones del menú y las muestra
        for opcion, descripcion in menu.items():
            print(f"{opcion}. {descripcion}")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            year = input("Ingrese el año del libro: ")
            tomo = input("Ingrese el tomo del libro: ")
            mt.agregarLibros(titulo,year,tomo)

            #categoria= input(" ingrese categoria del libro ")

            #codigo_categoria = str(mt.generar_codigo_categoria())
            #mt.asignar_categoria_a_libro(codigo_categoria,categoria)

        elif opcion == "2":
             while True:
                codigo_libro = input("Ingrese el código del libro a eliminar: ")
                try:
                    if mt.eliminar_libro(codigo_libro):
                        print("Libro eliminado con éxito.")
                        break
                    else:
                        print("El código del libro no existe. Intente nuevamente.")
                except Exception as e:
                    print(f"Ocurrió un error al eliminar el libro: {e}")
                    
        elif opcion == "7":
            print("¡Hasta luego!")
            break
                    
"""
        elif opcion == "3":
            codigo_libro = input("Ingrese el código del libro a editar: ")
            nuevo_titulo = input("Ingrese el nuevo título del libro: ")
            nuevo_ano = input("Ingrese el nuevo año del libro: ")
            nuevo_tomo = input("Ingrese el nuevo tomo del libro: ")

            mt.editar_libro(codigo_libro,nuevo_titulo,nuevo_ano,nuevo_tomo)

        elif opcion == "4":
            
            listado_libros = mt.obtener_libros()
            for libro in listado_libros:
                print(f"Código: {libro['codigo_libro']}, Título: {libro['titulo']}, Año: {libro['aho']}, Tomo: {libro['tomo']}")
            

        elif opcion == "5":
            codigo_libro = input("Ingrese el código del libro a buscar: ")
            libro = mt.buscar_libro(codigo_libro)
            print(f"Código: {libro['codigo_libro']}, Título: {libro['titulo']}, Año: {libro['aho']}, Tomo: {libro['tomo']}")
            
        elif opcion == "6":
        #informe de libros
            listado_libros = mt.obtener_libros()
            mt.generar_informe_libros(listado_libros)
        
        elif opcion == "7":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")"""

if __name__ == "__main__":
    main()
