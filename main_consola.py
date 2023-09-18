from Mantenimiento import Mantenimiento

mt = Mantenimiento()

menu = {
    '1': 'Agregar Libro',
    '2': 'Eliminar Libro',
    '3': 'Editar Libro',
    '4': 'Listar Libros',
    '5': 'Buscar Libro',
    '6': 'Buscar Categoría',
    '7': 'Eliminar Categoría',
    '8': 'Editar Categoría',
    '9': 'Informe de Libros',
    '10': 'Salir'
}

def sub_menu_buscar_categoria(mt):
    while True:
        print("\nSubmenú - Buscar Libro por Categoría:")
        print("1. Listar Libros por Categoría")
        print("2. Buscar Libro por Categoría")
        print("3. Eliminar Categoría")
        print("4. Editar Categoría")
        print("5. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Listar libros por categoría
            codigo_categoria = input("Ingrese el código de la categoría: ")
            libros = mt.listar_libros_por_categoria(codigo_categoria)
            for libro in libros:
                print(f"Código: {libro['codigo_libro']}, Título: {libro['titulo']}, Año: {libro['aho']}, Tomo: {libro['tomo']}")

        elif opcion == "2":
            # Buscar libro por categoría
            codigo_categoria = input("Ingrese el código de la categoría: ")
            codigo_libro = input("Ingrese el código del libro: ")
            libro = mt.buscar_libro_por_categoria(codigo_categoria, codigo_libro)
            if libro:
                print(f"Código: {libro['codigo_libro']}, Título: {libro['titulo']}, Año: {libro['aho']}, Tomo: {libro['tomo']}")
            else:
                print("Libro no encontrado en la categoría.")

        elif opcion == "3":
            # Eliminar categoría
            codigo_categoria = input("Ingrese el código de la categoría a eliminar: ")
            mt.eliminar_categoria(codigo_categoria)
            print("Categoría eliminada correctamente.")

        elif opcion == "4":
            # Editar categoría
            codigo_categoria = input("Ingrese el código de la categoría a editar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre de la categoría: ")
            mt.editar_categoria(codigo_categoria, nuevo_nombre)
            print("Categoría editada correctamente.")

        elif opcion == "5":
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def main():
    # Instancia a la clase Mantenimiento
    
    while True:
        print("\nMenú Principal:")
        # Itera sobre las opciones del menú y las muestra
        for opcion, descripcion in menu.items():
            print(f"{opcion}. {descripcion}")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo_libro = str(mt.generar_codigo_libro())
            titulo = input("Ingrese el título del libro: ")
            year = input("Ingrese el año del libro: ")
            tomo = input("Ingrese el tomo del libro: ")
            mt.agregar_libro(codigo_libro, titulo, year, tomo)

            categoria= input(" ingrese categoria del libro ")

            codigo_categoria = str(mt.generar_codigo_categoria())
            mt.asignar_categoria_a_libro(codigo_categoria,categoria)

        elif opcion == "2":
            codigo_libro = input("Ingrese el código del libro a eliminar: ")
            mt.eliminar_libro(codigo_libro)

        elif opcion == "3":
            codigo_libro = input("Ingrese el código del libro a editar: ")
            nuevo_titulo = input("Ingrese el nuevo título del libro: ")
            nuevo_ano = input("Ingrese el nuevo año del libro: ")
            nuevo_tomo = input("Ingrese el nuevo tomo del libro: ")
            mt.editar_libro(codigo_libro, nuevo_titulo, nuevo_ano, nuevo_tomo)

        elif opcion == "4":
            listado_libros = mt.obtener_libros()
            for libro in listado_libros:
                print(f"Código: {libro['codigo_libro']}, Título: {libro['titulo']}, Año: {libro['aho']}, Tomo: {libro['tomo']}")

        elif opcion == "5":
            codigo_libro = input("Ingrese el código del libro a buscar: ")
            libro = mt.buscar_libro(codigo_libro)
            print(f"Código: {libro['codigo_libro']}, Título: {libro['titulo']}, Año: {libro['aho']}, Tomo: {libro['tomo']}")

        elif opcion == "6":
            sub_menu_buscar_categoria(mt)

        elif opcion == "7":
            codigo_categoria = input("Ingrese el código de la categoría a eliminar: ")
            mt.eliminar_categoria(codigo_categoria)
            print("Categoría eliminada correctamente.")

        elif opcion == "8":
            codigo_categoria = input("Ingrese el código de la categoría a editar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre de la categoría: ")
            mt.editar_categoria(codigo_categoria, nuevo_nombre)
            print("Categoría editada correctamente.")

        elif opcion == "9":
            listado_libros = mt.obtener_libros()
            mt.generar_informe_libros(listado_libros)

        elif opcion == "10":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
