#!/bin/bash
echo "Iniciando instalación de RAGArch..."

# Instalar dependencias desde requirements.txt
pip install -r requirements.txt

# Verificar si FastAPI y AWS Lambda están instalados
echo "Verificando instalación de FastAPI y AWS Lambda..."
pip show fastapi > /dev/null 2>&1 && echo "✅ FastAPI instalado" || echo "❌ FastAPI NO está instalado"
pip show aws_lambda_sdk > /dev/null 2>&1 && echo "✅ AWS Lambda SDK instalado" || echo "❌ AWS Lambda SDK NO está instalado"

echo "Configuración completada. Ejecuta 'python app.py' para iniciar RAGArch."
