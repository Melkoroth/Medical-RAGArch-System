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
1️⃣ **Clona este repositorio en tu cuenta de GitHub.**  
2️⃣ **Crea un nuevo espacio en Hugging Face (tipo "FastAPI").**  
3️⃣ **Conecta tu Hugging Face Space con tu GitHub.**  
4️⃣ **El sistema se desplegará automáticamente y estará listo para recibir archivos y consultas.**  

## 📜 Licencia MIT
Este proyecto está licenciado bajo la **Licencia MIT**, lo que permite su uso, modificación y distribución sin restricciones comerciales.  
Para más información, consulta el archivo `LICENSE.md`.