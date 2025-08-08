from Figura import Figura

class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Triángulo")
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura) / 2
    
    def __str__(self):
        return f"{super().__str__()} - Base: {self.base}, Altura: {self.altura}, Área: {self.area()}"
