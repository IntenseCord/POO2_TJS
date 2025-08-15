from Numero import Numero
from Decimal import NumeroDecimal
from Binario import NumeroBinario
from Octal import NumeroOctal
from Hexadecimal import NumeroHexadecimal
from Romanos import NumeroRomano

class API_Numeros:
    
    def __init__(self):
        self.tipos_disponibles = {
            'decimal': NumeroDecimal,
            'binario': NumeroBinario,
            'octal': NumeroOctal,
            'hexadecimal': NumeroHexadecimal,
            'romano': NumeroRomano
        }
    
    def crear_numero(self, tipo, valor):
        if tipo not in self.tipos_disponibles:
            raise ValueError(f"Tipo no válido. Tipos disponibles: {', '.join(self.tipos_disponibles.keys())}")
        
        try:
            return self.tipos_disponibles[tipo](valor)
        except Exception as e:
            raise ValueError(f"Error al crear número {tipo}: {str(e)}")
    
    def mostrar_conversiones(self, numero):
        """
        Muestra todas las conversiones posibles de un número.
        
        Args:
            numero (Numero): Número a convertir
            
        Returns:
            dict: Diccionario con todas las conversiones
        """
        if not isinstance(numero, Numero):
            raise TypeError("El parámetro debe ser un objeto Numero")
        
        return {
            'Decimal': numero.to_decimal(),
            'Binario': numero.to_binario(),
            'Octal': numero.to_octal(),
            'Hexadecimal': numero.to_hexadecimal(),
            'Romano': numero.to_romano()
        }
    
    def sumar_numeros(self, num1, num2):
        if not isinstance(num1, Numero) or not isinstance(num2, Numero):
            raise TypeError("Ambos parámetros deben ser objetos Numero")
        
        return num1 + num2
    
    def multiplicar_numeros(self, num1, num2):
        if not isinstance(num1, Numero) or not isinstance(num2, Numero):
            raise TypeError("Ambos parámetros deben ser objetos Numero")
        
        return num1 * num2
    
    def obtener_tipos_disponibles(self):
        return list(self.tipos_disponibles.keys())
    
    def validar_tipo(self, tipo):
        return tipo in self.tipos_disponibles
