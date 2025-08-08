from circulo import circulo 
from triangulo import triangulo
from cuadro import cuadro

cuadr = cuadro(65)
cir = circulo(48)
tri= triangulo(23,654)

print(f"las areas son: \n cuadrado: {cuadr.sacar_area()} \n circulo: {cir.sacar_area()} \n triangulo: {tri.sacar_area()}")
