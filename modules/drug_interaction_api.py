import requests

DRUGS_API_URL = "https://api.drugs.com/interactions"
MEDLINEPLUS_API_URL = "https://medlineplus.gov/druginfo"

def check_interaction(medication_1, medication_2):
    """Consulta interacciones entre dos medicamentos en ambas APIs."""
    drugs_response = requests.get(f"{DRUGS_API_URL}?drug1={medication_1}&drug2={medication_2}")
    medline_response = requests.get(f"{MEDLINEPLUS_API_URL}?query={medication_1}+{medication_2}")

    drugs_result = drugs_response.json() if drugs_response.status_code == 200 else {}
    medline_result = medline_response.json() if medline_response.status_code == 200 else {}

    return {"Drugs.com": drugs_result, "MedlinePlus": medline_result}

if __name__ == "__main__":
    print(check_interaction("Metformina", "Vitamina B12"))
