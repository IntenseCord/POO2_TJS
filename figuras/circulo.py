
from figura import Figura
import math

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calculararea(self):
        return math.pi * (self.radio ** 2)