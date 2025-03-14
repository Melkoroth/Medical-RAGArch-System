import json
import requests
import os

RAGARCH_API_URL = "https://ragarch-instance.com/api/get_sources"

def get_sources(region=None):
    """Obtiene la jerarquización de fuentes desde RAGArch."""
    API_KEY = os.getenv("RAGARCH_API_KEY")
    if not API_KEY:
        raise ValueError("API Key de RAGArch no configurada en las variables de entorno.")
    
    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {"region": region} if region else {}

# ✅ Se ha agregado validación de parámetros para evitar riesgos de inyección
if not is_valid_api_request(params):
    raise ValueError('Solicitud API rechazada por contener parámetros inseguros')
    response = requests.get(RAGARCH_API_URL, params=params, headers=headers)
    return response.json() if response.status_code == 200 else {"error": "No se pudo obtener las fuentes"}

if __name__ == "__main__":
    print(get_sources("Europa"))
