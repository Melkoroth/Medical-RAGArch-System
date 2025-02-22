
import requests
import logging

def test_main_endpoint():
    url = "https://localhost:8000/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info("✅ main.py responde correctamente en /")
            logging.info("Respuesta:", response.json())
        else:
            logging.info("❌ main.py responde con un error en /:", response.status_code)
    except Exception as e:
        logging.info("❌ Error al probar main.py en /:", str(e))

test_main_endpoint()
