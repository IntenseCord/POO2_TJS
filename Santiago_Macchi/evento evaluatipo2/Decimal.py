from Numero import Numero

class NumeroDecimal(Numero):
    def __init__(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("El valor debe ser un número decimal")
        super().__init__(valor)
    
    def to_decimal(self):
        return self.valor
    
    def to_binario(self):
        if isinstance(self.valor, float):
            raise ValueError("No se pueden convertir números decimales a binario")
        return bin(int(self.valor))[2:]
    
    def to_octal(self):
        if isinstance(self.valor, float):
            raise ValueError("No se pueden convertir números decimales a octal")
        return oct(int(self.valor))[2:] 
    
    def to_hexadecimal(self):
        if isinstance(self.valor, float):
            raise ValueError("No se pueden convertir números decimales a hexadecimal")
        return hex(int(self.valor))[2:].upper() 
    
    def to_romano(self):
        if isinstance(self.valor, float):
            raise ValueError("No se pueden convertir números decimales a romano")
        
        if self.valor <= 0 or self.valor > 3999:
            raise ValueError("Los números romanos solo van del 1 al 3999")
        
        valores_romanos = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        resultado = ""
        valor_restante = int(self.valor)
        
        for valor, simbolo in valores_romanos:
            while valor_restante >= valor:
                resultado += simbolo
                valor_restante -= valor
        
        return resultado
