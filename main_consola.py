from mantenimiento import Mantenimiento


menu = {
    '1': 'Agregar Libro',
    '2': 'Eliminar Libro',
    '3': 'Editar Libro',
    '4': 'Listar Libros',
    '5': 'Buscar Libro',
    '6': 'Salir'
}

menuLibros = {
    '1' :'Agregar categoria '

}

def main():
    # Instancia a la clase Mantenimiento
    mt = Mantenimiento()
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
            mt.agregar_libro(codigo_libro,titulo,year,tomo)

        elif opcion == "2":
            codigo_libro = input("Ingrese el código del libro a eliminar: ")
            mt.eliminar_libro(codigo_libro)
            

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
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()