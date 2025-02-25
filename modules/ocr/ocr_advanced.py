
# OCR Avanzado con Pytesseract y Pillow

from PIL import Image
import pytesseract

# Cargar imagen de ejemplo
image_path = 'ejemplos/documento_medico.png'
img = Image.open(image_path)

# OCR para extraer texto de la imagen
text = pytesseract.image_to_string(img, lang='spa')
print("Texto extraído del documento médico:")
print(text)
