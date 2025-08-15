from Numero import Numero

class NumeroBinario(Numero):
    def __init__(self, valor):
        if isinstance(valor, str):
            if not all(bit in '01' for bit in valor):
                raise ValueError("El valor debe ser una cadena binaria válida (solo 0s y 1s)")
            self.valor = valor
        elif isinstance(valor, int):
            if valor < 0:
                raise ValueError("No se permiten números negativos en binario")
            self.valor = bin(valor)[2:]
        else:
            raise ValueError("El valor debe ser una cadena binaria o un entero")
    
    def to_decimal(self):
        return int(self.valor, 2)
    
    def to_binario(self):
        return self.valor
    
    def to_octal(self):
        decimal = self.to_decimal()
        return oct(decimal)[2:]  
    
    def to_hexadecimal(self):
        decimal = self.to_decimal()
        return hex(decimal)[2:].upper()  
    
    def to_romano(self):
        decimal = self.to_decimal()
        if decimal <= 0 or decimal > 3999:
            raise ValueError("Los números romanos solo van del 1 al 3999")
        
        valores_romanos = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        resultado = ""
        valor_restante = decimal
        
        for valor, simbolo in valores_romanos:
            while valor_restante >= valor:
                resultado += simbolo
                valor_restante -= valor
        
        return resultado
