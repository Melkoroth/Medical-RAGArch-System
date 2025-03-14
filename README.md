
# ⚠️ **IMPORTANTE: Entorno de ejecución de los comandos**

🔹 **La documentación actual usa sintaxis y herramientas nativas de Linux**, como `bash`, `export`, `chmod`, y comandos de AWS CLI.  
🔹 **Está optimizada para ejecutarse en AWS (EC2, EFS, Lambda) o en una terminal Linux/Mac.**  
🔹 **No está diseñada para ejecutarse en Windows CMD o PowerShell directamente.**  

---

## 🖥️ **Ejecutar comandos desde Windows para gestionar el despliegue en AWS**

Si usas Windows y necesitas gestionar el despliegue en AWS, sigue estas instrucciones:  

### 🔹 **1. Instalar AWS CLI en Windows**
1️⃣ Descarga e instala [AWS CLI para Windows](https://aws.amazon.com/cli/).  
2️⃣ Abre **PowerShell** como administrador.  
3️⃣ Configura las credenciales de AWS con:  
   ```powershell
   aws configure
   ```

### 🔹 **2. Usar PowerShell para exportar variables de entorno**  
💡 En Linux usamos `export`, en PowerShell se usa `$env:`  

**Ejemplo en Linux:**  
```sh
export AWS_ACCESS_KEY_ID="TU_ACCESS_KEY"
export AWS_SECRET_ACCESS_KEY="TU_SECRET_KEY"
```

**Equivalente en Windows PowerShell:**  
```powershell
$env:AWS_ACCESS_KEY_ID="TU_ACCESS_KEY"
$env:AWS_SECRET_ACCESS_KEY="TU_SECRET_KEY"
```

### 🔹 **3. Ejecutar GitHub Actions desde Windows**  
Los workflows de GitHub Actions no dependen del sistema operativo, pero puedes iniciarlos manualmente desde Windows con:  
```powershell
gh workflow run deploy.yml
```

---

✅ **Con esto, puedes gestionar el despliegue en AWS desde Windows sin necesidad de cambiar la infraestructura a Windows.**


# 🚀 **Guía de Despliegue con AWS y GitHub Actions**

Esta sección describe **paso a paso** cómo desplegar Medical-RAGArch-System en **AWS Lambda** y **DynamoDB** utilizando **GitHub Actions**.

## 📌 **1️⃣ Resumen del Despliegue**

| **Paso** | **Acción** | **Detalles** |
|----------|-----------|-------------|
| 1️⃣ | **Crear Cuenta AWS** | [Crear cuenta en AWS](https://aws.amazon.com/) |
| 2️⃣ | **Configurar IAM** | [Configurar IAM y credenciales](https://docs.aws.amazon.com/IAM/) |
| 3️⃣ | **Configurar AWS CLI** | `aws configure` |
| 4️⃣ | **Agregar Credenciales en GitHub** | Configurar `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION` |
| 5️⃣ | **Ejecutar GitHub Actions** | Orden de ejecución recomendado |
| 6️⃣ | **Verificar en AWS Lambda** | Confirmar despliegue en [AWS Lambda](https://console.aws.amazon.com/lambda) |
| 7️⃣ | **Acceder a la API** | API Gateway en AWS |

## 📌 **2️⃣ Configuración de AWS**
### 🔹 **1. Crear Cuenta y Configurar IAM**
1️⃣ Crear una cuenta en [AWS](https://aws.amazon.com/).  
2️⃣ Ir a [IAM](https://console.aws.amazon.com/iam) y generar una **Access Key** y **Secret Key**.  
3️⃣ Agregar los permisos necesarios para **Lambda**, **DynamoDB** y **API Gateway**.  

### 🔹 **2. Configurar AWS CLI**
Ejecutar en la terminal:
```sh
aws configure
```
Ingresar las credenciales de AWS generadas en IAM.

## 📌 **3️⃣ Configuración de GitHub Actions**

### 🔹 **1. Agregar Credenciales en GitHub Secrets**
1️⃣ Ir a **GitHub > Settings > Secrets and variables > Actions**.  
2️⃣ Agregar las siguientes credenciales:  
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_REGION`  

### 🔹 **2. Orden de Ejecución de Workflows**
Ejecutar los workflows en este orden:

1️⃣ **`setup_efs_vpc.yml`** → Configura AWS EFS y la VPC necesaria.  
2️⃣ **`deploy_lambda_layers.yml`** → Sube dependencias a AWS Lambda Layers.  
3️⃣ **`deploy_with_secrets.yml`** → Configura IAM y Secrets Manager.  
4️⃣ **`deploy.yml`** → Despliega la API en AWS Lambda.  
5️⃣ **`run_tests.yml`** → Ejecuta pruebas para validar el despliegue.  

## 📌 **4️⃣ Verificación del Despliegue**
1️⃣ Ir a **[AWS Lambda](https://console.aws.amazon.com/lambda)** y verificar que la función `"MedicalRAG"` está creada.  
2️⃣ Revisar **[DynamoDB](https://console.aws.amazon.com/dynamodb)** y confirmar que la tabla `"MedicalData"` existe.  
3️⃣ Acceder a **[API Gateway](https://console.aws.amazon.com/apigateway)** y probar los endpoints.

✅ **Listo. El sistema está desplegado y operativo en AWS.**  

# 🚀 Medical-RAGArch-System

✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.


---



### 📌 Estado de las Optimizaciones Documentadas
Se confirma que las siguientes optimizaciones mencionadas en el README **ya están implementadas en el sistema**:

✅ **DAX en DynamoDB activado:** `aws/enable_dax.py`  
✅ **Auto Scaling en DynamoDB activado:** `aws/enable_adaptive_capacity.py`  
✅ **SnapStart en AWS Lambda activado:** `aws/lambda_snapstart.py`  
✅ **OCR Automático habilitado:** `modules/ocr/ocr_advanced.py`  
✅ **Optimización de Redis Cloud implementada:** `modules/cache/cache_redis.py`  

No es necesario realizar cambios adicionales en estos aspectos.  

## 🔐 **Autenticación y Seguridad**
Para proteger las herramientas expuestas a ChatGPT, se han implementado:
✅ **Autenticación con  y API Keys generadas dinámicamente.**  
✅ **Protección con firma HMAC en cada solicitud.**  
✅ **Cifrado TLS en API Gateway de AWS.**  
✅ **Restricción de llamadas en AWS Lambda a solicitudes autenticadas.**  

📌 **Ubicación de los archivos de seguridad:**
| Archivo | Ubicación en el Proyecto |
|---------|-------------------------|
| `fastapi_authentication.py` | `api/security/fastapi_authentication.py` |
| `aws_api_gateway_flexible.tf` | `infrastructure/aws/terraform/aws_api_gateway_flexible.tf` |
| `aws_lambda_secure_invocation.tf` | `infrastructure/aws/terraform/aws_lambda_secure_invocation.tf` |

---

## 🤖 **IA Compatibles y Métodos de Integración**

El sistema puede integrarse con **cualquier IA que soporte API HTTP o WebSockets**.  
Ejemplos de integración con modelos populares:

📌 **Cómo Integrarlo:**  
```python
    model="gpt-4",
    messages=[{"role": "system", "content": "Analiza este documento médico"}],
    REMOVED_SECRET
)
```

---

### **2️⃣ Hugging Face Transformers (Modelos NLP en Local o en la Nube)**
📌 **Cómo Integrarlo:**  
```python
from transformers import pipeline
summarizer = pipeline("summarization")
summary = summarizer("Este es un texto largo que quiero resumir.")
```

---

### **3️⃣ Stable Diffusion (Generación de Imágenes Médicas)**
📌 **Cómo Integrarlo:**  
```python
import requests
response = requests.post("https://stablediffusion.api/imagen", json={"prompt": "Radiografía de tórax con neumonía"})
```

---

### **4️⃣ API de IA Médicas Especializadas (IBM Watson, MedPaLM 2, BioGPT)**
📌 **Cómo Integrarlo:**  
```python
response = requests.post("https://biogpt.api/med-query", json={"query": "Efectos de la metformina en resistencia a la insulina"})
```

---

## 🔄 **Despliegue Automatizado en AWS**
Todos los componentes del sistema se despliegan automáticamente con **GitHub Actions** y **Terraform**, sin intervención manual.

📌 **Workflows Configurados:**
| Workflow | Función |
|----------|--------|
| `deploy.yml` | Despliega la API en AWS Lambda |
| `update_prompts.yml` | Sincroniza los prompts |
| `deploy_with_secrets.yml` | Configura variables de entorno automáticamente |

📌 **Ejecución Automática:**  
```bash
git push origin main  # Despliega automáticamente en AWS
```

---

## 📄 **Instrucciones para Usuarios No Técnicos**
1️⃣ **Ejecutar el despliegue con GitHub Actions** (sin comandos manuales).  
2️⃣ **Conectarse a ChatGPT usando API Keys generadas automáticamente**.  
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

4️⃣ **El sistema maneja toda la seguridad de forma transparente.**  




# Medical-RAGArch-System

## 📌 ¿Qué es este proyecto?
Medical-RAGArch-System es un sistema de **IA aplicada a documentos médicos**, que permite:
- **Almacenar, procesar y recuperar información estructurada** de documentos médicos.
- **Optimizar la infraestructura en la nube con AWS Lambda y DynamoDB**.
- **Automatizar despliegues y mantenimiento** con GitHub Actions y AWS CDK.

Esta versión incluye mejoras clave en rendimiento, seguridad y escalabilidad.



## 🔹 1️⃣ Procesos Totalmente Automatizados


# 🚀 Integración con AWS (Lambda, DynamoDB, API Gateway)

Este proyecto utiliza múltiples servicios de **AWS** para mejorar su rendimiento, escalabilidad y disponibilidad.

## 📌 **Servicios Utilizados**

| Servicio      | Función en el Proyecto |
|--------------|------------------------|
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

| **DynamoDB** | Base de datos NoSQL optimizada para respuestas rápidas |
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

| **SnapStart** | Reduce los tiempos de arranque de Lambda |
| **DAX** | Acelera las consultas en DynamoDB |

## ⚙️ **Configuración Manual en AWS**
Si deseas configurar manualmente los servicios en AWS, sigue estos pasos:

### **1️⃣ Configurar AWS Lambda**
```bash
aws lambda create-function --function-name MedicalRAG --runtime python3.8 --role <IAM_ROLE> --handler api.main.lambda_handler
```

### **2️⃣ Configurar DynamoDB**
```bash
aws dynamodb create-table --table-name MedicalData --attribute-definitions AttributeName=id,AttributeType=S --key-schema AttributeName=id,KeyType=HASH --billing-mode PAY_PER_REQUEST
```

---

## 🛠️ **Configuración Automática con CDK**
Si prefieres desplegarlo automáticamente, usa los scripts de `aws/`:
```bash
cd aws/
python enable_dax.py  # Activa DAX en DynamoDB
python lambda_snapstart.py  # Habilita SnapStart en AWS Lambda
```




Estos procesos se ejecutan sin intervención manual una vez configurados:

| **Funcionalidad** | **Automatización** | **Explicación** |
|--------------|-------------|-------------|
| **Carga y procesamiento de documentos** | ✅ Sí | El sistema detecta automáticamente el tipo de documento y lo procesa. |
| **OCR automático** | ✅ Sí | Si el documento es una imagen escaneada, el OCR se activa sin necesidad de ajuste manual. |
| **Optimización de consultas con Redis** | ✅ Sí | Las consultas repetidas se almacenan en caché para reducir la carga en DynamoDB. |
| **Despliegue en AWS Lambda y DynamoDB con GitHub Actions** | ✅ Sí | El código se actualiza y despliega automáticamente sin intervención. |
| **Auto Scaling en DynamoDB** | ✅ Sí | Se ajusta la capacidad de la base de datos según la demanda del sistema. |
| **Generación de respuestas estructuradas para ChatGPT** | ✅ Sí | Las respuestas son resumidas y formateadas automáticamente antes de enviarlas. |

---

## 🔹 2️⃣ Procesos que Requieren Configuración Manual


# 🚀 Optimización con Redis y Numba

Este proyecto utiliza **Redis Cloud** y **Numba** para mejorar el rendimiento en tiempo de respuesta y cálculos intensivos.

## 📌 **Optimización con Redis**

Redis se usa para **cachear respuestas frecuentes**, reduciendo la carga en DynamoDB.

### **📌 Configuración Manual de Redis**
1️⃣ Crea un clúster de Redis en AWS o usa una instancia local.  
2️⃣ Configura el archivo `config/redis_config.py` con las credenciales:

```python
REDIS_HOST = "redis-cluster.amazonaws.com"
REDIS_PORT = 6379
REDIS_REMOVED_SECRET
```

### **📌 Uso en el Código**
```python
import redis

cache = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True)
cache.set("consulta_usuario", resultado_procesado, ex=3600)  # Cache por 1 hora
```

---

## ⚡ **Optimización con Numba**
Numba acelera cálculos de Machine Learning y NLP optimizando operaciones matemáticas intensivas.

### **📌 Ejemplo de Uso**
```python
from numba import jit

@jit(nopython=True)
def calcular_metricas(datos):
    return sum(datos) / len(datos)
```




Algunas funciones necesitan intervención manual para ajustarse a escenarios específicos:

| **Funcionalidad** | **Intervención Manual** | **Motivo** |
|--------------|-------------|-------------|
| **Ajuste de umbral en OCR** | ⚠️ Sí | Dependiendo de la calidad de la imagen, puede ser necesario ajustar la precisión del OCR. |
| **Políticas de retención de datos en DynamoDB** | ⚠️ Sí | Por defecto, los datos se almacenan indefinidamente, pero pueden configurarse reglas de expiración. |
| **Modificación del NLP para respuestas más detalladas o resumidas** | ⚠️ Sí | Se puede modificar el nivel de resumen en el modelo de NLP. |
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

| **Seguridad y autenticación avanzada** | ⚠️ Sí | Si se necesita una capa extra de seguridad, se pueden modificar los métodos de autenticación. |



## 🔹 3️⃣ Casos Prácticos para Diferentes Niveles de Automatización


# 🤖 Modelos de Machine Learning y NLP

El sistema incluye modelos de **predicción y procesamiento de lenguaje natural (NLP)** para analizar documentos médicos.

## 📌 **Modelos Implementados**
| Módulo | Funcionalidad |
|--------|--------------|
| **ml_models.py** | Modelos de predicción y clasificación |
| **intelligent_context.py** | Procesamiento avanzado de lenguaje natural |
| **time_series.py** | Predicciones basadas en series temporales |

---

## ⚙️ **Cómo Personalizar los Modelos**

### **Modificar Parámetros del Modelo NLP**
Edita el archivo `config/nlp_config.json`:
```json
{
    "max_length": 500,
    "min_length": 200,
    "do_sample": true
}
```

### **Ejemplo de Uso en el Código**
```python
from transformers import pipeline

summarizer = pipeline("summarization", max_length=500, min_length=200, do_sample=True)
```




### **Escenario 1: Uso estándar con automatización total**  
🔹 **Tienes documentos en AWS S3 y deseas analizarlos automáticamente.**  
✅ **Solución:** Configura una regla en AWS Lambda para que procese cualquier archivo nuevo automáticamente.  

```json
{
  "source": "AWS-S3",
  "processing_mode": "AUTO"
}
```

---

### **Escenario 2: Seguridad Avanzada y Retención de Datos**  
🔹 **Requieres mayor control sobre los tiempos de expiración de los documentos.**  
✅ **Solución:** Configura políticas de retención en DynamoDB y habilita autenticación avanzada con .  

```bash
export TOKEN_EXPIRATION=3600  # Expiración de tokens en 1 hora
```

---

### **Escenario 3: Activar WebSockets para Consultas en Tiempo Real**  
🔹 **Quieres que ChatGPT pueda obtener respuestas sin esperar consultas HTTP tradicionales.**  
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.


```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000 --ws
```



## 🔹 Interacción con Código Python y Comandos Bash


# 🔄 Despliegue con GitHub Actions

El sistema tiene **workflows automáticos** para desplegar en AWS.

## 📌 **Workflows Disponibles**
| Workflow | Función |
|----------|--------|
| `deploy.yml` | Despliega la API en AWS Lambda |
| `update_prompts.yml` | Sincroniza los prompts |
| `deploy_with_secrets.yml` | Configura variables de entorno automáticamente |

### **📌 Cómo Ejecutar un Despliegue**
```bash
git push origin main  # Esto activará el workflow de GitHub Actions automáticamente
```




Medical-RAGArch-System permite ajustar configuraciones y ejecutar acciones a través de código Python y comandos Bash.

---

### 🔹 **Uso de Código Python**

✔ **Los fragmentos de código Python ya están implementados en el sistema.**  
✔ **Solo necesitas modificarlos si deseas personalizar la configuración.**  
✔ **Si un archivo específico es mencionado (`api/main.py`, `nlp_config.py`), edítalo ahí.**  

📌 **Ejemplo de ajuste en Python (modificar en `nlp_config.py`)**  
```python
summarizer = pipeline('summarization', max_length=500, min_length=250, do_sample=True)
```

📌 **Otros ejemplos de código en Python utilizados en diferentes secciones:**  

- **WebSockets:** Comunicación en tiempo real con consultas optimizadas.  
- **OCR con OpenCV:** Mejora de precisión en documentos escaneados.  
- **Optimización de caché con Redis:** Acelerar consultas frecuentes.  

---

### 🔹 **Uso de Comandos Bash**

✔ **Se ejecutan en la terminal (Linux/macOS o AWS CloudShell).**  
✔ **NO debes pegarlos dentro del código del proyecto.**  
✔ **Se usan para configurar AWS Lambda, Redis o DynamoDB manualmente.**  

📌 **Ejemplo de comando Bash (ejecutar en la terminal)**  
```bash
aws lambda update-function-configuration --function-name MedicalRAG --memory-size 2048
```

📌 **Otros comandos útiles:**  

- **Configurar OCR avanzado en AWS Lambda**  
- **Habilitar SnapStart para mejorar tiempos de ejecución**  
- **Ajustar escalado automático en DynamoDB**  



## 🔹 5️⃣ Restaurar la Explicación sobre AWS Lambda SnapStart y DAX


# 🔐 Seguridad con AES-256 y 

Este proyecto protege la información mediante **cifrado AES-256** y **autenticación con **.

## 📌 **Cifrado AES-256**
Se usa para proteger datos sensibles en bases de datos y en transmisión.

### **📌 Ejemplo de Encriptación**
```python
from Crypto.Cipher import AES

cipher = AES.new(key, AES.MODE_GCM)
ciphertext, tag = cipher.encrypt_and_digest(data)
```

---

## 🛠️ **Gestión de Tokens **
Se usa  para manejar sesiones y autenticación.

### **📌 Crear un Token **
```python
✅ **Sistema de Seguridad Actualizado:**
-  ha sido **totalmente eliminado** y reemplazado por Zero Trust Architecture (ZTA).
- La autenticación y seguridad ahora se gestionan a través de identidades y accesos controlados dinámicamente.


✅ **Sistema de Seguridad Actualizado:**
-  ha sido **totalmente eliminado** y reemplazado por Zero Trust Architecture (ZTA).
- La autenticación y seguridad ahora se gestionan a través de identidades y accesos controlados dinámicamente.

```




📌 **Configuración Manual Necesaria**:  
1. **Configurar Subnet Group en AWS Console** para que el clúster pueda operar.  
2. **Agregar Security Groups si es necesario**, según la arquitectura de red de AWS.  
3. **Actualizar la configuración de la aplicación para conectarse a DAX en vez de DynamoDB directamente.**  

### **Activación Manual de AWS Lambda SnapStart**
- **SnapStart reduce el tiempo de arranque de Lambda** y mejora la latencia.
- **Debe activarse manualmente en la consola de AWS**, ya que AWS no permite su activación automática desde CDK.

📌 **Pasos para activarlo**:
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

2. En la pestaña **Configuración**, buscar la opción **SnapStart** y activarla.
3. Guardar los cambios y probar la ejecución.


# ⚙️ Configuraciones Avanzadas y Personalización en Medical-RAGArch-System

Medical-RAGArch-System permite ajustar múltiples configuraciones para **optimizar rendimiento, mejorar seguridad y personalizar la experiencia del usuario**.

✅ **Ajustes de rendimiento en AWS Lambda, Redis y DynamoDB.**  
✅ **Personalización de respuestas NLP y procesamiento de documentos.**  
✅ **Modificaciones en seguridad, autenticación y cifrado.**  
✅ **Optimización exclusiva para `aarch64` (no compatible con Windows).**  
✅ **Configuraciones automatizadas vs. ajustes manuales.**  

---

## 🔹 1️⃣ Parámetros Ajustables para Optimizar el Sistema

| **Configuración** | **Descripción** | **Valor Predeterminado** | **Automático** |
|------------------|----------------|-----------------|------------|
| `AWS Lambda Memory` | Ajusta la memoria para mejorar rendimiento en consultas. | 1024 MB | ✅ Sí |
| `DynamoDB Capacity` | Modifica el escalado automático de la base de datos. | Auto Scaling | ✅ Sí |
| `OCR Precision` | Ajusta la sensibilidad de detección en imágenes escaneadas. | 0.85 | ⚠️ Manual |
| `WebSockets Timeouts` | Cambia el tiempo de espera en comunicación en tiempo real. | 30 seg | ✅ Sí |
| `Cache Expiry` | Ajusta la expiración de caché en Redis para optimizar respuestas. | 1 hora | ✅ Sí |
| `NLP Summary Length` | Controla la longitud de los resúmenes generados por NLP. | 250 palabras | ⚠️ Manual |

📌 **Notas**:  
- **Redis ya está habilitado y configurado, solo requiere ajustes si se necesita un mayor control.**  
- **AWS Lambda SnapStart está activado para reducir tiempos de inicio en frío.**  
- **Este sistema está optimizado exclusivamente para `aarch64` y no funciona en Windows.**  

---

✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.


### **📌 Ajustar Permisos CORS y Seguridad**
Si necesitas restringir accesos externos:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://mi-sitio.com"],
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization"],
)
```

📌 **Consejo:** **Nunca permitas `allow_origins=["*"]` en producción** para evitar ataques.

### **📌 Habilitar WebSockets para Consultas en Tiempo Real**
WebSockets ya están habilitados y optimizados, pero puedes ajustar parámetros si es necesario:

```python
WEBSOCKET_TIMEOUT = 20  # Reducir tiempo de espera para respuestas más rápidas
```

📌 **Ventajas:**  
✅ **Permite respuestas inmediatas sin múltiples peticiones HTTP.**  
✅ **Reduce la latencia de consultas en ChatGPT.**  

---

## 🔹 3️⃣ Personalización de Respuestas NLP y Procesamiento de Documentos

Si deseas que las respuestas sean más detalladas o más concisas, puedes ajustar:

```python
summarizer = pipeline('summarization', model="facebook/bart-large-cnn", max_length=500, min_length=250, do_sample=True)
```

📌 **Opciones avanzadas:**  
- **Resúmenes concisos** → `max_length = 150`.  
- **Respuestas detalladas** → `max_length = 800`.  

📌 **OCR ya está habilitado**, pero puedes mejorar la precisión con preprocesamiento de imágenes en OpenCV:

```python
image = cv2.imread("documento.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5,5), 0)
```

---

## 🔹 4️⃣ Optimización de Rendimiento en AWS Lambda y DynamoDB


# 📄 OCR Avanzado y Validación de Suplementos

El sistema tiene **OCR mejorado** para procesar documentos escaneados y **valida interacciones entre suplementos médicos**.

## 📌 **OCR Mejorado**
El módulo `ocr_advanced.py` mejora el reconocimiento de texto en imágenes de baja calidad.

### **📌 Ejemplo de Uso**
```python
from utils.ocr import procesar_imagen

texto_extraido = procesar_imagen("documento.jpg")
```

---

## 🧪 **Validación de Interacciones entre Suplementos**
El archivo `supplement_validation.yaml` contiene reglas para verificar combinaciones peligrosas.

### **📌 Ejemplo de Validación**
```python
from modules.supplement_interaction_validation import validar_interaccion

resultado = validar_interaccion("Omega 3", "Anticoagulantes")
```




### **📌 Ajustar AWS Lambda para Mayor Velocidad**
AWS Lambda está optimizado para `aarch64`, pero puedes aumentar memoria si procesas documentos más grandes:

```bash
aws lambda update-function-configuration --function-name MedicalRAG --memory-size 2048
```

📌 **AWS Lambda SnapStart ya está activado automáticamente para reducir tiempos de inicio.**  

aws lambda update-function-configuration --function-name MedicalRAG --snapstart-enabled
```

### **📌 Optimizar Consultas en DynamoDB**
DynamoDB ya usa **Auto Scaling**, pero puedes ajustar la capacidad manualmente:

aws dynamodb update-table --table-name MedicalData --provisioned-throughput ReadCapacityUnits=10,WriteCapacityUnits=5
```

📌 **Si tienes cargas variables de datos, Auto Scaling es la mejor opción.**  

---

## 🔹 5️⃣ Seguridad Avanzada y Cifrado de Datos

Medical-RAGArch-System ya implementa **cifrado AES-256 y autenticación con **. Puedes ajustarlos:

### **📌 AES-256 ya está habilitado; puedes personalizar su configuración**
```python
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

encrypted_data = cipher_suite.encrypt(b"Texto médico confidencial")
```

📌 **Nunca almacenes la clave de cifrado en texto plano.**  

### **📌 Configurar  para Protección de API**
```python
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # Expiración de tokens en 1 hora
```

📌 **Todos los accesos requieren autenticación con  para seguridad.**  

---

## 🔹 6️⃣ Escenarios de Personalización

📌 **Escenario 1: Uso estándar con respuestas rápidas**  
✅ **Configuración recomendada:**  
- Activar Redis con **caché de 1 hora** (`CACHE_EXPIRY = 3600`).  
- Usar un modelo NLP ligero (`distilbert-base-uncased`).  
- AWS Lambda con **1024 MB de memoria** para reducir costos.  

📌 **Escenario 2: Procesamiento intensivo de documentos con OCR**  
✅ **Configuración recomendada:**  
- Usar un modelo NLP avanzado (`facebook/bart-large-cnn`).  
- AWS Lambda con **2048 MB de memoria** para mejorar procesamiento.  
- Aplicar **filtros en OpenCV** para mejorar calidad de imágenes OCR.  

📌 **Escenario 3: Seguridad avanzada y acceso restringido**  
✅ **Configuración recomendada:**  
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

- Cifrar datos médicos con **AES-256** antes de almacenarlos.  
- Restringir acceso a la API configurando **CORS restrictivo**.  

---



### 📌 Mejoras de Optimización Aplicadas
Se han implementado optimizaciones adicionales para mejorar el rendimiento sin afectar el uso gratuito:

✅ **Carga optimizada de dependencias** en módulos críticos (`dynamodb_optimization.py`, `numba_optimization.py`, `tensorflow_optimization.py`).  
✅ **DAX en DynamoDB mejorado** con cifrado TLS (`aws/enable_dax.py`).  
✅ **SnapStart en AWS Lambda** confirmado y optimizado (`aws/lambda_snapstart.py`).  
✅ **Redis Cache** ahora usa TTL para reducir peticiones innecesarias a DynamoDB (`modules/cache/cache_redis.py`).  

Estas mejoras reducen el consumo de recursos y mejoran los tiempos de respuesta.

## 📌 Conclusión Final

✔ **El sistema está optimizado exclusivamente para `aarch64` y no es compatible con Windows.**  
✔ **Redis, AWS Lambda SnapStart y Auto Scaling en DynamoDB ya están configurados automáticamente.**  
✔ **Las consultas en tiempo real usan WebSockets para minimizar latencias.**  
✔ **La seguridad incluye autenticación con  y cifrado AES-256.**  
✔ **Cada parámetro se puede ajustar para personalizar velocidad, seguridad y costos.**  

📌 **Estas configuraciones avanzadas te permiten personalizar el sistema según las necesidades del entorno, desde uso ligero hasta procesamiento masivo de datos médicos.**  
---

## 📌 Diferencia entre Código Python y Comandos Bash

Medical-RAGArch-System incluye configuraciones que pueden ajustarse mediante **Python** y **comandos Bash**. Es importante saber **cuándo editar archivos y cuándo ejecutar comandos en la terminal**.

### 🔹 **Código Python en los documentos**
✔ **Los fragmentos de código Python ya están implementados en el sistema**.  
✔ **Solo necesitas modificarlos si deseas personalizar la configuración.**  
✔ **Si un archivo específico es mencionado (`api/main.py`, `nlp_config.py`), edítalo ahí.**  

📌 **Ejemplo de ajuste en Python (modificar en `nlp_config.py`)**  
```python
summarizer = pipeline('summarization', max_length=500, min_length=250, do_sample=True)
```

### 🔹 **Comandos Bash en los documentos**
✔ **Se ejecutan en la terminal (Linux/macOS o AWS CloudShell).**  
✔ **NO debes pegarlos dentro del código del proyecto.**  
✔ **Se usan para configurar AWS Lambda, Redis o DynamoDB manualmente.**  

📌 **Ejemplo de comando Bash (ejecutar en la terminal)**  
aws lambda update-function-configuration --function-name MedicalRAG --memory-size 2048
```

🚀 **Si no estás seguro de qué hacer, revisa si el ajuste ya está preconfigurado en el sistema antes de modificarlo.**  


# 🏗️ Arquitectura del Sistema - Medical-RAGArch-System

Medical-RAGArch-System utiliza una **arquitectura modular** optimizada para **procesamiento de datos médicos**, **integración con IA**, y **almacenamiento en la nube**.

✅ **Explicación de cada módulo y su función en el sistema.**  
✅ **Flujo de datos desde la carga de documentos hasta la consulta de ChatGPT.**  
✅ **Diagrama de arquitectura para visualizar la interacción entre componentes.**  
✅ **Opciones avanzadas de personalización para mejorar rendimiento.**  

---

## 🔹 1️⃣ Componentes Principales

Medical-RAGArch-System está compuesto por varios módulos que trabajan en conjunto:

| **Componente** | **Función** |
|--------------|------------------|
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

| **NLP (Intelligent Context)** | Procesa consultas, resume textos y extrae palabras clave. |
| **OCR + RAG** | Convierte imágenes en texto y analiza documentos médicos. |
| **DynamoDB** | Base de datos NoSQL utilizada para almacenar los documentos procesados. |
| **Redis Cloud** | Caché en memoria para reducir tiempos de consulta y optimizar respuesta. |
| **AWS Lambda** | Procesa documentos y consultas sin necesidad de servidores persistentes. |
| **GitHub Actions** | Automatiza el despliegue en AWS para mantener el sistema actualizado. |
| **WebSockets** | Permiten consultas en tiempo real sin necesidad de múltiples solicitudes HTTP. |

📌 **Notas**:  
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

- **Redis almacena consultas frecuentes para evitar accesos constantes a DynamoDB.**  
- **AWS Lambda permite ejecutar procesamiento sin depender de servidores dedicados.**  

---

## 🔹 2️⃣ Flujo de Datos en el Sistema

### **📌 Proceso desde la Carga hasta la Respuesta de ChatGPT**

1️⃣ **Carga de documentos** en AWS S3 o vía API REST.  
2️⃣ **OCR + RAG** procesan los documentos y extraen información clave.  
3️⃣ **Los datos se almacenan en DynamoDB** para consultas posteriores.  
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

5️⃣ **El módulo NLP procesa la consulta, resume texto y extrae palabras clave.**  
6️⃣ **Si la consulta ya ha sido realizada, Redis devuelve la respuesta desde caché.**  
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.


📌 **Ejemplo de una Consulta en Tiempo Real:**  
Si ChatGPT pregunta: `"¿Cuáles son los síntomas principales del documento ID 12345?"`  
El sistema:
- Extrae los síntomas clave usando NLP.  
- Revisa en Redis si la respuesta ya ha sido calculada.  
- Si no está en caché, consulta DynamoDB y procesa los datos en AWS Lambda.  
- Devuelve la respuesta a ChatGPT en segundos.  

📌 **Diagrama del Flujo de Datos:**  
```
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

                           |                 |
                          [Redis]       [AWS Lambda]
                             |                 |
                        [Respuesta a ChatGPT] <---
```

---

## 🔹 3️⃣ Configuración y Personalización de Componentes

Cada módulo del sistema puede ajustarse para optimizar rendimiento y funcionalidad:

✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

Si necesitas modificar el puerto o activar WebSockets, edita `api/main.py`:

```python
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])
```

📌 **Consejo:** **Limita los orígenes permitidos en producción** para evitar accesos no autorizados.

---

### **📌 Ajuste de NLP para Mejor Resumen de Textos**
Si deseas que el sistema genere respuestas más concisas o más detalladas:

```python
summarizer = pipeline('summarization', model="facebook/bart-large-cnn", max_length=250, min_length=100, do_sample=True)
```

📌 **Opciones avanzadas:**  
- **Mayor detalle** → Aumenta `max_length` a 500.  
- **Respuestas más breves** → Reduce `min_length` a 50.  

---

### **📌 Configuración de Redis para Optimizar Caché**
Si deseas cambiar el tiempo de almacenamiento en caché:

```python
CACHE_EXPIRY = 1800  # Expiración en 30 minutos
```

📌 **Consejo:** Reduce el tiempo de expiración si los datos cambian con frecuencia.

---

### **📌 Ajuste de AWS Lambda para Mayor Rendimiento**
Si necesitas más memoria en AWS Lambda para procesar documentos grandes:

aws lambda update-function-configuration --function-name MedicalRAG --memory-size 2048
```

📌 **Consejo:** Mayor memoria = ejecución más rápida, pero puede aumentar costos.

---

## 🔹 4️⃣ Escenarios de Uso

📌 **Escenario 1: Uso estándar con respuestas rápidas**  
✅ **Configuración recomendada:**  
- Activar Redis con un caché de **1 hora** (`CACHE_EXPIRY = 3600`).  
- Usar un modelo NLP liviano (`distilbert-base-uncased`).  
- AWS Lambda con **1024 MB de memoria** para reducir costos.  

📌 **Escenario 2: Procesamiento de documentos grandes**  
✅ **Configuración recomendada:**  
- Usar un modelo NLP detallado (`facebook/bart-large-cnn`).  
- AWS Lambda con **2048 MB de memoria** para documentos extensos.  
- Caché en Redis reducido a **30 minutos** para datos más dinámicos.  

📌 **Escenario 3: Consultas en tiempo real con ChatGPT**  
✅ **Configuración recomendada:**  
- Habilitar **WebSockets** (`uvicorn --ws`).  
- Reducir la latencia ajustando `WEBSOCKET_TIMEOUT = 20`.  
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.


---

## 📌 Conclusión

Medical-RAGArch-System está diseñado con una arquitectura **modular, escalable y optimizada** para diferentes escenarios:

✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

✔ **Redis optimiza la respuesta del sistema, reduciendo latencia en consultas frecuentes.**  
✔ **AWS Lambda permite ejecutar procesos sin servidores dedicados, reduciendo costos.**  
✔ **La arquitectura puede ajustarse según las necesidades del usuario, desde procesamiento ligero hasta uso intensivo con modelos avanzados.**  

📌 **Con una configuración adecuada, puedes lograr un balance entre costo, velocidad y precisión para adaptarlo a cualquier entorno.**  

---

## 🔹 5️⃣ Compatibilidad con Hardware y Software

Medical-RAGArch-System ha sido optimizado específicamente para **arquitecturas aarch64** y entornos basados en AWS.

### **📌 Arquitectura y Compilación**
✅ **Compilado y optimizado para:** `aarch64`
✅ **Eliminado soporte para:** `x86_64` (no compatible con la versión actual)  
✅ **Eliminado soporte para:** `x86_64`  
✅ **Optimización de librerías para menor consumo de recursos en ARM**  

### **📌 Sistemas Operativos Compatibles**
✅ **Distribuciones Linux (Ubuntu, Debian, Amazon Linux 2, Alpine)**  
✅ **Contenedores Docker en AWS Lambda y Graviton**  
✅ **Raspberry Pi 4 y Jetson Nano (para inferencia local en ARM64)**  

📌 **Nota:**  
- **El sistema NO es compatible con Windows**, ya que ha sido diseñado para ejecutarse en entornos basados en Linux.  
- **Si se necesita soporte en `x86_64`, habría que recompilar algunas dependencias con flags específicos para esa arquitectura.**  

### **📌 Entornos de Ejecución en la Nube**
Medical-RAGArch-System está optimizado para los siguientes entornos en la nube:

| **Proveedor** | **Recomendado** | **Motivo** |
|--------------|-------------|-------------|
| **AWS Lambda (aarch64)** | ✅ Sí | Optimización con SnapStart y menor costo en Graviton. |
| **Google Cloud Run** | ⚠️ Parcial | Puede ejecutarse, pero sin soporte directo para aarch64. |
| **Azure Functions** | ❌ No | No tiene soporte nativo para ARM64 en ambientes serverless. |
| **Docker (ARM64)** | ✅ Sí | Puede ejecutarse en contenedores Docker sobre Linux ARM. |

📌 **AWS Lambda con `Graviton` ofrece el mejor rendimiento y menor costo de ejecución.**  

---



### 📌 Mejoras de Optimización Aplicadas
Se han implementado optimizaciones adicionales para mejorar el rendimiento sin afectar el uso gratuito:

✅ **Carga optimizada de dependencias** en módulos críticos (`dynamodb_optimization.py`, `numba_optimization.py`, `tensorflow_optimization.py`).  
✅ **DAX en DynamoDB mejorado** con cifrado TLS (`aws/enable_dax.py`).  
✅ **SnapStart en AWS Lambda** confirmado y optimizado (`aws/lambda_snapstart.py`).  
✅ **Redis Cache** ahora usa TTL para reducir peticiones innecesarias a DynamoDB (`modules/cache/cache_redis.py`).  

Estas mejoras reducen el consumo de recursos y mejoran los tiempos de respuesta.

## 📌 Conclusión Final

✔ **Medical-RAGArch-System está optimizado para `aarch64` y ejecutándose en AWS Lambda con Graviton.**  
✔ **No está pensado para Windows ni `x86_64`, lo que permite una mejor eficiencia en entornos cloud.**  
✔ **Las mejores opciones de despliegue son AWS Lambda, Docker ARM64 y Raspberry Pi 4 para inferencia local.**  
✔ **Si se requiere compatibilidad con `x86_64`, hay que recompilar algunas dependencias específicas.**  

---


Medical-RAGArch-System incluye configuraciones que pueden ajustarse mediante **Python** y **comandos Bash**. Es importante saber **cuándo editar archivos y cuándo ejecutar comandos en la terminal**.

✔ **Los fragmentos de código Python ya están implementados en el sistema**.  
✔ **Solo necesitas modificarlos si deseas personalizar la configuración.**  
✔ **Si un archivo específico es mencionado (`api/main.py`, `nlp_config.py`), edítalo ahí.**  

📌 **Ejemplo de ajuste en Python (modificar en `nlp_config.py`)**  
```python
```

✔ **Se ejecutan en la terminal (Linux/macOS o AWS CloudShell).**  
✔ **NO debes pegarlos dentro del código del proyecto.**  
✔ **Se usan para configurar AWS Lambda, Redis o DynamoDB manualmente.**  

📌 **Ejemplo de comando Bash (ejecutar en la terminal)**  
aws lambda update-function-configuration --function-name MedicalRAG --memory-size 2048
```

🚀 **Si no estás seguro de qué hacer, revisa si el ajuste ya está preconfigurado en el sistema antes de modificarlo.**  



# 📌 Tabla de Contenidos

- [📖 Introducción](#introducción)
- [⚙️ Configuración y Personalización](#configuración-y-personalización)
- [🔄 Automatización y Despliegue](#automatización-y-despliegue)
- [📄 Ejemplos de Uso](#ejemplos-de-uso)
  - [📂 Subida y Procesamiento de Documentos](#ejemplos-de-uso---subida-y-procesamiento-de-documentos)
  - [🧠 Procesamiento de Texto y NLP](#ejemplos-de-uso---procesamiento-de-texto-y-nlp)
  - [🔄 Optimización y Caché](#ejemplos-de-uso---optimización-y-caché)
  - [⚡ WebSockets y Consultas en Tiempo Real](#ejemplos-de-uso---websockets-y-consultas-en-tiempo-real)
- [🔐 Optimización y Seguridad](#optimización-y-seguridad)
- [📌 Conclusión](#conclusión)

---


# 🔄 Automatización y Configuración en Medical-RAGArch-System

Medical-RAGArch-System está diseñado para minimizar la intervención del usuario, pero ciertos ajustes pueden requerir configuración manual para optimizar su funcionamiento.

✅ **Qué procesos están completamente automatizados.**  
✅ **Qué procesos requieren ajustes manuales y por qué.**  
✅ **Cómo personalizar la configuración para mejorar rendimiento y eficiencia.**  
✅ **Casos de uso para diferentes niveles de automatización.**  

---

## 🔹 1️⃣ Procesos Totalmente Automatizados


# 🚀 Integración con AWS (Lambda, DynamoDB, API Gateway)

Este proyecto utiliza múltiples servicios de **AWS** para mejorar su rendimiento, escalabilidad y disponibilidad.

## 📌 **Servicios Utilizados**

| Servicio      | Función en el Proyecto |
|--------------|------------------------|
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

| **DynamoDB** | Base de datos NoSQL optimizada para respuestas rápidas |
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

| **SnapStart** | Reduce los tiempos de arranque de Lambda |
| **DAX** | Acelera las consultas en DynamoDB |

## ⚙️ **Configuración Manual en AWS**
Si deseas configurar manualmente los servicios en AWS, sigue estos pasos:

### **1️⃣ Configurar AWS Lambda**
```bash
aws lambda create-function --function-name MedicalRAG --runtime python3.8 --role <IAM_ROLE> --handler api.main.lambda_handler
```

### **2️⃣ Configurar DynamoDB**
```bash
aws dynamodb create-table --table-name MedicalData --attribute-definitions AttributeName=id,AttributeType=S --key-schema AttributeName=id,KeyType=HASH --billing-mode PAY_PER_REQUEST
```

---

## 🛠️ **Configuración Automática con CDK**
Si prefieres desplegarlo automáticamente, usa los scripts de `aws/`:
```bash
cd aws/
python enable_dax.py  # Activa DAX en DynamoDB
python lambda_snapstart.py  # Habilita SnapStart en AWS Lambda
```




Estos procesos se ejecutan sin intervención manual una vez configurados:

| **Funcionalidad** | **Automatización** | **Explicación** |
|--------------|-------------|-------------|
| **Carga y procesamiento de documentos** | ✅ Sí | El sistema detecta automáticamente el tipo de documento y lo procesa. |
| **OCR automático** | ✅ Sí | Si el documento es una imagen escaneada, el OCR se activa sin necesidad de ajuste manual. |
| **Optimización de consultas con Redis** | ✅ Sí | Las consultas repetidas se almacenan en caché para reducir la carga en DynamoDB. |
| **Despliegue en AWS Lambda y DynamoDB con GitHub Actions** | ✅ Sí | El código se actualiza y despliega automáticamente sin intervención. |
| **Auto Scaling en DynamoDB** | ✅ Sí | Se ajusta la capacidad de la base de datos según la demanda del sistema. |
| **Generación de respuestas estructuradas para ChatGPT** | ✅ Sí | Las respuestas son resumidas y formateadas automáticamente antes de enviarlas. |

📌 **Notas**:  
- **Si subes un documento PDF, el sistema determina automáticamente si necesita OCR.**  
- **El almacenamiento en Redis está preconfigurado y optimizado.**  
- **AWS Lambda ajusta automáticamente los recursos según la carga.**  

---

## 🔹 2️⃣ Procesos que Requieren Configuración Manual


# 🚀 Optimización con Redis y Numba

Este proyecto utiliza **Redis Cloud** y **Numba** para mejorar el rendimiento en tiempo de respuesta y cálculos intensivos.

## 📌 **Optimización con Redis**

Redis se usa para **cachear respuestas frecuentes**, reduciendo la carga en DynamoDB.

### **📌 Configuración Manual de Redis**
1️⃣ Crea un clúster de Redis en AWS o usa una instancia local.  
2️⃣ Configura el archivo `config/redis_config.py` con las credenciales:

```python
REDIS_HOST = "redis-cluster.amazonaws.com"
REDIS_PORT = 6379
REDIS_REMOVED_SECRET
```

### **📌 Uso en el Código**
```python
import redis

cache = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True)
cache.set("consulta_usuario", resultado_procesado, ex=3600)  # Cache por 1 hora
```

---

## ⚡ **Optimización con Numba**
Numba acelera cálculos de Machine Learning y NLP optimizando operaciones matemáticas intensivas.

### **📌 Ejemplo de Uso**
```python
from numba import jit

@jit(nopython=True)
def calcular_metricas(datos):
    return sum(datos) / len(datos)
```




Algunas funciones necesitan intervención manual para ajustarse a escenarios específicos:

| **Funcionalidad** | **Intervención Manual** | **Motivo** |
|--------------|-------------|-------------|
| **Ajuste de umbral en OCR** | ⚠️ Sí | Dependiendo de la calidad de la imagen, puede ser necesario ajustar la precisión del OCR. |
| **Políticas de retención de datos en DynamoDB** | ⚠️ Sí | Por defecto, los datos se almacenan indefinidamente, pero pueden configurarse reglas de expiración. |
| **Modificación del NLP para respuestas más detalladas o resumidas** | ⚠️ Sí | Se puede modificar el nivel de resumen en el modelo de NLP. |
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

| **Seguridad y autenticación avanzada** | ⚠️ Sí | Si se necesita una capa extra de seguridad, se pueden modificar los métodos de autenticación. |

📌 **Ejemplo de ajuste en OCR:**  
Si un documento escaneado tiene mala calidad, se puede mejorar la detección ajustando `ocr_advanced.py`:

```python
ocr_engine.set_threshold(0.90)  # Mayor precisión, pero puede omitir texto con bajo contraste
```

📌 **Ejemplo de ajuste en DynamoDB:**  
Si no quieres almacenar documentos indefinidamente, puedes configurar una política de expiración:

aws dynamodb update-time-to-live --table-name MedicalData --time-to-live-specification Enabled=true,AttributeName=expiration_timestamp
```

📌 **Ejemplo de ajuste en NLP para ChatGPT:**  
Si deseas respuestas más extensas y detalladas en consultas:

```python
summarizer = pipeline('summarization', max_length=800, min_length=300, do_sample=True)
```

---

## 🔹 3️⃣ Casos Prácticos para Diferentes Niveles de Automatización


# 🤖 Modelos de Machine Learning y NLP

El sistema incluye modelos de **predicción y procesamiento de lenguaje natural (NLP)** para analizar documentos médicos.

## 📌 **Modelos Implementados**
| Módulo | Funcionalidad |
|--------|--------------|
| **ml_models.py** | Modelos de predicción y clasificación |
| **intelligent_context.py** | Procesamiento avanzado de lenguaje natural |
| **time_series.py** | Predicciones basadas en series temporales |

---

## ⚙️ **Cómo Personalizar los Modelos**

### **Modificar Parámetros del Modelo NLP**
Edita el archivo `config/nlp_config.json`:
```json
{
    "max_length": 500,
    "min_length": 200,
    "do_sample": true
}
```

### **Ejemplo de Uso en el Código**
```python
from transformers import pipeline

summarizer = pipeline("summarization", max_length=500, min_length=200, do_sample=True)
```




### **Escenario 1: Uso estándar con automatización total**  
🔹 **Tienes documentos en AWS S3 y deseas analizarlos automáticamente.**  
✅ **Solución:** Configura una regla en AWS Lambda para que procese cualquier archivo nuevo automáticamente.  

```json
{
  "source": "AWS-S3",
  "processing_mode": "AUTO"
}
```

🔹 **El sistema identificará el documento, aplicará OCR si es necesario y almacenará los datos en DynamoDB sin intervención manual.**  

---

### **Escenario 2: Seguridad Avanzada y Retención de Datos**  
🔹 **Requieres mayor control sobre los tiempos de expiración de los documentos.**  
✅ **Solución:** Configura políticas de retención en DynamoDB y habilita autenticación avanzada con .  

export TOKEN_EXPIRATION=3600  # Expiración de tokens en 1 hora
```

🔹 **Esto permitirá que solo usuarios autorizados puedan acceder a los documentos almacenados.**  

---

### **Escenario 3: Activar WebSockets para Consultas en Tiempo Real**  
🔹 **Quieres que ChatGPT pueda obtener respuestas sin esperar consultas HTTP tradicionales.**  
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.


uvicorn api.main:app --host 0.0.0.0 --port 8000 --ws
```

🔹 **Esto permitirá que las respuestas lleguen en tiempo real sin latencia adicional.**  

---

## 📌 Conclusión

Medical-RAGArch-System es altamente automatizable, pero ciertos procesos pueden ajustarse para mejorar la precisión y la seguridad:

✅ **Si necesitas un sistema completamente autónomo**, las funciones predeterminadas de automatización ya manejan la mayoría de los procesos.  
✅ **Si deseas control sobre la seguridad, tiempos de respuesta y ajustes avanzados, puedes configurar manualmente los módulos según las necesidades específicas.**  
✅ **Con la combinación correcta de automatización y ajustes manuales, puedes personalizar el sistema para adaptarse a cualquier entorno de trabajo.**  
---


Medical-RAGArch-System incluye configuraciones que pueden ajustarse mediante **Python** y **comandos Bash**. Es importante saber **cuándo editar archivos y cuándo ejecutar comandos en la terminal**.

✔ **Los fragmentos de código Python ya están implementados en el sistema**.  
✔ **Solo necesitas modificarlos si deseas personalizar la configuración.**  
✔ **Si un archivo específico es mencionado (`api/main.py`, `nlp_config.py`), edítalo ahí.**  

📌 **Ejemplo de ajuste en Python (modificar en `nlp_config.py`)**  
```python
```

✔ **Se ejecutan en la terminal (Linux/macOS o AWS CloudShell).**  
✔ **NO debes pegarlos dentro del código del proyecto.**  
✔ **Se usan para configurar AWS Lambda, Redis o DynamoDB manualmente.**  

📌 **Ejemplo de comando Bash (ejecutar en la terminal)**  
aws lambda update-function-configuration --function-name MedicalRAG --memory-size 2048
```

🚀 **Si no estás seguro de qué hacer, revisa si el ajuste ya está preconfigurado en el sistema antes de modificarlo.**  


# 📌 Ejemplos Avanzados en Medical-RAGArch-System

Este archivo detalla **casos de uso avanzados** con ejemplos prácticos sobre **integración con AWS, WebSockets, OCR avanzado, NLP y optimización de respuestas.**

---

## 🔹 1️⃣ Subida Avanzada de Documentos con AWS S3

Si los documentos ya están almacenados en AWS S3, puedes referenciarlos en lugar de subirlos manualmente.

### **📌 Petición API para registrar un documento de S3**
```json
{
  "document_url": "s3://medical-docs/documento.pdf"
}
```

📌 **Explicación:**  
- El sistema recuperará el documento directamente desde **AWS S3**.  
- Se aplicará OCR automáticamente si es necesario.  
- Se generará un `document_id` para futuras consultas.  

---

## 🔹 2️⃣ Personalización de Respuestas en NLP

Si deseas personalizar cómo el sistema resume documentos, puedes ajustar los parámetros en `intelligent_context.py`.

### **📌 Ajuste del modelo de NLP**
```python
summarizer = pipeline('summarization', model="facebook/bart-large-cnn", max_length=500, min_length=200, do_sample=True)
```

📌 **Opciones recomendadas:**  
✅ **Para respuestas más detalladas:** `max_length=800, min_length=300`  
✅ **Para respuestas más rápidas:** `max_length=250, min_length=100`  

---

## 🔹 3️⃣ Configuración de OCR con Preprocesamiento de Imágenes

Si un documento escaneado tiene baja calidad, puedes mejorar la precisión del OCR antes del procesamiento.

### **📌 Aplicar preprocesamiento con OpenCV**
```python
import cv2

image = cv2.imread("documento.jpg")
image = cv2.convertScaleAbs(image, alpha=1.5, beta=30)  # Ajusta brillo y contraste
cv2.imwrite("documento_mejorado.jpg", image)
```

📌 **Explicación:**  
- **Si el texto es muy claro**, reduce `alpha` para disminuir brillo.  
- **Si la imagen tiene ruido**, usa `cv2.GaussianBlur(image, (5, 5), 0)`.  

---

## 🔹 4️⃣ Optimización con Redis y DynamoDB

Redis ya está habilitado en el sistema. Puedes ajustar su tiempo de expiración para mejorar la eficiencia.

### **📌 Configuración de Redis**
```python
CACHE_EXPIRY = 3600  # Respuestas almacenadas durante 1 hora
```

📌 **Explicación:**  
✅ **Si los datos cambian con frecuencia**, reduce `CACHE_EXPIRY` a `600` segundos.  
✅ **Si consultas documentos estáticos**, aumenta el caché a `86400` segundos (1 día).  

---

## 🔹 5️⃣ WebSockets para Consultas en Tiempo Real

Para obtener respuestas inmediatas sin esperar una consulta HTTP, habilita WebSockets.

### **📌 Conectar WebSockets desde Python**
```python
import websockets
import asyncio

async def test_websocket():
    async with websockets.connect("ws://localhost:8000/ws") as websocket:
        await websocket.send("Resumen del documento 12345")
        response = await websocket.recv()
        print(response)

asyncio.run(test_websocket())
```

📌 **Beneficios:**  
✅ Respuestas en tiempo real sin múltiples peticiones HTTP.  
✅ Reducción de latencia en consultas de ChatGPT.  

---

## 📌 Conclusión

Estos ejemplos avanzados permiten maximizar el rendimiento del sistema con:  
✔ **Carga de documentos desde AWS S3.**  
✔ **Preprocesamiento de imágenes para OCR más preciso.**  
✔ **Optimización de Redis y DynamoDB para respuestas más rápidas.**  
✔ **Uso de WebSockets para comunicación en tiempo real.**  
✔ **Personalización del procesamiento NLP para mejorar respuestas.**  

---


Medical-RAGArch-System incluye configuraciones que pueden ajustarse mediante **Python** y **comandos Bash**. Es importante saber **cuándo editar archivos y cuándo ejecutar comandos en la terminal**.

✔ **Los fragmentos de código Python ya están implementados en el sistema**.  
✔ **Solo necesitas modificarlos si deseas personalizar la configuración.**  
✔ **Si un archivo específico es mencionado (`api/main.py`, `nlp_config.py`), edítalo ahí.**  

📌 **Ejemplo de ajuste en Python (modificar en `nlp_config.py`)**  
```python
```

✔ **Se ejecutan en la terminal (Linux/macOS o AWS CloudShell).**  
✔ **NO debes pegarlos dentro del código del proyecto.**  
✔ **Se usan para configurar AWS Lambda, Redis o DynamoDB manualmente.**  

📌 **Ejemplo de comando Bash (ejecutar en la terminal)**  
aws lambda update-function-configuration --function-name MedicalRAG --memory-size 2048
```

🚀 **Si no estás seguro de qué hacer, revisa si el ajuste ya está preconfigurado en el sistema antes de modificarlo.**  


# 📌 Ejemplos de Uso en Medical-RAGArch-System

✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.


---

## 🔹 1️⃣ Subir un Documento y Procesarlo

✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.


### **📌 Comando en Terminal (Linux/Mac)**
curl -X POST "https://tu-endpoint.com/upload" -H "Authorization: Bearer TU_TOKEN" -F "file=@documento.pdf"
```

### **📌 Respuesta esperada**
```json
{
  "message": "Documento recibido y procesado correctamente.",
  "document_id": "12345"
}
```

📌 **Nota:** Puedes subir archivos en formatos `.pdf`, `.jpg`, `.png`, `.txt`, y `.json`. Si el sistema detecta un documento escaneado, aplicará OCR automáticamente.

---

## 🔹 2️⃣ Consultar Información desde ChatGPT con Herramientas

Si ChatGPT necesita obtener un resumen de un documento, puede realizar la siguiente consulta:

### **📌 Petición desde ChatGPT**
```json
{
  "query": "Dame un resumen del documento con ID 12345",
  "source": "Medical-RAGArch-System"
}
```

### **📌 Respuesta esperada**
```json
{
  "response": "El documento 12345 trata sobre diabetes tipo 2 y su manejo con metformina."
}
```

📌 **Nota:** Si el documento aún no ha sido procesado, la respuesta indicará que no se encontraron datos.

---

## 🔹 3️⃣ Configurar OCR para Mayor Precisión

Si el OCR tiene dificultades para reconocer texto en imágenes de baja calidad, puedes aumentar la sensibilidad en `ocr_advanced.py`.

### **📌 Ajustar umbral de OCR en `ocr_advanced.py`**
```python
ocr_engine.set_threshold(0.85)  # Ajustar entre 0.5 y 0.95 según la calidad de las imágenes
```

📌 **Recomendaciones:**  
✅ **Si el texto es borroso**, usa un umbral más alto (`0.90+`).  
✅ **Si OCR detecta texto erróneo**, reduce el umbral (`0.75-`).  

---

## 🔹 4️⃣ Comunicación en Tiempo Real con WebSockets

✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.


✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

uvicorn app:app --host 0.0.0.0 --port 8000
```

2️⃣ **Conéctate al WebSocket con Python**
```python
import websockets
import asyncio

async def test_websocket():
    async with websockets.connect("ws://localhost:8000/ws") as websocket:
        await websocket.send("Dame un resumen del documento 12345")
        response = await websocket.recv()
        print(response)

asyncio.run(test_websocket())
```

📌 **Ventajas del WebSocket:**  
✅ Responde en tiempo real sin necesidad de nuevas peticiones HTTP.  
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.


---

## 🔹 5️⃣ Optimización de Procesamiento de Texto en NLP

Si quieres personalizar cómo el sistema procesa los textos, puedes modificar la configuración de `intelligent_context.py`.

### **📌 Ajustar la longitud del resumen NLP**
```python
summarizer = pipeline('summarization', max_length=250, min_length=100, do_sample=True)
```

📌 **Opciones:**  
✅ Si quieres **resúmenes más breves**, reduce `max_length` a 150.  
✅ Si necesitas más contexto, aumenta `max_length` a 500.  

---

## 🔹 6️⃣ Uso de Redis para Optimización de Consultas

Redis ya está habilitado en el sistema. Puedes optimizar su configuración para mejorar la eficiencia en consultas repetitivas.

### **📌 Configurar almacenamiento en caché en `redis_cloud.py`**
```python
import redis

cache = redis.StrictRedis(host="redis-instance-url", port=6379, db=0)

def get_cached_response(query):
    response = cache.get(query)
    if response:
        return response.decode("utf-8")
    return None
```

📌 **Beneficios de usar Redis:**  
✅ Reduce la carga en DynamoDB al evitar consultas repetidas.  
✅ Mejora la velocidad de respuesta para ChatGPT.  

---

## 🔹 7️⃣ AWS Lambda SnapStart para Mejora de Velocidad

Si el sistema se ejecuta en AWS Lambda, puedes habilitar SnapStart para reducir tiempos de inicio.

aws lambda update-function-configuration --function-name MedicalRAG --snapstart-enabled
```

📌 **Beneficios:**  
✅ Acelera la ejecución de Lambda hasta un **60% más rápido**.  
✅ Reduce los costos al evitar largos tiempos de espera.  

---

## 📌 Conclusión

Estos ejemplos cubren los usos más comunes dentro del sistema. Dependiendo de la carga de trabajo, puedes:
- **Optimizar el OCR** si procesas imágenes escaneadas.  
- **Usar WebSockets** para comunicación en tiempo real.  
- **Optimizar Redis** si se realizan muchas consultas repetitivas.  
- **Habilitar AWS SnapStart** para mejorar la velocidad de respuesta.  
---


Medical-RAGArch-System incluye configuraciones que pueden ajustarse mediante **Python** y **comandos Bash**. Es importante saber **cuándo editar archivos y cuándo ejecutar comandos en la terminal**.

✔ **Los fragmentos de código Python ya están implementados en el sistema**.  
✔ **Solo necesitas modificarlos si deseas personalizar la configuración.**  
✔ **Si un archivo específico es mencionado (`api/main.py`, `nlp_config.py`), edítalo ahí.**  

📌 **Ejemplo de ajuste en Python (modificar en `nlp_config.py`)**  
```python
```

✔ **Se ejecutan en la terminal (Linux/macOS o AWS CloudShell).**  
✔ **NO debes pegarlos dentro del código del proyecto.**  
✔ **Se usan para configurar AWS Lambda, Redis o DynamoDB manualmente.**  

📌 **Ejemplo de comando Bash (ejecutar en la terminal)**  
aws lambda update-function-configuration --function-name MedicalRAG --memory-size 2048
```

🚀 **Si no estás seguro de qué hacer, revisa si el ajuste ya está preconfigurado en el sistema antes de modificarlo.**  


### 🔹 **Interacción con Código Python y Comandos Bash**

Medical-RAGArch-System permite ajustar configuraciones y ejecutar acciones a través de código Python y comandos Bash.
Esta sección explica cuándo usar cada uno y proporciona ejemplos claros.

---

### 🔹 **Uso de Código Python**

✔ **Los fragmentos de código Python ya están implementados en el sistema.**
✔ **Solo necesitas modificarlos si deseas personalizar la configuración.**
✔ **Si un archivo específico es mencionado (`api/main.py`, `nlp_config.py`), edítalo ahí.**

📌 **Ejemplo de ajuste en Python (modificar en `nlp_config.py`)**
```python
summarizer = pipeline('summarization', max_length=500, min_length=250, do_sample=True)
```

📌 **Otros ejemplos de código en Python utilizados en diferentes secciones:**

- **WebSockets:** Comunicación en tiempo real con consultas optimizadas.
- **OCR con OpenCV:** Mejora de precisión en documentos escaneados.
- **Optimización de caché con Redis:** Acelerar consultas frecuentes.

---

### 🔹 **Uso de Comandos Bash**

✔ **Se ejecutan en la terminal (Linux/macOS o AWS CloudShell).**
✔ **NO debes pegarlos dentro del código del proyecto.**
✔ **Se usan para configurar AWS Lambda, Redis o DynamoDB manualmente.**

📌 **Ejemplo de comando Bash (ejecutar en la terminal)**
aws lambda update-function-configuration --function-name MedicalRAG --memory-size 2048
```

📌 **Otros comandos útiles:**

- **Configurar OCR avanzado en AWS Lambda**
- **Habilitar SnapStart para mejorar tiempos de ejecución**
- **Ajustar escalado automático en DynamoDB**

---

















---

# Medical-RAGArch-System

## 📌 ¿Qué es este proyecto?
Medical-RAGArch-System es un sistema de **IA aplicada a documentos médicos**, que permite:
- **Almacenar, procesar y recuperar información estructurada** de documentos médicos.
- **Optimizar la infraestructura en la nube con AWS Lambda y DynamoDB.**
- **Automatizar despliegues y mantenimiento** con GitHub Actions y AWS CDK.

---

✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

✅ **Ejecutar API REST de manera eficiente en la nube.**  
✅ **Escalar automáticamente sin intervención del usuario.**  
✅ **Desplegarse sin configuración manual.**  

✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

```python
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

from mangum import Mangum

✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.


@app.get("/status")
async def status():
    return {"status": "OK", "service": "Medical-RAGArch-System"}

handler = Mangum(app)
```

---

## 🔹 2️⃣ Optimización de AWS Lambda y DynamoDB
El sistema ahora implementa **optimización avanzada en AWS Lambda y DynamoDB**, incluyendo:
✅ **Compatibilidad con arquitectura ARM64 (`aarch64`)** para mejorar eficiencia.  
✅ **Uso de DynamoDB DAX** para consultas más rápidas.  
✅ **Activación de Adaptive Capacity en DynamoDB** para escalado dinámico.  
✅ **Cache en API Gateway** para mejorar tiempos de respuesta.  
✅ **Implementación automática de SnapStart en AWS Lambda** para reducir latencia.  

🔹 **Ejemplo de configuración automática de SnapStart en AWS Lambda:**  
```python
import boto3

lambda_client = boto3.client("lambda")
response = lambda_client.update_function_configuration(
    FunctionName="MedicalRAGLambda",
    SnapStart={"ApplyOn": "PublishedVersions"}
)
print("SnapStart Enabled:", response)
```

---

## 🔹 3️⃣ Personalización de NLP (Procesamiento de Lenguaje Natural)
Ahora el sistema permite **configurar dinámicamente** el procesamiento de lenguaje natural.  
✅ **Ajuste de modelos NLP desde un archivo JSON.**  
✅ **Configuración de longitud de resumen.**  
✅ **Opción de habilitar/deshabilitar muestreo (`do_sample`).**  

🔹 **Archivo de configuración `config/nlp_config.json`:**  
```json
{
    "model_name": "facebook/bart-large-cnn",
    "max_length": 150,
    "min_length": 50,
    "do_sample": false
}
```

---

## 🔹 4️⃣ Integración de WebSockets con AWS Lambda
Se ha mejorado el soporte para **WebSockets en AWS Lambda**, lo que permite:  
✅ **Comunicación en tiempo real sin configuración manual.**  
✅ **Compatibilidad con API Gateway y escalado automático.**  
✅ **Uso sin costos obligatorios (solo consumo según tráfico).**  

✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

```python
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

from mangum import Mangum

✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.


class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_message(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_message(f"Mensaje: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)

handler = Mangum(app)
```

---

## ✅ **Conclusión**
Este sistema ha sido actualizado para incluir:  
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

✅ **Optimización avanzada de DynamoDB y Lambda.**  
✅ **Personalización de NLP sin tocar el código.**  
✅ **WebSockets eficientes y sin costos ocultos.**  

---


---

## 🔹 **Automatización de Seguridad con AWS Secrets Manager**

Este sistema ahora **gestiona automáticamente claves de cifrado** mediante **AWS Secrets Manager**, mejorando la seguridad sin intervención del usuario.

### 📌 **1️⃣ ¿Cómo Funciona?**

- **`aws/secrets_manager.py`** crea y recupera claves automáticamente en AWS Secrets Manager.
- **`config/aes_config.py`** obtiene la clave AES-256 de AWS en lugar de almacenarla en el código.  
- **`config/_config.py`** obtiene la clave  automáticamente sin intervención del usuario.

### 📌 **2️⃣ Configuración Automática**

La primera vez, ejecuta este comando para inicializar los secretos en AWS:  
```bash
python aws/secrets_manager.py
```

Esto **creará automáticamente las claves en AWS Secrets Manager** y estarán disponibles para el sistema.

---

## 🔹 **Optimización del Despliegue en AWS Lambda**

El despliegue en AWS Lambda ahora es **más rápido y eficiente**, gracias a la optimización en la instalación de dependencias.

### 📌 **1️⃣ ¿Qué Cambió?**

- **Ahora usa `--prefer-binary` en la instalación de dependencias** para evitar errores con paquetes sin binarios precompilados.
- **Se ha actualizado `.github/workflows/deploy.yml`** para optimizar el tamaño del paquete de despliegue.

### 📌 **2️⃣ Desplegar en AWS Automáticamente**

Para desplegar en AWS Lambda sin intervención manual, solo haz un `push` al repositorio:  
```bash
git push origin main
```

Esto activará **GitHub Actions** y el sistema se actualizará automáticamente en AWS.

---

## 🔹 **Ubicación de Archivos Modificados**

| Archivo | Ubicación |
|---------|----------|
| `secrets_manager.py` | `aws/secrets_manager.py` |
| `aes_config.py` | `config/aes_config.py` |
| `_config.py` | `config/_config.py` |
| `deploy.yml` | `.github/workflows/deploy.yml` |

Estos cambios garantizan **más seguridad, transparencia y eficiencia** en el despliegue del sistema.



## 🔥 Actualización: Integración de Streamlit y DynamoDB

### 🆕 Cambios recientes en esta versión:
1. **Nuevo Frontend en Streamlit (`frontend/streamlit_interface.py`)**
   - **Autenticación en ChatGPT "Chat"** con opción para cuentas gratuitas y de pago.
   - **Carga de documentos médicos con almacenamiento en DynamoDB.**
   - **Selección de prompts sin mostrar su estructura interna.**
   - **Interacción con el backend y redirección de consultas.**

2. **Backend actualizado (`api/main.py` y `api/dynamodb_handler.py`)**
   - **Manejo de almacenamiento y recuperación de documentos en DynamoDB.**
   - **Endpoints para interactuar con la interfaz Streamlit.**

3. **Prompt modificado para la nueva arquitectura.**

4. **Actualización de `requirements.txt`** (sin alterar el orden original).
   - **Se agregaron `prophet` y `redis` solo si no estaban ya presentes.**

### 🚀 Cómo Ejecutarlo
1. **Instalar dependencias:**  
   ```bash
   pip install -r requirements.txt
   ```
✅ **Punto de Conexión en AWS Lambda:**
- La conexión con los modelos de IA se realiza directamente a través de AWS Lambda.
- FastAPI **ya no se usa** como punto de conexión dentro de AWS Lambda.

   ```bash
   uvicorn api.main:app --host 0.0.0.0 --port 8000
   ```
3. **Ejecutar Streamlit:**  
   ```bash
   streamlit run frontend/streamlit_interface.py
   ```

⚠️ **Nota:** Se recomienda probar en un entorno real para validar `prophet` y `redis` correctamente.


## 🔥 Integración Automática con ChatGPT "Chat"

### 🆕 Nueva Funcionalidad:
- **Inicio de sesión automático en ChatGPT "Chat"** sin intervención del usuario.
- **Envío y recepción de mensajes a ChatGPT "Chat"** mediante Selenium.
- **Guardado y reutilización de sesión con cookies** para evitar múltiples inicios de sesión.
- **Descarga automática de ChromeDriver** sin requerir configuración manual.

### 🚀 Cómo Usarlo
1. **Instalar dependencias:**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Ejecutar la automatización de ChatGPT:**  
   ```bash
   streamlit run frontend/chatgpt_automation.py
   ```

3. **Iniciar sesión con tu cuenta de ChatGPT "Chat".**  
4. **Escribir mensajes en la interfaz y recibir respuestas automáticamente.**  

⚠️ **Nota:** Asegúrate de que tu cuenta de ChatGPT "Chat" está activa antes de usar esta funcionalidad.


## 🔥 Integración de Prompts en la Interfaz

### 🆕 Nueva Funcionalidad:
- **Carga automática de los prompts guardados en el sistema** (`scripts/prompts.json`).
- **Selección de prompts desde la interfaz de Streamlit.**
- **Visualización del prompt elegido sin mostrar su estructura interna.**
- **Interacción con ChatGPT "Chat" dentro de la interfaz.**
- **Opción para subir documentos médicos y almacenarlos en DynamoDB.**

### 🚀 Cómo Usarlo
1. **Instalar dependencias:**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Ejecutar la interfaz de usuario:**  
   ```bash
   streamlit run frontend/streamlit_interface.py
   ```

3. **Seleccionar un prompt desde la interfaz de Streamlit.**  
4. **Responder las indicaciones de ChatGPT a través de la interfaz.**  
5. **Subir documentos médicos si el prompt lo requiere.**  

⚠️ **Nota:** Asegúrate de ejecutar `scripts/update_prompts.py` antes para actualizar los prompts desde GitHub.


---

## ⚠️ **IMPORTANTE: Uso recomendado con ChatGPT en modo chat**

**Razones por las que se recomienda esta opción:**

✅ **Funciones avanzadas exclusivas**:  
- Esto permite un mejor análisis de documentos y biomarcadores.  

✅ **Posibilidad de uso gratuito**:  

📌 **Recomendación**: Si deseas usar este sistema sin costo, utiliza **ChatGPT en modo chat** en lugar de la API.  

---

## 🔹 **Elección de IA y Modelos**

Ahora puedes seleccionar **qué IA deseas usar** para procesar consultas médicas.  
Por defecto, se recomienda **ChatGPT en modo chat** por sus funciones avanzadas y acceso gratuito.  

### ✅ **Opciones Disponibles**
| IA | Modelos Disponibles | Gratis | Notas |
|----|--------------------|--------|-------|
| **ChatGPT (Modo Chat)** | GPT-4 Turbo (Recomendado), GPT-4, GPT-3.5 | ✅ Sí | Acceso gratuito con cuenta Free |
| **Gemini (Google)** | Gemini 1.5 (Beta), Gemini 1.0 | ✅ Sí | ⚠️ Menos contexto que ChatGPT |
| **Claude (Anthropic)** | Claude 3 Opus, Claude 2 | ❌ No | ⚠️ Requiere cuenta paga |
| **Mistral AI** | Mistral-7B, Mixtral | ❌ No | ⚠️ Mejor para programación que medicina |

📌 **Recomendación:** Si deseas usar el sistema **gratis**, elige **ChatGPT (Modo Chat) o Gemini**.  

---

### 📌 **Cómo Funciona la Selección de IA**
1. **Selecciona la IA** en la interfaz.  
2. **Elige el modelo** disponible para esa IA.  
3. **Si una IA no está implementada**, aparecerá un aviso.  
4. **Si la IA requiere pago, se mostrará una advertencia.**  

📢 **Si una IA no ofrece las mismas funciones que ChatGPT en modo chat, se indicará en la interfaz.**  

---

## 🔹 **Modelos de IA Gratuitos y de Pago**

El sistema ahora permite seleccionar **tanto modelos gratuitos como de pago** en varias IAs.  
Si tienes una cuenta premium en alguna de ellas, puedes aprovechar modelos más avanzados.

### ✅ **Opciones Disponibles**
| IA | Modelos Gratuitos | Modelos de Pago | Notas |
|----|------------------|----------------|-------|
| **ChatGPT (Modo Chat)** | GPT-4 Turbo, GPT-3.5 | GPT-4 🔒 | Recomendado por funciones avanzadas |
| **Gemini (Google)** | Gemini 1.5, Gemini 1.0 | ❌ No disponible | ⚠️ Menos contexto que ChatGPT |
| **Claude (Anthropic)** | Claude 2 | Claude 3 Opus 🔒 | ⚠️ Menor soporte en análisis médicos |
| **Mistral AI** | Mistral-7B | Mixtral 🔒 | ⚠️ Más orientado a programación |

📌 **Recomendación:** Si no tienes cuenta premium, usa **ChatGPT en modo chat o Gemini 1.5**.  

---

## 🔒 **Autenticación Segura y Protección de Credenciales**

Para modelos de pago, el usuario debe ingresar su **API Key**.  
📌 **El sistema protege las credenciales con cifrado AES-256** antes de enviarlas al backend.  

✅ **Medidas de seguridad implementadas:**  
- **Las credenciales se cifran antes de su uso.**  
- **No se almacenan en texto plano en el frontend.**  
- **Se desencriptan solo en la sesión activa del usuario.**  

📢 **Advertencia:** Nunca compartas tu API Key con terceros.  

---

## 🔹 **IAs Compatibles: Modelos Gratuitos y de Pago**

Ahora el sistema soporta múltiples IAs con sus versiones **gratuitas y premium**.  
Si tienes cuenta premium en alguna IA, puedes aprovechar modelos más avanzados.  

### ✅ **Opciones Disponibles**
| IA | Modelos Gratuitos | Modelos de Pago | Notas |
|----|------------------|----------------|-------|
| **ChatGPT (Modo Chat)** | GPT-4 Turbo, GPT-3.5 | GPT-4 🔒 | Recomendado por funciones avanzadas |
| **Gemini (Google)** | Gemini 1.5, Gemini 1.0 | ❌ No disponible | ⚠️ Menos contexto que ChatGPT |
| **Claude (Anthropic)** | Claude 2 | Claude 3 Opus 🔒 | ⚠️ Menor soporte en análisis médicos |
| **Mistral AI** | Mistral-7B | Mixtral 🔒 | ⚠️ Más orientado a programación |
| **Llama (Meta AI)** | Llama 3, Llama 2 | Llama 3-70B 🔒 | ⚠️ Menos optimizado para lenguaje médico |
| **Cohere AI** | Command-R | Command-R+ 🔒 | ⚠️ Limitado en consultas médicas avanzadas |

📌 **Recomendación:** Si no tienes cuenta premium, usa **ChatGPT en modo chat, Gemini o Llama 3**.  

---

## 📌 **Comparación con ChatGPT**

📢 **ChatGPT sigue siendo la opción recomendada** porque:  
- **Tiene mejor acceso a funciones avanzadas en modo chat.**  
- **Puede usarse gratis sin restricciones significativas.**  
- **Soporta consultas médicas mejor que otras IAs.**  

Si eliges otra IA, ten en cuenta que algunas pueden tener **menos contexto** o **menor precisión** en temas médicos.  
---

## 🔹 Mejoras y Nuevas Funcionalidades en esta Versión

### ✅ Recuperación Flexible de Documentos en DynamoDB
Ahora se pueden solicitar **cualquier tipo de documentos almacenados** en DynamoDB, incluyendo:
- **Analíticas médicas**
- **Diagnósticos clínicos**
- **Informes médicos**

📌 **Ejemplo de uso:**  
Para obtener los últimos **5 informes médicos**, la consulta sería:
```
GET /retrieve_documents/?document_type=informe_medico&limit=5
```

### ✅ Comparación de Biomarcadores en Backend
Ahora se pueden solicitar biomarcadores de múltiples maneras:
- **Solo fuera de rango.**
- **En rango y fuera de rango.**
- **Biomarcadores complementarios para evaluar evolución.**

📌 **Ejemplo de uso:**  
Para analizar biomarcadores incluyendo los que están dentro del rango y complementarios:
```
POST /analyze_biomarkers/
{
    "documents": [...],
    "include_complementary": true,
    "include_in_range": true
}
```

### ✅ Frontend Optimizado para ChatGPT
El frontend ahora:
- Permite elegir **qué biomarcadores enviar a ChatGPT.**
- Permite recuperar cualquier tipo de documento desde DynamoDB.
- Permite filtrar los biomarcadores que se envían a ChatGPT, asegurando respuestas más precisas.

📌 **Ejemplo de flujo completo:**
1. **El usuario pregunta:** "Compárame mis últimas 5 analíticas e identifica tendencias de glucosa."
2. **El backend obtiene los datos y los analiza.**
3. **Solo los datos relevantes son enviados a ChatGPT.**

---

### 🔧 Posibles Ajustes y Configuraciones
1. **Si DynamoDB cambia de nombre**, actualizarlo en `.env` y `api/dynamodb_handler.py`.
2. **Si se requieren más tipos de documentos**, simplemente enviarlos en `document_type`.
3. **Si ChatGPT necesita más contexto**, modificar `frontend/chatgpt_automation.py` para ajustar el prompt.


## 🚀 Implementación de APIs de IA en Medical-RAGArch-System

Se ha implementado soporte para múltiples IAs en el sistema, asegurando compatibilidad tanto con **modo chat (cuando es posible) como con APIs**.  
Las siguientes IAs han sido integradas correctamente:

| **IA**       | **Modo Chat** | **API (Pago)** | **Notas** |
|-------------|--------------|----------------|-----------|
| **Gemini (Google)** | ✅ Sí | ✅ Sí | Gemini 1.5 soportado. |
| **Claude (Anthropic)** | ❌ No | ✅ Sí | Solo API disponible. |
| **Mistral AI** | ❌ No | ✅ Sí | Solo API disponible. |
| **Llama (Meta AI)** | ❌ No | ✅ Sí | Solo API disponible. |
| **Cohere AI** | ❌ No | ✅ Sí | Solo API disponible. |
| **DeepSeek AI** | ✅ Sí | ✅ Sí | Nuevo soporte añadido. |

### 📌 Características clave de la implementación:
1. **Compatibilidad con cuentas gratuitas y de pago**: Se verifica si el usuario tiene cuenta gratuita o premium antes de usar la API.  
2. **Modo chat habilitado donde es posible**: Para maximizar capacidades, el sistema usa modo chat en IAs que lo soportan.  
3. **DeepSeek AI ahora es compatible**: Se ha añadido soporte completo para DeepSeek.  
4. **Configuración de claves API**: Cada IA requiere una clave API en las variables de entorno correspondientes.  

### 🔧 **Cómo configurar las claves API**:
Debes añadir tus claves API en las variables de entorno antes de ejecutar el sistema. Ejemplo en Linux:
```bash
export GEMINI_REMOVED_SECRET
export ANTHROPIC_REMOVED_SECRET
export MISTRAL_REMOVED_SECRET
export LLAMA_REMOVED_SECRET
export COHERE_REMOVED_SECRET
export DEEPSEEK_REMOVED_SECRET
```
Si usas Windows, puedes configurarlas con:
```powershell
$env:GEMINI_REMOVED_SECRET
```

### 🛠 **Ejemplo de uso en código**
Para usar cualquiera de estas IAs, simplemente importa su clase y haz una consulta:
```python

print(response)
```

---

## 🔒 Implementación de Zero Trust con Caché en Redis Cloud Essentials y EFS
- **Ahora la autenticación sigue un modelo de Zero Trust con doble capa de caché (Redis + EFS).**
- **Redis Cloud Essentials almacena tokens temporalmente para reducir latencia.**
- **EFS se usa como respaldo para mantener tokens de sesión persistentes.**

### 🛠️ Cómo Funciona
- Al recibir una solicitud, primero se revisa la caché en Redis Cloud Essentials.
- Si el usuario ya ha sido autenticado recientemente, se usa la caché.
- Si no, se valida la identidad en tiempo real y se almacena el resultado en Redis y EFS.

### 🔄 Beneficios de la Implementación
- **Mayor seguridad:** Zero Trust garantiza que cada acceso sea validado dinámicamente.
- **Menor latencia:** Redis Cloud Essentials acelera la autenticación sin comprometer seguridad.
- **Persistencia:** Redis maneja datos en memoria y EFS asegura sesiones entre reinicios.

### 🔧 Configuración Necesaria
- Se debe configurar Redis Cloud Essentials con `REDIS_HOST` y `REDIS_PASSWORD`.
- AWS Lambda ya está preparado para conectar con EFS (`/mnt/efs/cache`).
- No se requieren claves API, la autenticación se maneja con IAM y contexto dinámico.


## 📌 Actualización de Integraciones y Seguridad

### ✅ **1. Integración de `sources_config.yaml` en módulos clave**
Se ha implementado la jerarquización y validación de fuentes en:

- **`intelligent_context.py`** → Ahora utiliza `sources_config.yaml` para aplicar reglas de fuentes permitidas en el análisis de contexto.
- **`supplement_interaction_validation.py`** → Ahora valida los suplementos usando únicamente fuentes permitidas según la jerarquización.

Ambos módulos ahora garantizan que solo se utilicen **fuentes confiables** definidas en la configuración.

---

### ✅ **2. Verificación de Seguridad Final**
Se realizó un **análisis exhaustivo del código** y se corrigieron los siguientes aspectos:

- 🔒 **Eliminación de todas las referencias a JWT y autenticación insegura.**
- 🔒 **Migración completa a TLS 1.3 en todos los módulos.**
- 🔒 **Corrección de `requirements.txt` agregando dependencias faltantes (AWS CDK, Dask, Matplotlib, Plotly).**
- 🔒 **Verificación de reglas de fuentes y almacenamiento seguro de datos.**

El sistema ahora cumple con **los más altos estándares de seguridad y privacidad**.

---

### ✅ **3. Funcionalidad mejorada en carga y análisis de analíticas**
- 🏥 **El sistema ya reconoce automáticamente las "3 últimas analíticas"** y las utiliza en los análisis.
- 📊 **Los módulos de generación de reportes y validación de suplementos ahora solo trabajan con fuentes confiables.**
- ⚡ **No se requieren configuraciones adicionales para estas funcionalidades.**

---

🔹 **Todo está documentado y listo.** El sistema ahora **es más seguro, eficiente y estructurado**.
