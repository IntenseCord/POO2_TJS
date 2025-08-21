from abc import ABC, abstractmethod

class Numero(ABC):
    def __init__(self, valor):
        self.valor = valor

    @abstractmethod
    def a_decimal(self):
        pass

    @abstractmethod
    def a_binario(self):
        pass

    @abstractmethod
    def a_octal(self):
        pass

    @abstractmethod
    def a_hexadecimal(self):
        pass

    @abstractmethod
    def sumar(self, otro):
        pass

    @abstractmethod
    def multiplicar(self, otro):
        pass

    @abstractmethod
    def convertir(self):
        pass