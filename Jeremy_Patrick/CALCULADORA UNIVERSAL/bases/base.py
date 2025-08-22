from abc import ABC, abstractmethod #significa que es obligario implementar los metodos  en los hijos


class BaseNumerica(ABC):
    def __init__(self, valor):
        self.valor = valor

    @abstractmethod
    def validar(self): pass

    @abstractmethod
    def a_decimal(self): pass

    @abstractmethod
    def desde_decimal(self, valor_decimal): pass

    def sumar(self, otro):
        resultado = self.a_decimal() + otro.a_decimal()
        return self.desde_decimal(resultado)

    def restar(self, otro):
        resultado = self.a_decimal() - otro.a_decimal()
        return self.desde_decimal(resultado)
