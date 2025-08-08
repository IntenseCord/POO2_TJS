from forma import forma
class cuadro(forma):
    def __init__ (self,lado):
        
        self.lado=lado

    def sacar_area(self):
        return self.lado ** 2
    