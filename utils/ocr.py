from paddleocr import PaddleOCR
from PIL import Image

ocr = PaddleOCR(use_angle_cls=True, lang="en")

def extract_text_from_image(image_path: str):
    image = Image.open(image_path)
    results = ocr.ocr(image_path, cls=True)
    return [result[1][0] for result in results[0]]

# Uso de ejemplo
print(extract_text_from_image("example_image.png"))
