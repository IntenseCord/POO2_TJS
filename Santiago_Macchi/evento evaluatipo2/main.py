from API_Numeros import API_Numeros

def mostrar_menu():
    print("\n" + "="*60)
    print("           SISTEMA DE NÚMEROS MULTIBASE")
    print("="*60)
    print("1. Mostrar conversiones de un número")
    print("2. Sumar dos números")
    print("3. Multiplicar dos números")
    print("4. Ver tipos de números disponibles")
    print("5. Salir")
    print("="*60)

def obtener_tipo_numero():
    print("\nTipos disponibles:")
    tipos = ['decimal', 'binario', 'octal', 'hexadecimal', 'romano']
    for i, tipo in enumerate(tipos, 1):
        print(f"{i}. {tipo.upper()}")
    
    while True:
        try:
            opcion = int(input("\nSeleccione el tipo de número (1-5): "))
            if 1 <= opcion <= 5:
                return tipos[opcion - 1]
            else:
                print("Opción no válida. Seleccione del 1 al 5.")
        except ValueError:
            print("Por favor ingrese un número válido.")

def obtener_valor_numero(tipo):
    print(f"\nIngrese el valor para el número {tipo.upper()}:")
    
    if tipo == 'decimal':
        print("Ejemplos: 42, 100, 255")
        return int(input("Valor decimal: "))
    
    elif tipo == 'binario':
        print("Ejemplos: 1010, 1100, 11111111")
        return input("Valor binario: ")
    
    elif tipo == 'octal':
        print("Ejemplos: 52, 144, 377")
        return input("Valor octal: ")
    
    elif tipo == 'hexadecimal':
        print("Ejemplos: 2A, 64, FF")
        return input("Valor hexadecimal: ")
    
    elif tipo == 'romano':
        print("Ejemplos: IV, X, CCL")
        return input("Valor romano: ")

def mostrar_conversiones(api):
    print("\n--- MOSTRAR CONVERSIONES ---")
    
    tipo = obtener_tipo_numero()
    valor = obtener_valor_numero(tipo)
    
    try:
        numero = api.crear_numero(tipo, valor)
        print(f"\n🔄 Conversiones del número {numero}:")
        
        print(f"{'Decimal':12}: {numero.to_decimal()}")
        print(f"{'Binario':12}: {numero.to_binario()}")
        print(f"{'Octal':12}: {numero.to_octal()}")
        print(f"{'Hexadecimal':12}: {numero.to_hexadecimal()}")
        
        try:
            romano = numero.to_romano()
            print(f"{'Romano':12}: {romano}")
        except ValueError as e:
            print(f"{'Romano':12}: ❌ {e}")
            
    except ValueError as e:
        print(f"❌ Error: {e}")

def operacion_numeros(api, operacion):
    print(f"\n--- {operacion.upper()} NÚMEROS ---")
    
    print(f"\nPrimer número:")
    tipo1 = obtener_tipo_numero()
    valor1 = obtener_valor_numero(tipo1)
    
    try:
        num1 = api.crear_numero(tipo1, valor1)
    except ValueError as e:
        print(f"❌ Error en el primer número: {e}")
        return
    
    print(f"\nSegundo número:")
    tipo2 = obtener_tipo_numero()
    valor2 = obtener_valor_numero(tipo2)
    
    try:
        num2 = api.crear_numero(tipo2, valor2)
    except ValueError as e:
        print(f"❌ Error en el segundo número: {e}")
        return
    
    try:
        if operacion == "sumar":
            resultado = api.sumar_numeros(num1, num2)
            print(f"\n➕ Resultado de la suma:")
        else:
            resultado = api.multiplicar_numeros(num1, num2)
            print(f"\n✖️  Resultado de la multiplicación:")
        
        print(f"Resultado en decimal: {resultado.to_decimal()}")
        print(f"Resultado en binario: {resultado.to_binario()}")
        print(f"Resultado en octal: {resultado.to_octal()}")
        print(f"Resultado en hexadecimal: {resultado.to_hexadecimal()}")
        print(f"Resultado en romano: {resultado.to_romano()}")
        
    except Exception as e:
        print(f"❌ Error en la operación: {e}")

def ver_tipos_disponibles(api):
    print("\n--- TIPOS DE NÚMEROS DISPONIBLES ---")
    tipos = api.obtener_tipos_disponibles()
    
    print("El sistema soporta los siguientes tipos de números:")
    for i, tipo in enumerate(tipos, 1):
        print(f"{i}. {tipo.upper()}")
    
    print("\nCaracterísticas:")
    print("• Decimal: Números enteros y decimales (ej: 42, 3.14)")
    print("• Binario: Números en base 2 (ej: 1010, 1100)")
    print("• Octal: Números en base 8 (ej: 52, 144)")
    print("• Hexadecimal: Números en base 16 (ej: 2A, FF)")
    print("• Romano: Números romanos del I al MMMCMXCIX")

def main():
    api = API_Numeros()
    
    print("¡Bienvenido al Sistema de Números Multibase!")
    print("Este sistema permite trabajar con diferentes tipos de números")
    print("y realizar operaciones matemáticas entre ellos.")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\nSeleccione una opción (1-5): ").strip()
            
            if opcion == '1':
                mostrar_conversiones(api)
            
            elif opcion == '2':
                operacion_numeros(api, "sumar")
            
            elif opcion == '3':
                operacion_numeros(api, "multiplicar")
            
            elif opcion == '4':
                ver_tipos_disponibles(api)
            
            elif opcion == '5':
                print("\n👋 ¡Gracias por usar el Sistema de Números Multibase!")
                print("¡Hasta luego!")
                break
            
            else:
                print("❌ Opción no válida. Por favor seleccione del 1 al 5.")
        
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
