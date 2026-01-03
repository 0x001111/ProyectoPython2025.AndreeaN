libros = []

def insertarLibro(): 
    titulo = input("inserta un nombre para el libro").strip()
    
    if not titulo:
        print("Introduce un titulo: ");
        return
    

    encontrado = False; 

    for l in libros: 
        if l['titulo'].lower() == titulo.lower():
            encontrado = True; 
            print("Este libro ya está registrado. ");
            break 
            
   

    autor = input("introduce un autor")
    año = input("introduce un año")
    tipo = input("introduce el tipo de libro")
    
    libro = {"titulo" : titulo , "autor" : autor , "año" : año, "tipo" : tipo};
    libros.append(libro);
    
    print("libro '{titulo}' añadido correctamente");
    
    
def buscarLibro():
    
    entrada = input("Introduzca nombre del libro a buscar");
    for libro in libros:
        if libro['titulo'.lower() == entrada.lower()]:
            return libro
    return None 

def modificarLibro():
    entrada = input("Introduce libro a modificar: ").strip()
    encontrado = False

    for l in libros:
        if l['titulo'].lower() == entrada.lower():
            # Título
            nuevo_titulo = input("Título (" + l['titulo'] + "): ").strip()
            if nuevo_titulo:
                l['titulo'] = nuevo_titulo

            # Autor
            nuevo_autor = input("Autor (" + l['autor'] + "): ").strip()
            if nuevo_autor:
                l['autor'] = nuevo_autor

            # Año con validación
            while True:
                nuevo_año = input("Año (" + l['año'] + "): ").strip()
                if not nuevo_año:
                    break  # deja vacío = no modificar
                if nuevo_año.isdigit():
                    l['año'] = nuevo_año
                    print("Año actualizado")
                    break
                print("Año inválido. Debe ser un número.")

            # Tipo con validación
            while True:
                nuevo_tipo = input("Tipo (" + l['tipo'] + "): ").strip()
                if not nuevo_tipo:
                    break  # deja vacío = no modificar
                l['tipo'] = nuevo_tipo
                print("Tipo actualizado")
                break

            encontrado = True
            break  # ya encontramos el libro, no seguimos buscando

    if not encontrado:
        print("No se ha encontrado el libro")

                

def eliminarLibro():
    
    print(libros); 
    entrada = input("Introduzca el titulo del libro a eliminar").strip()
    encontrado = False; 
    for l in libros: 
        if l['titulo'].lower() == entrada.lower(): 
            libros.remove(l)
            print("el libro con el titulo " + entrada +  " ha sido eliminado")
            encontrado = True; 
            break 
    if not encontrado: 
        print("No se ha encontrado el libro con ese titulo");


def mostrarDatos():
    encontrado = False
    print("----------------------");
    print("LIBROS:")
    for l in libros: 
        print("----------------------");
        print(f"titulo: {l['titulo']}")
        print("----------------------");
        
    entrada = input("Introduzca titulo a mostrar datos").strip() #strip() limpia espacios antes y después del input.
    
    for libro in libros:
        if libro['titulo'].lower() == entrada.lower():
            print("----------------------");
            print(f"titulo: {libro['titulo']}")
            print(f"Autor: {libro['autor']}")
            print(f"Año: {libro['año']}")
            print(f"Tipo: {libro['tipo']}")
            print("----------------------");
            encontrado = True
            break
        
        if not encontrado:
            print("introduzca un titulo válido")
                    
    
    
def salir(): 
    
    input("salir")
    
def menu():

    while True: 
            
        print("----Menu principal. LIBROS----");
        print("1.Añadir libro");
        print("2.Mostrar datos libro");
        print("3.Modificar libro");
        print("4.Eliminar libro");
        print("5.Salir");
        print("----------------------");
        
        opcion = input("----elige una opción----");
        
        match opcion:
            
            case "1":
                insertarLibro();
            case "2":
                mostrarDatos();
            case "3":
                modificarLibro();
            case "4":
                eliminarLibro();
                break
            case "5":
                break
                
menu()