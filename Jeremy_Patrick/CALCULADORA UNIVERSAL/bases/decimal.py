from bases.base import BaseNumerica

class Decimal(BaseNumerica):
    def validar(self):
        return self.valor.isdigit()

    def a_decimal(self):
        return int(self.valor)

    def desde_decimal(self, valor_decimal):
        return str(valor_decimal)
