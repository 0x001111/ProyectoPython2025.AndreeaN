import json

class Libro: 
    def __init__(self, titulo, autor, año, tipo, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.tipo = tipo
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.titulo} ({self.año}) - {self.autor} - {self.cantidad}"
    
    def to_dict(self):
        """Convierte el objeto a diccionario para JSON"""
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "año": self.año,
            "tipo": self.tipo,
            "cantidad": self.cantidad
        }
    
    @classmethod
    def from_dict(cls, data):
        """Crea un objeto Libro desde un diccionario"""
        return cls(
            data["titulo"],
            data["autor"],
            data["año"],
            data["tipo"],
            data["cantidad"]
        )
    
class LibroDigital(Libro):
    def __init__(self, titulo, autor, año, tipo, formato, cantidad):
        super().__init__(titulo, autor, año, tipo, cantidad)
        self.formato = formato
        
    def __str__(self):
        return f"[DIGITAL] {self.titulo} ({self.año}) - {self.autor} - Formato: {self.formato} - CANTIDAD: {self.cantidad}"
    
    def to_dict(self):
        """Convierte LibroDigital a diccionario, incluyendo formato"""
        d = super().to_dict()
        d.update({"tipo": "digital", 
                  "formato": self.formato, 
                  "stock":self.cantidad
                  })
        return d
    

class LibroEspecial(Libro):
    def __init__(self, titulo, autor, año, tipo, descuento_vip, cantidad):
        super().__init__(titulo, autor, año, tipo, cantidad)
        self.descuento_vip = descuento_vip

    def __str__(self):
        return f"[LIBRO ESPECIAL] {self.titulo} ({self.año}) - {self.autor} - {self.tipo} - DESCUENTO POR VIP: {self.descuento_vip} - STOCK: {self.cantidad}"
    
    