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

            # Caso 1: la API ya devuelve lista
            if isinstance(data, list):
                return data

            # Caso 2: es un dict con una lista dentro
            if isinstance(data, dict):
                for v in data.values():
                    if isinstance(v, list):
                        return v

                # Caso especial: API de Coindesk (bpi es un dict)
                if "bpi" in data:
                    return [
                        {"moneda": k, "precio": v["rate_float"]}
                        for k, v in data["bpi"].items()
                    ]

            raise ValueError("La respuesta de la API no contiene una lista de registros.")

        except requests.RequestException as e:
            raise ConnectionError(f"Error conectando a la API: {e}") from e
