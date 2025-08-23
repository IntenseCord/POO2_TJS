# from fabrica import crear_instancia 

# 📦 Importación de clases base y fábrica
#from fabrica import crear_instancia as crear
from bases.decimal import Decimal
from bases.binario import Binario
from bases.hexadecimal import Hexadecimal
from bases.octal import Octal
from bases.romano import Romano

# 🧠 Diccionario de clases y lista de bases disponibles
bases_disponibles = ['decimal', 'binario', 'hexadecimal', 'octal', 'romano']
clases = {
    'decimal': Decimal,
    'binario': Binario,
    'hexadecimal': Hexadecimal,
    'octal': Octal,
    'romano': Romano
}

# 📌 Función para elegir una base desde el menú
def elegir_base(prompt):
    print(prompt)
    for i, base in enumerate(bases_disponibles):
        print(f"{i}. {base}")
    indice = input("Elige el número de la base: ")
    try:
        return bases_disponibles[int(indice)]
    except (ValueError, IndexError):
        raise ValueError("Índice inválido")

# 🛠️ Función para crear una instancia de número en la base seleccionada
def crear(base, valor, validar=True):
    clase = clases.get(base)
    if not clase:
        raise ValueError("Base no soportada")
    instancia = clase(valor)
    if validar and not instancia.validar():
        raise ValueError("Valor inválido para la base seleccionada")
    return instancia

# 🎯 Función principal del programa
def main():
    while True:
        print("\n🧮 Calculadora Numérica Universal")
        print("1. Convertir número entre bases")
        print("2. Sumar dos números")
        print("3. Restar dos números")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '0':
            print("👋 Hasta luego!")
            break

        if opcion not in ['1', '2', '3']:
            print("❌ Opción inválida.")
            continue

        try:
            # Primer número
            base1 = elegir_base("Base del primer número:")
            valor1 = input("Valor del primer número: ")
            num1 = crear(base1, valor1)

            if opcion == '1':
                # Conversión entre bases
                base_destino = elegir_base("¿A qué base quieres convertir?")
                clase_destino = clases[base_destino]
                instancia_temporal = clase_destino("0")  # valor ficticio
                resultado = instancia_temporal.desde_decimal(num1.a_decimal())
                print(f"\n✅ Resultado en {base_destino}: {resultado}")

            else:
                # Segundo número
                base2 = elegir_base("Base del segundo número:")
                valor2 = input("Valor del segundo número: ")
                num2 = crear(base2, valor2)

                if opcion == '2':
                    resultado = num1.sumar(num2)
                else:
                    resultado = num1.restar(num2)

                print(f"\n✅ Resultado en base {base1}: {resultado}")

        except Exception as e:
            print(f"\n❌ Error: {e}")

# 🚀 Punto de entrada
if __name__ == "__main__":
    main()