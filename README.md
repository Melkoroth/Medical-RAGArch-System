# 🚀 Medical-RAGArch-System: Despliegue Optimizado en aarch64

## 📌 **Novedades en esta Versión**

### 🔹 **1. Implementación de Despliegue Automatizado en AWS**  
✅ Ahora puedes **desplegar tu propio sistema en AWS sin introducir credenciales manualmente**.  
✅ Se crea automáticamente **una API en AWS Lambda y un almacenamiento en DynamoDB**.  
✅ **Cada usuario tiene su propio entorno independiente**, ideal para forks y despliegues personalizados.  

### 🔹 **2. OCR Mejorado con PaddleOCR**  
✅ **OCR más preciso y rápido** en aarch64.  
✅ **Sin dependencias de binarios nativos** → Se instala automáticamente con `pip install paddleocr`.  
✅ **Soporte para múltiples idiomas y mejor rendimiento**.  

---  

## 📘 **Instrucciones de Instalación y Uso**  

### **🔹 1. Instalación Manual (Linux/macOS/aarch64)**  
Si prefieres instalar manualmente en Linux, usa:  

```bash
git clone https://github.com/Melkoroth/Medical-RAGArch-System.git
cd Medical-RAGArch-System
pip install -r requirements.txt
```  

### **🔹 2. Ejecución del OCR con PaddleOCR**  
Ejemplo de uso en Python:  

```python
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang="es")  # OCR en español
resultado = ocr.ocr("imagen_de_prueba.png", cls=True)
print(resultado)
```  

---  

## 🚀 **Despliegue Automático en AWS**  

### 📌 **¿Cómo desplegar tu propio sistema en AWS?**  
Este repositorio permite que **cualquier usuario haga un fork y cree su propio entorno en AWS**, sin necesidad de introducir credenciales manualmente.

### 🔹 **Pasos para desplegar tu entorno personalizado:**  
1. **Haz un fork** de este repositorio en GitHub.  
2. **Ve a la pestaña "Actions" en tu fork.**  
3. **Selecciona el workflow "Deploy Personal AWS Environment".**  
4. **Ejecuta el workflow manualmente (workflow_dispatch).**  
5. **Espera unos minutos mientras GitHub Actions despliega automáticamente tu entorno en AWS.**  

### 🔹 **¿Qué se desplegará automáticamente?**  
✅ **Un nuevo AWS DynamoDB** para almacenar los datos de tu instancia.  
✅ **Un nuevo AWS Lambda con FastAPI**, que servirá como punto de acceso para consultas desde IA como ChatGPT.  
✅ **Una API Gateway en AWS**, que te proporcionará un endpoint para acceder a FastAPI desde cualquier aplicación.  

### 🔹 **¿Cómo saber si el despliegue fue exitoso?**  
Al finalizar el workflow, verás un mensaje en los logs como este:  
```
✅ API desplegada en: https://<tu-endpoint>.execute-api.us-east-1.amazonaws.com/prod/
```
Este es el enlace de tu propia API en AWS. ¡Listo para usar! 🚀  

---  

## 📄 **Archivo `.env.example`**  
El archivo `.env.example` proporciona una plantilla de configuración para variables de entorno.  
Para usarlo:  
1. **Copia el archivo y renómbralo como `.env`**.  
2. **Edita los valores según tu configuración**.  
3. **Ejemplo de variables en `.env`:**  

```
SECRET_KEY=tu_clave_secreta_personalizada
JWT_SECRET_KEY=otra_clave_secreta
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=tu_password_redis
FERNET_KEY=clave_cifrado_fernet
```

Este archivo **no contiene credenciales reales**, solo ejemplos de configuración.  



---

## 🛠 **Pruebas Automáticas y Validación del Código**

### ✅ **¿Cómo funciona el sistema de pruebas?**
El sistema incluye **pruebas automáticas (`pytest`)** para validar el funcionamiento de módulos clave.  
Cada vez que se sube un cambio, **GitHub Actions ejecuta las pruebas automáticamente** con `run_tests.yml`.  

### 🔹 **Módulos que tienen pruebas**
✅ **API de interacciones medicamentosas** (`drug_interaction_api.py`).  
✅ **Generación de reportes en PDF y JSON** (`report_generation.py`).  
✅ **Predicción de datos clínicos con Prophet** (`ml_forecasting.py`).  
✅ **Conexión a Redis Cloud Essentials** (`redis_cloud.py`).  

### 🔹 **¿Cómo ejecutar las pruebas manualmente?**
Si quieres ejecutar las pruebas en tu equipo, usa:
```bash
pytest tests/ --maxfail=5 --disable-warnings
```

### 🔹 **¿Cómo GitHub Actions valida el código?**
Cuando se sube un cambio (`push`) o se abre un PR (`pull request`):
1️⃣ GitHub ejecuta `run_tests.yml`.  
2️⃣ **Si las pruebas fallan, el sistema muestra un error.**  
3️⃣ Esto evita que código defectuoso llegue a producción.  



### 🔹 **Nuevas Pruebas Agregadas**
✅ **Gráficos de tendencias clínicas** (`analytics_comparison.py`).  
✅ **Extracción de texto con OCR** (`ocr_aes256_jwt_module.py`).  
✅ **Validación de interacciones entre suplementos** (`supplement_interaction_validation.py`).  

🔹 Estas pruebas se ejecutan automáticamente en **GitHub Actions** cada vez que se sube un cambio.  
🔹 También puedes ejecutarlas manualmente con:
```bash
pytest tests/ --maxfail=5 --disable-warnings
```


---

## 🔹 **Dependencias Importantes del Proyecto**
Este proyecto usa varias librerías especializadas. Asegúrate de que están instaladas correctamente:

### ✅ **Librerías Clave y sus Usos**
- **FastAPI** → API principal del sistema.
- **Redis** → Caché para acelerar consultas.
- **PaddleOCR** → OCR avanzado para reconocimiento de texto.
- **Numba** → Acelera cálculos matemáticos.
- **TensorFlow** → Optimización de modelos de IA.
- **NeuralProphet** → Predicciones de biomarcadores.
- **Matplotlib / Seaborn / Plotly** → Generación de gráficos clínicos.
- **OpenCV** → Procesamiento de imágenes para OCR.

Puedes instalar todas las dependencias con:
```bash
pip install -r requirements.txt
```

---

## 🔹 **Módulos Clave del Proyecto y sus Funciones**
Este sistema incluye módulos especializados para diversas tareas:

### ✅ **Módulos No Documentados Anteriormente**
- **`dynamodb_optimization.py`** → Optimiza consultas a DynamoDB.
- **`numba_optimization.py`** → Usa `Numba` para acelerar cálculos.
- **`ocr_aes256_jwt_module.py`** → Extrae texto con OCR y maneja JWT.
- **`ragarch_sources_config.py`** → Obtiene jerarquización de fuentes.
- **`reporting_generator.py`** → Genera reportes en PDF y JSON.
- **`supplement_interaction_validation.py`** → Valida interacciones de suplementos.
- **`synergy_analysis.py`** → Evalúa combinaciones de tratamientos.
- **`tensorflow_optimization.py`** → Optimiza modelos de IA con TensorFlow XLA.

