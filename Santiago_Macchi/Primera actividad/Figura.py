class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def sacar_area(self):
        print(f"el area es ??")

    def __str__(self):
        return f"Figura: {self.nombre}"
