from bases.decimal import Decimal
from bases.binario import Binario
from bases.hexadecimal import Hexadecimal
from bases.octal import Octal
from bases.romano import Romano

def crear_instancia(base, valor):
    clases = {
        'decimal': Decimal,
        'binario': Binario,
        'hexadecimal': Hexadecimal,
        'octal': Octal,
        'romano': Romano
    }
    clase = clases.get(base.lower())
    if clase:
        instancia = clase(valor)
        if instancia.validar():
            return instancia
        else:
            raise ValueError(f"Valor inválido para base {base}")
    else:
        raise ValueError(f"Base no soportada: {base}")
