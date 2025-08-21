from decimall import Decimal
from binario import Binario
from octal import Octal
from hexadecimal import Hexadecimal
from romano import Romano

tipos = {
    "d": Decimal,
    "b": Binario,
    "r": Romano,
    "h": Hexadecimal,
    "o": Octal
}

if __name__ == "__main__":
    print("Buen día, ¿qué operación desea realizar?")
    print("Si llegas a ingresar un número en romano, asegúrate que sea en mayúsculas.")
    print("Opciones: decimal (d), binario (b), romano (r), hexadecimal (h), octal (o)")

    tipo1 = input("Primer número: decimal (d), binario (b), romano (r), hexadecimal (h), octal (o) ").lower()
    valor1 = input("Ingrese el valor: ")
    num1 = tipos[tipo1](valor1)

    tipo2 = input("Segundo número decimal (d), binario (b), romano (r), hexadecimal (h), octal (o) : ").lower()
    valor2 = input("Ingrese el valor: ")
    num2 = tipos[tipo2](valor2)

    op = input("¿Suma (s) o multiplicación (m)?: ").lower()

    if op == "s":
        resultado = num1.sumar(num2)
    elif op == "m":
        resultado = num1.multiplicar(num2)
    else:
        print("Operación no válida.")
        exit()

    print("Resultado:", resultado.convertir())