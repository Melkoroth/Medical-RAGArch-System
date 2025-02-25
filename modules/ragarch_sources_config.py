import json
import requests

RAGARCH_API_URL = "https://ragarch-instance.com/api/get_sources"

def get_sources(region=None):
    """Obtiene la jerarquización de fuentes desde RAGArch."""
    params = {"region": region} if region else {}
    response = requests.get(RAGARCH_API_URL, params=params)
    return response.json() if response.status_code == 200 else {"error": "No se pudo obtener las fuentes"}

if __name__ == "__main__":
    print(get_sources("Europa"))
