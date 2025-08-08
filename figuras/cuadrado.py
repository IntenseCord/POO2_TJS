from figura import Figura

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calculararea(self):
        return self.lado ** 2