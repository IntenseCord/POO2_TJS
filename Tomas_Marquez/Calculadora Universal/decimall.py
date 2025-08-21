from numero import Numero

class Decimal(Numero):
    def __init__(self, valor):
        super().__init__(int(valor))

    def a_decimal(self):
        return self.valor

    def a_binario(self):
        return bin(self.valor)[2:]

    def a_octal(self):
        return oct(self.valor)[2:]

    def a_hexadecimal(self):
        return hex(self.valor)[2:]

    def sumar(self, otro):
        resultado_decimal = self.a_decimal() + otro.a_decimal()
        return Decimal(str(resultado_decimal))

    def multiplicar(self, otro):
        resultado_decimal = self.a_decimal() * otro.a_decimal()
        return Decimal(str(resultado_decimal))
    
    def convertir(self):
        return str(self.valor)