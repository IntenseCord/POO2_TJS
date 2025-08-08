
import math
from cuadrado import Cuadrado
from triangulo import Triangulo
from circulo import Circulo

cuadrado1 = Cuadrado(4)
triangulo1 = Triangulo(3, 4)
circulo1 = Circulo(math.sqrt(16 / math.pi))

print("El área del cuadrado es:", cuadrado1.calculararea())
print("El área del triángulo es:", triangulo1.calculararea())
print("El área del círculo es:", circulo1.calculararea())