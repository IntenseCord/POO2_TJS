from bases.base import BaseNumerica

class Octal(BaseNumerica):
    def validar(self):
        try:
            int(self.valor, 8)
            return True
        except ValueError:
            return False

    def a_decimal(self):
        return int(self.valor, 8)

    def desde_decimal(self, valor_decimal):
        return oct(valor_decimal)[2:]
