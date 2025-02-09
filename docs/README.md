# Medical-RAGArch: Implementación Automatizada
## 📌 Descripción del Proyecto
Medical-RAGArch es un sistema de almacenamiento y análisis de archivos médicos basado en RAG (Retrieval-Augmented Generation),
permitiendo consultas avanzadas desde ChatGPT y almacenamiento seguro con cifrado **AES-256**.
Este sistema está diseñado para ser fácil de desplegar en **Hugging Face Spaces** sin necesidad de conocimientos técnicos.

## 📂 ¿Dónde se almacenan los archivos médicos?
✅ **Por defecto, todos los archivos médicos se almacenan dentro del RAG en Hugging Face Space del usuario.**  
✅ **Los datos están cifrados con AES-256 y se descifran en tiempo real cuando son consultados.**  
🚫 **Hugging Face Datasets NO es obligatorio y solo se usa si el usuario lo configura explícitamente como almacenamiento externo.**  

## 🔐 Seguridad y Cifrado
🔹 **Todos los datos en RAGArch están cifrados con AES-256.**  
🔹 **Si Hugging Face Datasets se usa como respaldo opcional, los datos también se almacenarán cifrados con AES-256.**  
🔹 **El descifrado ocurre automáticamente sobre la marcha cuando se ejecutan consultas.**  

## 🚀 ¿Cómo desplegar en Hugging Face?

### **Pasos Rápidos**
1️⃣ **Haz un Fork del Repositorio** en tu cuenta de GitHub.  
2️⃣ **Configura tu Token de Hugging Face:**  
   - Ve a [Hugging Face Tokens](https://huggingface.co/settings/tokens).  
   - Genera un nuevo token con permisos de escritura.  
   - Ve a tu repositorio (fork) en GitHub y entra a **Settings > Secrets and Variables > Actions**.  
   - Crea un nuevo secreto llamado `HF_TOKEN` y pega el token generado.  
3️⃣ **Espera a que el workflow automático despliegue el sistema.**  
4️⃣ **Accede a tu espacio de Hugging Face para interactuar con el sistema.**  

### 📌 **Características Principales**
- **Cifrado AES-256**: Todos los datos almacenados están cifrados para garantizar la seguridad.  
- **FastAPI Integrado**: Manejo de autenticación JWT, WebSockets y soporte para consultas en tiempo real.  
- **Interfaz Gradio/Streamlit**: Interacción sencilla para seleccionar prompts, cargar datos y más.  
- **Actualización Automática de Prompts**: Los prompts se sincronizan automáticamente con un repositorio externo en GitHub y Hugging Face Datasets.  
- **Rollback de Prompts**: Posibilidad de restaurar una versión anterior en caso de errores.  
- **Compatibilidad Total**: Diseñado para ser desplegado en Hugging Face Spaces en minutos.  

## 🔄 **Sincronización con Repositorios Base**
El sistema se sincroniza automáticamente con los siguientes repositorios base para mantener todas las funcionalidades actualizadas:

1. **FastAPI Base**: [https://github.com/tiangolo/full-stack-fastapi-postgresql](https://github.com/tiangolo/full-stack-fastapi-postgresql)  
2. **Cifrado AES-256**: [https://github.com/pyca/cryptography](https://github.com/pyca/cryptography)  
3. **Gradio Base**: [https://github.com/gradio-app/gradio](https://github.com/gradio-app/gradio)  
4. **Streamlit Base**: [https://github.com/streamlit/streamlit](https://github.com/streamlit/streamlit)  

## 🔒 Seguridad Mejorada
- **Autenticación JWT**: Todas las solicitudes a FastAPI están protegidas mediante tokens JWT.  
- **Cifrado AES-256**: Los datos se cifran en el almacenamiento y se descifran durante las consultas.  

## 📜 Licencia MIT
Este proyecto está licenciado bajo la **Licencia MIT**, lo que permite su uso, modificación y distribución sin restricciones comerciales.  
Para más información, consulta el archivo `LICENSE.md`.
