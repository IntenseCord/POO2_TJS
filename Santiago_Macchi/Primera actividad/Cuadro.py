from Figura import Figura

class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.lado = lado
    
    def area(self):
        return self.lado ** 2
    
    def __str__(self):
        return f"{super().__str__()} - Lado: {self.lado}, Área: {self.area()}"
