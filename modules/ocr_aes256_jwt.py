
import pytesseract
from PIL import Image
import numpy as np
import cv2

# Función para preprocesar imagen para OCR
def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.convert('L')  # Convertir a escala de grises
    np_image = np.array(image)
    _, thresholded = cv2.threshold(np_image, 150, 255, cv2.THRESH_BINARY)
    return Image.fromarray(thresholded)

# Función para extraer texto con OCR en múltiples idiomas y configuración avanzada de PSM
def extract_text_from_image(image_path, psm=6):
    try:
        preprocessed_image = preprocess_image(image_path)
        config = f'--psm {psm}'
        text = pytesseract.image_to_string(preprocessed_image, lang='spa+cat+eng', config=config)
        return text
    except Exception as e:
        print(f"Error en OCR: {e}")
        return ""

# Función para extraer texto de PDF con OCR y configuración avanzada de PSM
def extract_text_from_pdf(pdf_path, psm=6):
    from pdf2image import convert_from_path
    pages = convert_from_path(pdf_path, dpi=300)
    full_text = []
    config = f'--psm {psm}'
    for page in pages:
        text = pytesseract.image_to_string(page, lang='spa+cat+eng', config=config)
        full_text.append(text)
    return "
".join(full_text)
