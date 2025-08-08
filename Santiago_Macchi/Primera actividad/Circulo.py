import math
from Figura import Figura

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio
    
    def area(self):
        return math.pi * (self.radio ** 2)
    
    def __str__(self):
        return f"{super().__str__()} - Radio: {self.radio}, Área: {self.area():.2f}"
