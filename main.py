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
            7. Calcular Inversión total de un tipo de libro en específico
            8. Salir
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
                biblioteca.autores_sin_repetir()
            case "6":
                biblioteca.generar_reporte()
            case "7":
                biblioteca.calcular_inversion()
            case "8":
                print("saliendo...")
                break
            case _:
                print("Opción no válida")


if __name__ == "__main__":
    main()
