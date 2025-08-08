from Cuadro import Cuadrado
from Triangulo import Triangulo
from Circulo import Circulo

def main():
    
    cuadrado = Cuadrado(5)
    triangulo = Triangulo(6, 4)
    circulo = Circulo(3)
    
    print("1. CUADRADO:")
    print(cuadrado)
    print(f"   Área calculada: {cuadrado.area()}")
    print()
    
    print("2. TRIÁNGULO:")
    print(triangulo)
    print(f"   Área calculada: {triangulo.area()}")
    print()
    
    print("3. CÍRCULO:")
    print(circulo)
    print(f"   Área calculada: {circulo.area():.2f}")
    print()
    
    figuras = [cuadrado, triangulo, circulo]
    

if __name__ == "__main__":
    main()
