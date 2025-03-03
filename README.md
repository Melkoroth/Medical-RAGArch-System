# 🚀 Medical-RAGArch-System: Despliegue Optimizado en aarch64

## 📌 **Novedades en esta Versión**

### 🔹 **1. Reemplazo de Tesseract por PaddleOCR**  
✅ **OCR más preciso y rápido** en aarch64.  
✅ **Sin dependencias de binarios nativos** → Se instala automáticamente con `pip install paddleocr`.  
✅ **Soporte para múltiples idiomas y mejor rendimiento**.  

### 🔹 **2. Optimización de Dependencias**  
✅ **Prophet → NeuralProphet** (**Predicciones más eficientes**).  
✅ **Scikit-learn-intelex → XGBoost + LightGBM** (**Machine Learning más rápido en ARM**).  
✅ **Poetry → PDM** (**Gestión de dependencias más eficiente**).  
✅ **Plotly → Seaborn/Altair** (**Visualización más ligera y rápida**).  

### 🔹 **3. Instalación 100% Automática en Windows**  
✅ **Ejecuta `install_windows10.bat` y todo se instalará automáticamente**.  
✅ **Descarga RAGArch desde GitHub y lo configura con PaddleOCR y todas las dependencias**.  
✅ **Empaqueta todo en un ZIP listo para subir a GitHub y desplegar en DynamoDB**.  

---  

## 📘 **Instrucciones de Instalación y Uso**  

### **🔹 1. Instalación Automática en Windows**  
Ejecuta el siguiente archivo en Windows para instalar todo:  

```batch
install_windows10.bat
```  

Este script:  
1️⃣ **Descarga el repositorio desde GitHub**.  
2️⃣ **Instala PaddleOCR y todas las dependencias optimizadas**.  
3️⃣ **Empaqueta todo en un ZIP listo para desplegar en DynamoDB**.  

### **🔹 2. Instalación Manual (Linux/macOS/aarch64)**  
Si prefieres instalar manualmente en Linux, usa:  

```bash
git clone https://github.com/Melkoroth/Medical-RAGArch-System.git
cd Medical-RAGArch-System
pip install -r requirements.txt
```  

### **🔹 3. Ejecución del OCR con PaddleOCR**  
Ejemplo de uso en Python:  

```python
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang="es")  # OCR en español
resultado = ocr.ocr("imagen_de_prueba.png", cls=True)
print(resultado)
```  

---  

## 🔧 **Lista de Dependencias Optimizadas**  

| 🔍 **Paquete Antiguo**         | 🚀 **Nueva Alternativa**        | ✅ **Motivo de Cambio** |
|--------------------------------|--------------------------------|------------------------|
| `pytesseract` (OCR)            | **PaddleOCR**                  | 🔥 **Más preciso y rápido**, sin dependencias nativas |
| `prophet` (Series Temporales)  | **NeuralProphet**              | 📈 Mejor rendimiento en **aarch64** |
| `scikit-learn-intelex`         | **XGBoost + LightGBM**         | 🏆 **Optimizado para ARM, evita dependencias Intel** |
| `poetry` (Gestor de Dependencias) | **PDM**                    | ⚡ **Más ligero y rápido** |
| `plotly` (Visualización)       | **Seaborn o Altair**           | 📊 **Menos pesado, más eficiente** |

📌 **Todos estos cambios ya están reflejados en `requirements.txt`.**  

---  

## 🚀 **Despliegue en DynamoDB**  

1️⃣ **Sube el ZIP generado a GitHub**.  
2️⃣ **Ejecuta `install_windows10.bat` en cualquier PC Windows** para preparar la versión lista para subir.  
3️⃣ **Desde AWS Lambda**, usa `pip install -r requirements.txt` para instalar las dependencias en el entorno.  
4️⃣ **RAGArch estará completamente optimizado y listo para su uso.**  

---  

## 🔒 **Seguridad y Cifrado**  
✔ **AES-256-GCM** para cifrado de datos en tránsito.  
✔ **Tokens OAuth2 con ES256 (ECDSA)** para autenticación segura.  
✔ **TLS 1.3 habilitado en WebSockets y API Gateway**.  

---  

## 📄 **Generación Automática de Reportes**  
✅ **Ahora puedes generar reportes en PDF automáticamente** con análisis de biomarcadores.  
✅ **Se ejecuta sin intervención manual y genera visualizaciones optimizadas.**  

Ejemplo de uso:  

```python
from modules.report_generation import generate_biomarker_report
import pandas as pd

data = pd.DataFrame({
    "Fecha": ["2024-03-01", "2024-04-01", "2024-05-01"],
    "Biomarcador": ["Glucosa", "Colesterol", "Triglicéridos"],
    "Valor": [95, 180, 150],
    "Predicción": [90, 175, 145]
})

generate_biomarker_report(data)
```  

🚀 **Ahora todo el proceso es más rápido, seguro y fácil de desplegar en aarch64.** 🔥  

---  

📌 **Si tienes dudas o necesitas soporte, contacta a [Melkoroth](https://github.com/Melkoroth).**  
