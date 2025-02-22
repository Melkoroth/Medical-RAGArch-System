
# Mock para evitar bloqueos en módulos que esperan respuesta de API externa

from unittest.mock import patch

# Mock para drug_interaction_api.py
with patch('modules.drug_interaction_api.requests.get') as mock_get:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"interactions": []}
    logging.info("Mock aplicado en drug_interaction_api.py")

# Mock para ocr_aes256_jwt.py
with patch('modules.ocr_aes256_jwt.process_image') as mock_process:
    mock_process.return_value = "Texto simulado"
    logging.info("Mock aplicado en ocr_aes256_jwt.py")

# Mock para frontend/interface.py
with patch('frontend.interface.input', return_value='mocked_input'):
    logging.info("Mock aplicado en frontend/interface.py")
