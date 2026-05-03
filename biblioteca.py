import json
import logging
from datetime import datetime
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
        """Carga los libros detectando si el formato es antiguo (lista) o nuevo (dict)"""
        try:
            with open(self.FICHERO, "r", encoding="utf-8") as f:
                contenido = json.load(f)
                
                # Comprobamos: ¿Es el formato nuevo (diccionario) o el viejo (lista)?
                if isinstance(contenido, dict):
                    datos = contenido.get("items", [])
                else:
                    # Es una lista (formato viejo), la usamos directamente
                    datos = contenido
                
                self.libros = []
                for d in datos:
                    # Estructura: [0]tit, [1]aut, [2]año, [3]tipo, [4]cant, [5]extra
                    fila = [
                        d.get("titulo", "Sin título"),
                        d.get("autor", "Anónimo"),
                        d.get("año", "N/A"),
                        d.get("tipo", "Normal"),
                        d.get("cantidad", 1),
                        d.get("formato") or d.get("especialidad") or d.get("descuento_vip") or ""
                    ]
                    self.libros.append(fila)
                logging.info("Carga completada con éxito.")
        except (FileNotFoundError, json.JSONDecodeError):
            self.libros = []

    def guardar(self):
        """Guarda los libros con metadatos globales de fecha"""
        try:
            ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            lista_para_guardar = []
            for l in self.libros:
                info = {
                    "titulo": l[0], "autor": l[1], "año": l[2],
                    "tipo": l[3], "cantidad": l[4]
                }
                if l[3] == "digital": info["formato"] = l[5]
                elif l[3] == "especial": info["especialidad"] = l[5]
                lista_para_guardar.append(info)

            raiz = {"items": lista_para_guardar, "fecha_ultimo_guardado": ahora}
            with open(self.FICHERO, "w", encoding="utf-8") as f:
                json.dump(raiz, f, indent=4, ensure_ascii=False)
        except Exception as e:
            logging.error(f"Error al guardar: {e}")

    #----------------------------LOGICA----------------------------

    #CALCULAR INVERSION TOTAL DE CADA TIPO DE LIBRO QUE HAYA EN LA BIBLIOTECA

    def calcular_inversion(self):

        total = 0

        salida = input("A que tipo de libro quieres ver la inversion total?").lower()

        for fila in self.libros: 
            if salida == fila[3].lower():
                total+= int(fila[4]) * 50

        print(f"total: {total}")

    #MOSTRAR LIBROS ORDENADOS POR TITULO CON UNA FUNCION LAMBDA Y BUSQUEDA PARCIAL

    def mostrar(self):
        print("---LISTADO COMPLETO DE LIBROS---")
        for fila in self.libros:
            print(f"Titulo: {fila[0]} - Autor: {fila[1]}")
            

        """Búsqueda parcial trabajando con ARREGLOS"""
        busqueda = input("\nBuscar: ").lower().strip()
        # f[0] es título, f[1] es autor
        encontrados = []
        for f in self.libros:
            if busqueda in f[0].lower():
                encontrados.append(f)

        if encontrados:
            for indice, fila in enumerate(encontrados, 1):
                print(f"{indice}. {fila[0]} - {fila[1]} (Stock: {fila[4]})")
        else:
            print("Sin resultados.")

        #Ordenar los libros por titulo
        libros_ordenados_por_titulo = sorted(encontrados, key=lambda x:x[0].lower()) #sorted crea un copia, .sort(), no. 

        print(f"---LIBROS ORDENADOS POR TITULO---")
        for libro in libros_ordenados_por_titulo:
            print(f"Titulo: {libro[0]} - Autor: {libro[1]}")
        

    #BUSQUEDA DE AUTORES SIN REPETIR MEDIANTE HASHSET
    def autores_sin_repetir(self):
        autores = set()

        
        for fila in self.libros: 
            autores.add(fila[1])

        if autores:
            print('---lista de autores sin repetir---')
            for autor in sorted(autores):
                print(f"- {autor}")


    #ENCONTRAR TITULOS MEDIANTE BUSQUEDA PARCIAL

    def buscar_por_titulo(self, titulo):
        """Devuelve la FILA (arreglo) si lo encuentra"""
        busqueda = titulo.lower().strip()
        for fila in self.libros:
            if fila[0].lower().strip() == busqueda:
                return fila
        return None

    #GENERAR UN REPORTE GENERAL DEL INVENTARIO DE LIBROS
    def generar_reporte(self):
        """Convierte ARREGLOS a OBJETOS para imprimir usando las clases"""
        print("\n--- REPORTE DE INVENTARIO ---")
        total_stock = 0

        cant_digitales = 0 
        cant_especiales = 0
        cant_normales = 0

        for fila in self.libros: 
            
            total_stock += fila[4]
            objeto = None

            if fila[3].lower() == "normal":
                objeto = Libro(fila[0], fila[1], fila[2], fila[3], fila[4])
                cant_normales+=fila[4]

            elif fila[3].lower() == "digital":
                objeto = LibroDigital(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
                cant_digitales += fila[4]
            
            elif fila[3].lower() == "especial":
                objeto = LibroEspecial(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
                cant_especiales += fila[4]

            if objeto:
                print(objeto)

        ##IMPRIMIR POR PANTALLA 
        print(f"Total stock de libros: {total_stock}")
        print(f"Total de libros digitales: {cant_digitales}")
        print(f"Total de libros especiales: {cant_especiales}")
        print(f"Total de libros normales {cant_normales}")
        

    #INSERTAR LIBRO
    def insertar(self):
        """Añade o actualiza stock"""
        print("\n--- AÑADIR/ACTUALIZAR ---")
        titulo = input("Título: ").strip()
        if not titulo: return

        encontrado = self.buscar_por_titulo(titulo)
        if encontrado:
            print(f"Ya existe. Stock actual: {encontrado[4]}")
            while True:
                try:
                    suma = int(input('Cuantos sumamos?'))
                    if suma < 0:
                        print('introduce un numero positivo')
                    else:
                        encontrado[4]+=suma 
                        break
                except ValueError:
                    print('error, debes introducir un numero entero')
        else:
            autor = input("Autor: ")
            
            #validacion del año
            while True:
                try:
                    año_ingresado = int(input("Año: ")) 
                    if año_ingresado > 2026:
                        print("Introduce un año valido")
                    elif año_ingresado < 0 :
                        print("Introduce un año mayor que cero")
                    else:
                        año = año_ingresado
                        break
                except ValueError:
                    print(f"Introduce un año valido")


            try: 
                cant = int(input("Cantidad: "))
            except ValueError: 
                cant = 1
                
            print("1.Normal | 2.Digital | 3.Especial")

            opc = input("Tipo: ")
            if opc == "2":
                tipo = "digital"
                extra = input("Formato:")
            elif opc == "3":
                tipo = "especial"
                extra = input("Especialidad:")
            else:
                tipo = "normal"
                extra = "" #le asigno ningun extra al normal

            self.libros.append([titulo, autor, año, tipo, cant, extra])
            
        self.guardar()

    #MODIFICAR LIBRO

    def modificar(self):
        """Modifica un ARREGLO/ARRAY"""
        titulo = input("\nTítulo a modificar: ")
        fila = self.buscar_por_titulo(titulo)
        if not fila:
            print("No encontrado."); return

        print(f"Editando {fila[0]}. Enter para mantener valor.")
        nuevo_tit = input(f"Título [{fila[0]}]: ")
        if nuevo_tit: 
            fila[0] = nuevo_tit
        
        nuevo_aut = input(f"Autor [{fila[1]}]: ")
        if nuevo_aut: 
            fila[1] = nuevo_aut
        
        # El índice [4] es la cantidad
        try:
            nueva_cant = input(f"Cantidad [{fila[4]}]: ")
            if nueva_cant: fila[4] = int(nueva_cant)
        except ValueError: print("Cantidad no cambiada.")

        self.guardar()

    def eliminar(self):
        """Elimina la fila de la lista"""
        titulo = input("\nTítulo a eliminar: ")
        fila = self.buscar_por_titulo(titulo)
        if fila:
            self.libros.remove(fila)
            self.guardar()
            print("Eliminado.")



# Objetos


    def generar_reporte_obj(self):
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

# cargar y guardar con objetos

    def cargar_obj(self):
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

    def guardar_obj(self):
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