import requests

BACKEND_URL = "https://localhost:8000"

def get_filtered_biomarkers(document_type: str = "analitica", limit: int = 3, 
                            include_complementary: bool = False, include_in_range: bool = False):
    """
    Recupera documentos y extrae biomarcadores en base a los parámetros solicitados.
    - `document_type`: Tipo de documento a recuperar (analítica, diagnóstico, informe, etc.).
    - `limit`: Número de documentos a obtener.
    - `include_complementary`: Si es True, añade biomarcadores adicionales.
    - `include_in_range`: Si es True, añade biomarcadores en rango normal.
    """

    # Obtener documentos desde el backend
    response = requests.get(f"{BACKEND_URL}/retrieve_documents/", params={"document_type": document_type, "limit": limit})
    documents = response.json().get("documents", [])

    # Enviar documentos para análisis de biomarcadores
    analyzed_response = requests.post(
        f"{BACKEND_URL}/analyze_biomarkers/", 
        json={"documents": documents, "include_complementary": include_complementary, "include_in_range": include_in_range}
    )
    analyzed_data = analyzed_response.json().get("analyzed_data", [])

    return analyzed_data

def send_to_chatgpt(prompt: str, biomarkers: list, include_complementary: bool = False, include_in_range: bool = False):
    """
    Envía a ChatGPT los biomarcadores seleccionados según la solicitud del usuario.
    - `include_complementary`: Si es True, añade biomarcadores complementarios.
    - `include_in_range`: Si es True, añade biomarcadores dentro del rango normal.
    """

    if not biomarkers:
        return "No se encontraron biomarcadores relevantes."

    prompt_formatted = f"{prompt}\n\nBiomarcadores seleccionados:\n" + "\n".join(
        [f"{b['name']}: {b['value']}" for b in biomarkers]
    )
    
    if include_complementary:
        prompt_formatted += "\n(Se incluyeron biomarcadores complementarios)"
    if include_in_range:
        prompt_formatted += "\n(Se incluyeron biomarcadores dentro del rango normal)"

    # Simulación de respuesta de ChatGPT
    chatgpt_response = f"Simulación de respuesta de ChatGPT basada en: {prompt_formatted}"
    return chatgpt_response
