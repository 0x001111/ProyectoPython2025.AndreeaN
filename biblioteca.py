import json
import logging
from libro import Libro, LibroDigital, LibroEspecial

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Biblioteca:
    FICHERO = "libros.json"

    def __init__(self):
        self.libros = []
        self.cargar()

    def cargar(self):
        """Carga los libros desde el archivo JSON"""
        try:
            with open(self.FICHERO, "r", encoding="utf-8") as f:
                datos = json.load(f)
                self.libros = []
                for d in datos:
                    # Verificar si es digital Y tiene formato
                    if d.get("tipo") == "digital" and "formato" in d:
                        obj = LibroDigital(
                            d["titulo"], 
                            d["autor"], 
                            d["año"], 
                            d["tipo"], 
                            d["formato"]
                        )
                    elif d.get("tipo") == "Especial":
                        obj = LibroEspecial(
                            d["titulo"], 
                            d["autor"], 
                            d["año"], 
                            d.get("especialidad", "General"), 
                            12
                        )
                    else:
                        # Si no, crear libro normal
                        obj = Libro(
                            d["titulo"], 
                            d["autor"], 
                            d["año"], 
                            d.get("tipo", "Normal")
                        )
                    self.libros.append(obj)
                logging.info(f"Cargados {len(self.libros)} libros desde {self.FICHERO}")
        except FileNotFoundError:
            logging.warning(f"Archivo {self.FICHERO} no encontrado. Creando biblioteca vacía.")
            self.libros = []
        except json.JSONDecodeError as e:
            logging.error(f"Error al leer JSON: {e}")
            self.libros = []
        except Exception as e:
            logging.error(f"Error inesperado al cargar: {e}")
            self.libros = []

    def guardar(self):
        """Guarda los libros en el archivo JSON"""
        try:
            with open(self.FICHERO, "w", encoding="utf-8") as f:
                json.dump(
                    [l.to_dict() for l in self.libros],
                    f,
                    indent=4,
                    ensure_ascii=False
                )
            logging.info(f"Guardados {len(self.libros)} libros en {self.FICHERO}")
        except Exception as e:
            logging.error(f"Error al guardar: {e}")
            print(f"Error al guardar: {e}")

    # ---------- BÚSQUEDA ----------
    
    def buscar_por_titulo(self, titulo):
        """Busca un libro por título exacto (insensible a mayúsculas)"""
        titulo_lower = titulo.lower().strip()
        for libro in self.libros:
            if libro.titulo.lower().strip() == titulo_lower:
                return libro
        return None

    # ---------- LÓGICA ----------
    
    def generar_reporte(self):
        """Genera un reporte ordenado con estadísticas"""
        if not self.libros:
            print("No hay libros en la biblioteca.")
            return
        
        # 1. Ordenar alfabéticamente
        libros_ordenados = sorted(self.libros, key=lambda l: l.titulo.lower())
        
        # 2. Mostrar lista ordenada
        print("\n--- REPORTE DE LIBROS ---")
        for l in libros_ordenados:
            print(f"Título: {l.titulo} ({l.tipo})")
        
        # 3. Calcular totales
        total_libros = len(self.libros)
        contador_digitales = sum(1 for l in self.libros if isinstance(l, LibroDigital))
        contador_especiales = sum(1 for l in self.libros if isinstance(l, LibroEspecial))
        
        # 4. Mostrar resumen
        print(f"\n--- RESUMEN ---")
        print(f"Total libros: {total_libros}")
        print(f"Libros digitales: {contador_digitales}")
        print(f"Libros físicos: {total_libros - contador_digitales}")
        print(f"Libros Especiales: {contador_especiales}")
    
    def mostrar_autores_unicos(self):
        """Muestra todos los autores sin repetir"""
        if not self.libros:
            print("No hay ningún autor. Biblioteca vacía.")
            return
        
        conjunto_autores = {libro.autor for libro in self.libros}
        
        print('\n--- Autores en la Biblioteca (Sin Repetir) ---')
        for autor in sorted(conjunto_autores):
            print(f"- {autor}")

    def insertar(self):
        """Añade un nuevo libro a la biblioteca"""
        print("\n--- AÑADIR LIBRO ---")
        titulo = input("Título: ").strip()
        
        if not titulo:
            print("El título no puede estar vacío.")
            return
        
        # Búsqueda parcial para avisar de duplicados
        for libro in self.libros:
            if titulo.lower() in libro.titulo.lower(): 
                print(f"Aviso: Ya existe algo parecido llamado '{libro.titulo}'")
        
        autor = input("Autor: ").strip()
        if not autor:
            print("El autor no puede estar vacío.")
            return
        
        año = input("Año: ").strip()
        if not año:
            print("El año no puede estar vacío.")
            return
        
        # Tipo de libro
        print("\n1. Normal (físico)")
        print("2. Digital")
        print("3. Especial")
        tipo_opcion = input("Selecciona tipo (1, 2, 3): ").strip()
        
        if tipo_opcion == "2":
            formato = input("Formato (PDF/WORD): ").strip().upper()
            if not formato:
                formato = "PDF"
            nuevo = LibroDigital(titulo, autor, año, "digital", formato)
        elif tipo_opcion == "3": 
            tipo_especialidad = input("Que tipo de especialidad tiene?: ").strip()
            nuevo = LibroEspecial(titulo, autor, año, tipo_especialidad, 12)
        else:
            nuevo = Libro(titulo, autor, año, "Normal")

        # Guardar
        self.libros.append(nuevo)
        self.guardar()
        logging.info(f"Libro añadido: {titulo}")
        print("Libro guardado con éxito")

    def mostrar(self):
        """Muestra libros y permite realizar una búsqueda parcial"""
        if not self.libros:
            print("\nNo hay libros en la biblioteca.")
            return
        
        print("\n--- BUSCAR LIBROS ---")
        busqueda = input("Buscar título o autor (deja vacío para ver todos): ").strip().lower()
        
        if not busqueda:
            # Mostrar todos
            print(f"\n--- TODOS LOS LIBROS ({len(self.libros)}) ---")
            for i, libro in enumerate(self.libros, 1):
                print(f"{i}. {libro}")
        else:
            # Búsqueda parcial
            encontrados = [l for l in self.libros if busqueda in l.titulo.lower() or busqueda in l.autor.lower()]
            
            if encontrados:
                print(f"\n--- Resultados: {len(encontrados)} ---")
                for i, libro in enumerate(encontrados, 1):
                    print(f"{i}. {libro}")
            else:
                print("No se encontraron coincidencias.")
                logging.info(f"Búsqueda fallida: {busqueda}")

    def modificar(self):
        """Modifica un libro existente"""
        if not self.libros:
            print("\nNo hay libros para modificar.")
            return
        
        print("\n--- MODIFICAR LIBRO ---")
        titulo = input("Título del libro a modificar: ").strip()
        libro = self.buscar_por_titulo(titulo)
        
        if not libro:
            print("Libro no encontrado.")
            return
        
        print(f"\nModificando: {libro}")
        print("(Pulsa Enter para mantener el valor actual)")
        
        # Modificar título
        nuevo_titulo = input(f"Nuevo título [{libro.titulo}]: ").strip()
        if nuevo_titulo:
            libro.titulo = nuevo_titulo
        
        # Modificar autor
        nuevo_autor = input(f"Nuevo autor [{libro.autor}]: ").strip()
        if nuevo_autor:
            libro.autor = nuevo_autor
        
        # Modificar año
        nuevo_año = input(f"Nuevo año [{libro.año}]: ").strip()
        if nuevo_año:
            libro.año = nuevo_año
        
        # Modificar tipo
        nuevo_tipo = input(f"Nuevo tipo [{libro.tipo}]: ").strip()
        if nuevo_tipo:
            libro.tipo = nuevo_tipo
        
        # Si es digital, permitir modificar formato
        if isinstance(libro, LibroDigital):
            nuevo_formato = input(f"Nuevo formato [{libro.formato}]: ").strip()
            if nuevo_formato:
                libro.formato = nuevo_formato
        
        self.guardar()
        logging.info(f"Libro modificado: {libro.titulo}")
        print("Libro modificado correctamente.")

    def eliminar(self):
        """Elimina un libro de la biblioteca"""
        if not self.libros:
            print("\nNo hay libros para eliminar.")
            return
        
        print("\n--- ELIMINAR LIBRO ---")
        titulo = input("Título del libro a eliminar: ").strip()
        libro = self.buscar_por_titulo(titulo)
        
        if not libro:
            print("Libro no encontrado.")
            return
        
        # Confirmar eliminación
        confirmacion = input(f"¿Seguro que quieres eliminar '{libro.titulo}'? (s/n): ").strip().lower()
        if confirmacion == 's':
            self.libros.remove(libro)
            self.guardar()
            logging.info(f"Libro eliminado: {titulo}")
            print("Libro eliminado correctamente.")
        else:
            print("Eliminación cancelada.")