from numero import Numero

class Romano(Numero):
    def __init__(self, valor):
        super().__init__(valor)
        self.ROMANOS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        self.ROMANOS = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
        self.VALORES = sorted(self.ROMANOS.values(), reverse=True)
        self.SIMBOLOS = {v: k for k, v in self.ROMANOS.items()}

    def a_decimal(self):
        decimal = 0
        i = 0
        while i < len(self.valor):
            simbolo_actual = self.valor[i]
            valor_actual = self.ROMANOS[simbolo_actual]
            if i + 1 < len(self.valor):
                valor_siguiente = self.ROMANOS[self.valor[i + 1]]
                if valor_siguiente > valor_actual:
                    decimal += valor_siguiente - valor_actual
                    i += 2
                else:
                    decimal += valor_actual
                    i += 1
            else:
                decimal += valor_actual
                i += 1
        return decimal

    def a_binario(self):
        return bin(self.a_decimal())[2:]

    def a_octal(self):
        return oct(self.a_decimal())[2:]

    def a_hexadecimal(self):
        return hex(self.a_decimal())[2:]
        
    def a_romano(self, numero_decimal):
        if not isinstance(numero_decimal, int) or numero_decimal <= 0 or numero_decimal > 3999:
            raise ValueError("El número debe ser un entero positivo menor a 4000.")
        
        romano = ''
        for valor in self.VALORES:
            while numero_decimal >= valor:
                romano += self.SIMBOLOS[valor]
                numero_decimal -= valor
                
        # Manejo de casos especiales (resta)
        romano = romano.replace("IIII", "IV").replace("VIIII", "IX")
        romano = romano.replace("XXXX", "XL").replace("LXXXX", "XC")
        romano = romano.replace("CCCC", "CD").replace("DCCCC", "CM")
        return romano

    def sumar(self, otro):
        resultado_decimal = self.a_decimal() + otro.a_decimal()
        return Romano(self.a_romano(resultado_decimal))

    def multiplicar(self, otro):
        resultado_decimal = self.a_decimal() * otro.a_decimal()
        return Romano(self.a_romano(resultado_decimal))
    
    def convertir(self):
        return self.valor