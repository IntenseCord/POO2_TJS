from forma import forma
class triangulo(forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def sacar_area(self):
        return (self.base * self.altura) / 2
    