libros = []

def insertarLibro(): 
    titulo = input("inserta un nombre para el libro").strip()
    
    if not titulo:
        print("Introduce un titulo: ");
        return
    
    autor = input("introduce un autor")
    año = input("introduce un año")
    tipo = input("introduce el tipo de libro")
    
    libro = {"titulo" : titulo , "autor" : autor , "año" : año, "tipo" : tipo};
    libros.append(libro);
    
    print(libros);
    
    
def buscarLibro():
    
    entrada = input("Introduzca nombre del libro a buscar");
    

def modificarLibro():
    
    entrada = input("Introduzca libro a modificar")
    
def eliminarLibro():
    
    entrada = input("Introduzca libro a eliminar")
    
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