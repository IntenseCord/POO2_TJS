# utils/exceptions.py

class APIError(Exception):
    """Error general al interactuar con la API."""
    pass


class DataFormatError(Exception):
    """La respuesta de la API no tiene el formato esperado."""
    pass


class SortingError(Exception):
    """Error relacionado con los algoritmos de ordenamiento."""
    pass
