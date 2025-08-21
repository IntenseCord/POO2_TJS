from numero import Numero

class Binario(Numero):
    def __init__(self, valor):
        super().__init__(valor)

    def a_decimal(self):
        return int(self.valor, 2)

    def a_binario(self):
        return self.valor

    def a_octal(self):
        return oct(self.a_decimal())[2:]

    def a_hexadecimal(self):
        return hex(self.a_decimal())[2:]

    def sumar(self, otro):
        resultado_decimal = self.a_decimal() + otro.a_decimal()
        return Binario(bin(resultado_decimal)[2:])

    def multiplicar(self, otro):
        resultado_decimal = self.a_decimal() * otro.a_decimal()
        return Binario(bin(resultado_decimal)[2:])
    
    def convertir(self):
        return self.valor