from figura import Figura

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calculararea(self):
        return (self.base * self.altura) / 2