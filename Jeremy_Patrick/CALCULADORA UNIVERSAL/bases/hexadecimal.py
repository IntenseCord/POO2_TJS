from bases.base import BaseNumerica

class Hexadecimal(BaseNumerica):
    def validar(self):
        try:
            int(self.valor, 16)
            return True
        except ValueError:
            return False

    def a_decimal(self):
        return int(self.valor, 16)

    def desde_decimal(self, valor_decimal):
        return hex(valor_decimal)[2:].upper()
