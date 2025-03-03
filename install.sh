#!/bin/bash
echo 'Iniciando instalación automática en DynamoDB (aarch64)...'

# Instalar Tesseract OCR y sus idiomas automáticamente
echo 'Instalando Tesseract OCR...'
sudo apt-get update -y && sudo apt-get install -y tesseract-ocr

# Copiar los idiomas descargados en la carpeta correcta
echo 'Instalando idiomas de Tesseract OCR...'
sudo cp ./tesseract_data/*.traineddata /usr/share/tesseract-ocr/4.00/tessdata/
echo 'Idiomas de Tesseract OCR instalados correctamente.'

# Verificar instalación
tesseract --version && echo 'Tesseract OCR instalado correctamente.'

echo 'Sistema listo para usar. No es necesaria ninguna configuración adicional.'
