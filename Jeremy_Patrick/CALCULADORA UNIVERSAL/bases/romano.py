from bases.base import BaseNumerica

class Romano(BaseNumerica):
    simbolos = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}

    def validar(self):
        try:
            self.a_decimal()
            return True
        except:
            return False

    def a_decimal(self):
        total = 0
        prev = 0
        for c in reversed(self.valor.upper()):
            val = self.simbolos[c]
            if val < prev:
                total -= val
            else:
                total += val
                prev = val
        return total

    def desde_decimal(self, valor_decimal):
        valores = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        resultado = ''
        for val, simbolo in valores:
            while valor_decimal >= val:
                resultado += simbolo
                valor_decimal -= val
        return resultado
