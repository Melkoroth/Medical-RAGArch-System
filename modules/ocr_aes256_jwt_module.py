
import pytesseract
from PIL import Image
import base64

# Idiomas soportados por Tesseract OCR
SUPPORTED_LANGUAGES = [
    'eng',  # Inglés
    'spa',  # Español
    'fra',  # Francés
    'deu',  # Alemán
    'ita',  # Italiano
    'por',  # Portugués
    'cat',  # Catalán
    'eus',  # Euskera
    'glg'   # Gallego
]

# Detección automática de idioma
def detect_language(image):
    # Analiza el texto en todos los idiomas soportados
    combined_langs = '+'.join(SUPPORTED_LANGUAGES)
    return pytesseract.image_to_string(image, lang=combined_langs)

# OCR con selección automática de idioma
def ocr_image(image_path):
    image = Image.open(image_path)
    # Intentar detección automática de idioma
    try:
        text = detect_language(image)
    except Exception as e:
        print(f"Error en detección automática: {e}. Usando inglés como predeterminado.")
        text = pytesseract.image_to_string(image, lang='eng')
    return text

# OCR desde base64
def ocr_base64(image_base64):
    image_data = base64.b64decode(image_base64)
    with open('temp_image.png', 'wb') as file:
        file.write(image_data)
    return ocr_image('temp_image.png')
