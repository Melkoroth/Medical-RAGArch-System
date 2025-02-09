
RAGArch - Sistema de Almacenamiento y Gestión de Prompts

Este repositorio contiene la configuración personalizada de RAGArch con seguridad avanzada, integración con ChatGPT y administración de prompts desde Hugging Face.

Características:
- Autenticación segura con JWT
- Interfaz en Gradio para la selección de prompts
- Actualización automática de la biblioteca de prompts desde GitHub
- Gestión de datos médicos con almacenamiento cifrado

Instalación y Uso:
1. Instalar dependencias
   pip install fastapi uvicorn jwt gradio requests
2. Ejecutar FastAPI
   uvicorn api.main:app --reload
3. Ejecutar la interfaz de usuario
   python frontend/interface.py

Seguridad:
- Uso de tokens JWT para autenticación
- Conexión cifrada con HTTPS
- Acceso a la biblioteca de prompts solo a través de FastAPI
