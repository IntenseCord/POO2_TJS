from Numero import Numero

class NumeroRomano(Numero):
    def __init__(self, valor):
        if isinstance(valor, str):
            valor_upper = valor.upper()
            if not self._es_romano_valido(valor_upper):
                raise ValueError("El valor debe ser un número romano válido")
            self.valor = valor_upper
        elif isinstance(valor, int):
            if valor <= 0 or valor > 3999:
                raise ValueError("Los números romanos solo van del 1 al 3999")
            self.valor = self._decimal_a_romano(valor)
        else:
            raise ValueError("El valor debe ser una cadena romana o un entero")
    
    def _es_romano_valido(self, romano):
        simbolos_validos = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
        
        if not all(simbolo in simbolos_validos for simbolo in romano):
            return False
        
        for simbolo in 'VLD':
            if romano.count(simbolo) > 1:
                return False
        
        for simbolo in 'IXCM':
            if romano.count(simbolo) > 3:
                return False
        
        return True
    
    def _decimal_a_romano(self, decimal):
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
    
    def _romano_a_decimal(self, romano):
        valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        resultado = 0
        anterior = 0
        
        for simbolo in reversed(romano):
            valor_actual = valores[simbolo]
            if valor_actual >= anterior:
                resultado += valor_actual
            else:
                resultado -= valor_actual
            anterior = valor_actual
        
        return resultado
    
    def to_decimal(self):
        return self._romano_a_decimal(self.valor)
    
    def to_binario(self):
        decimal = self.to_decimal()
        return bin(decimal)[2:] 
    
    def to_octal(self):
        decimal = self.to_decimal()
        return oct(decimal)[2:]
    
    def to_hexadecimal(self):
        decimal = self.to_decimal()
        return hex(decimal)[2:].upper()
    
    def to_romano(self):
        return self.valor
