from biblioteca import Biblioteca


def main():
    biblioteca = Biblioteca()

    while True:
        print("""
            ---- MENÚ LIBROS ----
            1. Añadir libro
            2. Mostrar libros
            3. Modificar libro
            4. Eliminar libro
            5. Mostrar Autores (Sin repetidos)
            6. Generar Reporte
            7. Salir
            """)

        opcion = input("Elige una opción: ").strip()

        match opcion:
            case "1":
                biblioteca.insertar()
            case "2":
                biblioteca.mostrar()
            case "3":
                biblioteca.modificar()
            case "4":
                biblioteca.eliminar()
            case "5":
                biblioteca.mostrar_autores_unicos()
            case "6":
                biblioteca.generar_reporte()
            case "7":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida")


if __name__ == "__main__":
    main()
