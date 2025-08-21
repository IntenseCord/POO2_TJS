from numero import Numero

class Hexadecimal(Numero):
    def __init__(self, valor):
        super().__init__(valor)

    def a_decimal(self):
        return int(self.valor, 16)

    def a_binario(self):
        return bin(self.a_decimal())[2:]

    def a_octal(self):
        return oct(self.a_decimal())[2:]

    def a_hexadecimal(self):
        return self.valor

    def sumar(self, otro):
        resultado_decimal = self.a_decimal() + otro.a_decimal()
        return Hexadecimal(hex(resultado_decimal)[2:])

    def multiplicar(self, otro):
        resultado_decimal = self.a_decimal() * otro.a_decimal()
        return Hexadecimal(hex(resultado_decimal)[2:])
    
    def convertir(self):
        return self.valor