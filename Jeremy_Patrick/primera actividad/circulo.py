from forma import forma
import math
class circulo (forma):
    def __init__(self,radio):
        self.radio=radio

    def sacar_area(self):
        return math.pi * (self.radio ** 2)

    