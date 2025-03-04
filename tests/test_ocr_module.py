import pytest
from modules.ocr_aes256_jwt_module import pytesseract

def test_ocr_extraction():
    text = pytesseract.image_to_string("tests/sample_image.png", lang="eng")
    assert isinstance(text, str), "El resultado del OCR debe ser un string."
