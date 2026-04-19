import json

class Libro: 
    def __init__(self, titulo, autor, año, tipo):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.tipo = tipo

    def __str__(self):
        return f"{self.titulo} ({self.año}) - {self.autor}"
    
    def to_dict(self):
        """Convierte el objeto a diccionario para JSON"""
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "año": self.año,
            "tipo": self.tipo
        }
    
    @classmethod
    def from_dict(cls, data):
        """Crea un objeto Libro desde un diccionario"""
        return cls(
            data["titulo"],
            data["autor"],
            data["año"],
            data["tipo"]
        )
    
class LibroDigital(Libro):
    def __init__(self, titulo, autor, año, tipo, formato):
        super().__init__(titulo, autor, año, tipo)
        self.formato = formato
        
    def __str__(self):
        return f"[DIGITAL] {self.titulo} ({self.año}) - {self.autor} - Formato: {self.formato}"
    
    def to_dict(self):
        """Convierte LibroDigital a diccionario, incluyendo formato"""
        d = super().to_dict()
        d.update({"tipo": "digital", "formato": self.formato})
        return d
    

class LibroEspecial(Libro):
    def __init__(self, titulo, autor, año, tipo, descuento_vip):
        super().__init__(titulo, autor, año, tipo)
        self.descuento_vip = descuento_vip

    def __str__(self):
        return f"[LIBRO ESPECIAL] {self.titulo} ({self.año}) - {self.autor} - {self.tipo} - DESCUENTO POR VIP: {self.descuento_vip}"
    
    