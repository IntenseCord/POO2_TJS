import requests

class DataFetcher:
    """Maneja la conexión a la API y devuelve una lista de registros."""
    def __init__(self, url: str, timeout: int = 8):
        self.url = url
        self.timeout = timeout

    def fetch(self):
        """Intenta obtener datos de la API y devolver una lista de diccionarios."""
        try:
            resp = requests.get(self.url, timeout=self.timeout)
            resp.raise_for_status()
            data = resp.json()
            if isinstance(data, list):
                return data
            if isinstance(data, dict):
                for v in data.values():
                    if isinstance(v, list):
                        return v
            raise ValueError("La respuesta de la API no contiene una lista de registros.")
        except requests.RequestException as e:
            raise ConnectionError(f"Error conectando a la API: {e}") from e
