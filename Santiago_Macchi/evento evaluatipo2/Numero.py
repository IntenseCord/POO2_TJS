from abc import ABC, abstractmethod

class Numero(ABC):
    def __init__(self, valor):
        self.valor = valor
    
    @abstractmethod
    def to_decimal(self):
        pass
    
    @abstractmethod
    def to_binario(self):
        pass
    
    @abstractmethod
    def to_octal(self):
        pass
    
    @abstractmethod
    def to_hexadecimal(self):
        pass
    
    @abstractmethod
    def to_romano(self):
        pass
    
    def __add__(self, other):
        if isinstance(other, Numero):
            resultado_decimal = self.to_decimal() + other.to_decimal()
            from Decimal import NumeroDecimal
            return NumeroDecimal(resultado_decimal)
        else:
            raise TypeError("Solo se pueden sumar objetos de tipo Numero")
    
    def __mul__(self, other):
        if isinstance(other, Numero):
            resultado_decimal = self.to_decimal() * other.to_decimal()
            from Decimal import NumeroDecimal
            return NumeroDecimal(resultado_decimal)
        else:
            raise TypeError("Solo se pueden multiplicar objetos de tipo Numero")
    
    def __str__(self):
        return f"{self.__class__.__name__}({self.valor})"
    
    def __repr__(self):
        return self.__str__()
