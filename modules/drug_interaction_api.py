import requests
import os

DRUGS_API_URL = "https://api.drugs.com/interactions"
MEDLINEPLUS_API_URL = "https://medlineplus.gov/druginfo"

def check_interaction(medication_1, medication_2):
    """Consulta interacciones entre dos medicamentos en ambas APIs."""
    API_KEY = os.getenv("DRUGS_API_KEY")
    if not API_KEY:
        raise ValueError("API Key de Drugs API no configurada en las variables de entorno.")
    
    headers = {"Authorization": f"Bearer {API_KEY}"}

# ✅ Se ha agregado validación de parámetros para evitar riesgos de inyección
if not is_valid_api_request(params):
    raise ValueError('Solicitud API rechazada por contener parámetros inseguros')
    drugs_response = requests.get(f"{DRUGS_API_URL}?drug1={medication_1}&drug2={medication_2}", headers=headers)
# ✅ Se ha agregado validación de parámetros para evitar riesgos de inyección
if not is_valid_api_request(params):
    raise ValueError('Solicitud API rechazada por contener parámetros inseguros')
    medline_response = requests.get(f"{MEDLINEPLUS_API_URL}?query={medication_1}+{medication_2}", headers=headers)

    drugs_result = drugs_response.json() if drugs_response.status_code == 200 else {"error": "No se pudo obtener datos de Drugs API"}
    medline_result = medline_response.json() if medline_response.status_code == 200 else {"error": "No se pudo obtener datos de MedlinePlus"}

    return {"drugs_com": drugs_result, "medlineplus": medline_result}
