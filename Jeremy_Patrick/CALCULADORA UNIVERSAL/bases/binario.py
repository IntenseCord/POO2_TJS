from bases.base import BaseNumerica

class Binario(BaseNumerica):
    def validar(self):
        return all(c in '01' for c in self.valor)

    def a_decimal(self):
        return int(self.valor, 2)

    def desde_decimal(self, valor_decimal):
        return bin(valor_decimal)[2:]
