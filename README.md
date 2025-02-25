
# Medical-RAGArch-System

## Descripción del Proyecto
Medical-RAGArch-System es un sistema avanzado para el análisis de datos médicos, predicciones de series temporales, y gestión de interacciones de medicamentos y suplementos. Está optimizado exclusivamente para `aarch64`, asegurando el máximo rendimiento y compatibilidad.

---

# Instalación en Windows 10
1. Descomprime el archivo ZIP en una carpeta de tu elección.
2. Ejecuta el archivo `install_windows10.bat` como Administrador.
3. El script verificará automáticamente si Python y pip están instalados:
   - Si no están instalados, **descargará e instalará Python 3.9.13**.
   - Creará y activará un **entorno virtual**.
   - Instalará todas las dependencias desde `requirements.txt`.
4. Una vez completada la instalación, el entorno estará listo para usarse.

---

# Despliegue en GitHub y DynamoDB
### Sincronización con GitHub
- El proyecto está configurado para **sincronizarse automáticamente con GitHub** utilizando **GitHub Actions**.
- Cada vez que se hace un `push` en el branch `main`, se inicia un despliegue automatizado.

### Despliegue en DynamoDB
- La tabla `MedicalRAGArchData` se crea automáticamente en **DynamoDB** con:
  - `RecordID` como clave primaria.
  - **5 Unidades de Lectura y Escritura** para rendimiento optimizado.

### Despliegue en AWS Lambda
- El código se despliega automáticamente en **AWS Lambda**, maximizando el rendimiento y la escalabilidad.
- Utiliza el paquete de despliegue `deployment-package.zip`.

---

# OCR (Reconocimiento Óptico de Caracteres)
### ¿Qué es y para qué sirve?
- **OCR (Optical Character Recognition)** permite extraer texto de imágenes y documentos escaneados.
- Utilizado para **analizar resultados médicos en formato de imagen** (ej. PDFs escaneados).

### ¿Por qué se ha implementado?
- Para **automatizar la extracción de datos** de documentos médicos sin necesidad de ingresarlos manualmente.
- **Compatibilidad multilenguaje** para reconocer texto en varios idiomas.

### ¿Cómo funciona y cómo se usa?
- Implementado con **pytesseract**, **Pillow** y **langdetect**.
- **pytesseract** convierte imágenes en texto.
- **Pillow** preprocesa las imágenes.
- **langdetect** detecta el idioma automáticamente.
- **Uso:** Coloca las imágenes en la carpeta `input_images/` y ejecuta `ocr_processing.py`.

---

# Cifrado en AES-256 y JWT
### ¿Qué es y para qué sirve?
- **AES-256**: Algoritmo de cifrado avanzado que protege datos sensibles.
- **JWT (JSON Web Tokens)**: Se utiliza para **autenticación segura** y **protección de tokens de acceso**.

### ¿Por qué se ha implementado?
- Para **proteger información médica sensible** y **cumplir con normativas de seguridad** como **GDPR** y **HIPAA**.
- Para **evitar el acceso no autorizado** a datos médicos y credenciales de usuarios.

### ¿Cómo funciona y cómo se usa?
- **AES-256** cifra los datos localmente y en GitHub.
- **JWT** se utiliza para autenticar usuarios y proteger tokens.
- Las claves de cifrado se almacenan en `config/security.env` y se cargan automáticamente.
- **Uso:** Ejecuta `encryption.py` para cifrar/desencriptar datos.

---

# Integración de FastAPI en AWS Lambda
### ¿Qué es y para qué sirve?
- **FastAPI** es un framework de alto rendimiento para construir APIs.
- **AWS Lambda** permite ejecutar el backend sin gestionar servidores.

### ¿Por qué se ha implementado?
- Para **maximizar el rendimiento** y **escalabilidad** de las APIs médicas.
- Para **reducir costos de infraestructura** usando un modelo **serverless**.

### ¿Cómo funciona y cómo se usa?
- Configurado para **desplegarse automáticamente en AWS Lambda** usando **GitHub Actions**.
- **FastAPI** maneja las consultas médicas y el backend.
- **AWS Lambda** ejecuta las funciones de manera **serverless**.
- **Uso:** Realiza un `git push` en `main` para desplegar automáticamente en AWS.

---

# Seguridad Avanzada (AWS IAM Roles y Protección de Tokens)
### ¿Qué es y para qué sirve?
- **AWS IAM Roles** restringe el acceso y permisos en AWS.
- **Protección de Tokens** asegura que **ningún token o clave API** quede expuesta.

### ¿Por qué se ha implementado?
- Para **cumplir con las mejores prácticas de seguridad en AWS**.
- Para **evitar accesos no autorizados** a bases de datos y APIs.

### ¿Cómo funciona y cómo se usa?
- Configurado con **mínimo privilegio** para limitar permisos en AWS.
- **Tokens y claves API** están **cifrados en AES-256** en `security.env`.
- **Uso:** Los permisos y roles se configuran automáticamente en el despliegue.

---

# Internacionalización y Localización
### ¿Qué es y para qué sirve?
- **i18n y l10n** adaptan la interfaz y análisis médico al **idioma y región del usuario**.
- Soporta **múltiples formatos de fecha** y **terminología médica regional**.

### ¿Por qué se ha implementado?
- Para **adaptarse a usuarios internacionales**.
- Para **evitar errores en la interpretación de datos médicos** debido a formatos regionales.

### ¿Cómo funciona y cómo se usa?
- Utiliza **babel** para la localización de fechas y texto.
- **langdetect** detecta el idioma automáticamente.
- **Uso:** Detecta automáticamente la configuración regional del usuario.

---

# WebSockets Mejorada (Tiempo Real y Bidireccional)
### ¿Qué es y para qué sirve?
- **WebSockets** permite **comunicación en tiempo real** y **bidireccional**.
- Se utiliza para **alertas inmediatas** y **actualizaciones en vivo**.

### ¿Por qué se ha implementado?
- Para **analizar datos clínicos en tiempo real**.
- Para **notificaciones automáticas** ante valores críticos en analíticas.

### ¿Cómo funciona y cómo se usa?
- Implementado con **FastAPI WebSockets** y **asyncio**.
- Permite **comunicación bidireccional** entre cliente y servidor.
- **Uso:** Las alertas en tiempo real se activan automáticamente.

---

# Desarrollado y Mantenido por:
- **Medical-RAGArch-Team**

# Contacto
Si tienes alguna pregunta o necesitas soporte, contacta con el equipo de desarrollo.

---

## 🚀 Configuración Automática y Preconfigurada

### ✅ Token de GitHub y Contraseña del ZIP Preconfigurados

- **No necesitas configurar nada** para el acceso a los prompts.
- **El token de solo lectura y la contraseña del ZIP** están **preconfigurados y codificados en Base64**.
- **Funciona automáticamente** al ejecutar el proyecto.
- **No necesitas configurar variables de entorno** ni `.env`.

### 🔒 Seguridad y Privacidad
- **El token de solo lectura solo tiene permisos de lectura**:
  - No puede modificar ni eliminar nada en el repositorio.
  - No puede acceder a otros repositorios.
- **La contraseña del ZIP está en Base64**, no en texto plano.
- **El descifrado ocurre automáticamente en tiempo de ejecución**.
- **Totalmente transparente y seguro**.

### ⚙️ Ejecución Automática
- Para actualizar los prompts automáticamente, simplemente ejecuta:
  ```sh
  python scripts/update_prompts.py
  ```
- **No se necesita configuración manual**.
- **Funciona automáticamente** y **sin intervención**.

### 📁 Flujo Completo
1. **El token y la contraseña son descifrados automáticamente**.
2. **El ZIP de prompts se descarga del repositorio privado**.
3. **El ZIP se descomprime automáticamente** utilizando la contraseña.
4. **Los prompts se sincronizan automáticamente en DynamoDB**.

### ❗️ Notas Importantes
- **No necesitas modificar el código ni las configuraciones**.
- **Todo está preconfigurado y listo para usar**.


## 🔒 Seguridad con AES-256-CBC

### ✅ Token de GitHub Cifrado en AES-256-CBC

- **El token de solo lectura está cifrado en AES-256-CBC**.
- **Utiliza la contraseña proporcionada en Base64** para el descifrado.
- **El token nunca se expone en texto plano**.
- **El descifrado ocurre automáticamente** en tiempo de ejecución.
- **Funciona automáticamente** y **sin intervención del usuario**.

### 🔑 Cómo Funciona el Cifrado en AES-256-CBC
1. **El token está cifrado en AES-256-CBC** con:
   - **Un IV (Vector de Inicialización) aleatorio**.
   - **La contraseña proporcionada en Base64**, extendida a 32 bytes con SHA-256.
2. **El token cifrado y el IV están almacenados en Base64**:
   - **No se pueden descifrar sin la contraseña correcta**.
   - **Incluso con acceso al código, el token permanece seguro**.
3. **El descifrado ocurre automáticamente** al ejecutar el proyecto:
   - **No se necesita configuración manual**.
   - **El usuario no necesita tocar nada**.

### 🔒 Seguridad y Privacidad
- **El token de solo lectura solo tiene permisos de lectura**:
  - No puede modificar ni eliminar nada en el repositorio.
  - No puede acceder a otros repositorios.
- **La contraseña está en Base64**, no en texto plano.
- **Totalmente transparente y seguro**.

### ⚙️ Ejecución Automática
- Para actualizar los prompts automáticamente, simplemente ejecuta:
  ```sh
  python scripts/update_prompts.py
  ```
- **No se necesita configuración manual**.
- **Funciona automáticamente** y **sin intervención**.

### ❗️ Notas Importantes
- **No necesitas modificar el código ni las configuraciones**.
- **Todo está preconfigurado y listo para usar**.
- **El token está completamente protegido en AES-256-CBC**.


## 📁 Estructura y Organización según RAGArch

El proyecto **Medical-RAGArch-System** cumple con la estructura y nomenclatura estándar de RAGArch:

```
Medical-RAGArch-System/
│   app.py                  # Aplicación principal (FastAPI)
│   requirements.txt        # Dependencias del proyecto
│   README.md                # Documentación del proyecto
│
├── api/
│   └── main.py              # Router de la API principal
│
├── modules/
│   └── ocr_aes256_jwt_module.py  # OCR con múltiples lenguajes y AES-256-CBC
│
├── scripts/
│   └── update_prompts.py    # Actualización automática de prompts
│
├── config/                  # Configuraciones generales
│
├── tests/                   # Pruebas unitarias
│
└── docs/                    # Documentación adicional
```

### ✅ Cumple con los Estándares de RAGArch
- **Snake_case** en módulos y scripts.
- **Convención de `test_`** para archivos en `tests/`.
- **Organización modular y clara** para facilitar mantenimiento y escalabilidad.

---

## 🔍 OCR con Múltiples Lenguajes y Detección Automática

### ✅ Idiomas Soportados
- **Español (`spa`)**
- **Inglés (`eng`)**
- **Francés (`fra`)**
- **Alemán (`deu`)**
- **Italiano (`ita`)**
- **Portugués (`por`)**
- **Catalán (`cat`)**
- **Euskera (`eus`)**
- **Gallego (`glg`)

### 🔑 Características Principales
- **Detección automática de idioma** entre los soportados.
- **Permite combinación de idiomas** (`lang='eng+spa+cat+eus+glg'`).
- **Si no se detecta automáticamente**, usa `eng` como idioma predeterminado.

### ⚙️ Cómo Usar el OCR
- **OCR desde archivo de imagen**:
    ```python
    from modules.ocr_aes256_jwt_module import ocr_image
    text = ocr_image('ruta/a/la/imagen.png')
    print(text)
    ```
- **OCR desde imagen en Base64**:
    ```python
    from modules.ocr_aes256_jwt_module import ocr_base64
    text = ocr_base64('cadena_base64')
    print(text)
    ```

---

## 🚀 Ejecución de la API

### ✅ Iniciar el Servidor con Uvicorn
```sh
uvicorn app:app --reload
```

### ✅ Endpoints Disponibles
- **`GET /`** - Verifica el estado general del sistema.
- **`GET /status`** - Verifica el estado de la API.

### 🌐 Acceder a la API en el Navegador
- **Estado general**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Estado de la API**: [http://127.0.0.1:8000/status](http://127.0.0.1:8000/status)

## 🚀 Integración con FastAPI y AWS Lambda

### ✅ Integración Completa con FastAPI
- **`app.py` está configurado con FastAPI**:
  - **Define la aplicación principal en FastAPI**.
  - **Incluye el router de la API principal (`api/main.py`)**.
  - **Incluye ruta raíz (`"/"`)** para verificar el estado del sistema.
- **Incluye el router de `api/main.py`**:
  - **Permite la funcionalidad completa de la API**.
  - **Incluye rutas adicionales definidas en `api/main.py`**.

### ✅ Despliegue en AWS Lambda con Mangum
- **`Mangum` está integrado** para permitir que FastAPI funcione en AWS Lambda.
- **Configurado para funcionar automáticamente en Lambda**:
  - **Incluye `handler = Mangum(app)`**.
  - **No necesita configuración manual** ni variables de entorno.

### 🌐 Ejecución en Local con Uvicorn
Para probar en local antes de desplegar en AWS Lambda:
```sh
uvicorn app:app --reload
```

### 🌐 Despliegue en AWS Lambda
1. **Crear un archivo ZIP para Lambda**:
    ```sh
    zip -r function.zip .
    ```
2. **Subir el archivo ZIP a AWS Lambda**:
    - Crear una función en AWS Lambda.
    - Seleccionar **"Runtime"** como **Python 3.x**.
    - Configurar el **Handler** como:
      ```plaintext
      app.handler
      ```
3. **Configurar AWS API Gateway**:
    - Crear una API REST en API Gateway.
    - Integrar con la función Lambda.
    - Implementar la API.

### ✅ Endpoints Disponibles
- **`GET /`** - Verifica el estado general del sistema.
- **`GET /status`** - Verifica el estado de la API.

### 🌐 Acceder a la API en AWS
- **Estado general**: `https://<API_ID>.execute-api.<REGION>.amazonaws.com/`
- **Estado de la API**: `https://<API_ID>.execute-api.<REGION>.amazonaws.com/status`

### ❗️ Notas Importantes
- **No necesitas modificar el código ni las configuraciones**.
- **Todo está preconfigurado y listo para desplegar en AWS Lambda**.
- **Funciona automáticamente** y **sin intervención**.

## 🔒 Seguridad Avanzada y Funcionalidades Mejoradas

### ✅ Cifrado AES-256 con Fernet
- **Cifra y almacena datos médicos** en AES-256.
- **Clave de cifrado almacenada en `security/secret.key`**.
- **Si no existe, genera una clave automáticamente**.
- **Totalmente seguro y transparente**.

### ✅ JWT para Autenticación y Autorización
- **Genera tokens JWT** con expiración.
- **Verifica JWT en cada solicitud**.
- **Endpoint `/token/`** para generar **JWT**.
- **Protege datos médicos sensibles** y **controla el acceso a la API**.

### ✅ Cacheo con Redis Cloud Essentials
- **Mejora el rendimiento** con **cacheo avanzado**.
- **Endpoint `/cached-query/{query_key}`** para **consultas cacheadas**.
- **Utiliza `redis_cloud.get_cached_data(query_key)`**.
- **Optimiza el tiempo de respuesta de la API**.

### ✅ Manejo de Logs Avanzado
- **Configura niveles de log y formato de mensajes**.
- **Logs detallados de almacenamiento y recuperación de datos**.
- **Monitoriza la seguridad y el rendimiento** de la API.

### 🔥 Endpoints Adicionales y Funcionalidad
- **`/token/`** - Genera tokens JWT para autenticación.
- **`/store/`** - Almacena datos cifrados en AES-256.
- **`/retrieve/`** - Recupera datos cifrados en AES-256.
- **`/cached-query/{query_key}`** - Consultas cacheadas en Redis Cloud Essentials.

---

## 🚀 Despliegue en AWS Lambda

### ✅ Integración con AWS Lambda
- **`Mangum` está integrado** para permitir que FastAPI funcione en AWS Lambda.
- **Configurado para funcionar automáticamente en Lambda**:
  - **Incluye `handler = Mangum(app)`**.
  - **No necesita configuración manual** ni variables de entorno.

### 🌐 Ejecución en Local con Uvicorn
Para probar en local antes de desplegar en AWS Lambda:
```sh
uvicorn app:app --reload
```

### 🌐 Despliegue en AWS Lambda
1. **Crear un archivo ZIP para Lambda**:
    ```sh
    zip -r function.zip .
    ```
2. **Subir el archivo ZIP a AWS Lambda**:
    - Crear una función en AWS Lambda.
    - Seleccionar **"Runtime"** como **Python 3.x**.
    - Configurar el **Handler** como:
      ```plaintext
      app.handler
      ```
3. **Configurar AWS API Gateway**:
    - Crear una API REST en API Gateway.
    - Integrar con la función Lambda.
    - Implementar la API.

### ✅ Endpoints Disponibles
- **`GET /`** - Verifica el estado general del sistema.
- **`GET /status`** - Verifica el estado de la API.
- **`POST /token/`** - Genera tokens JWT para autenticación.
- **`POST /store/`** - Almacena datos cifrados en AES-256.
- **`GET /retrieve/`** - Recupera datos cifrados en AES-256.
- **`GET /cached-query/{query_key}`** - Consultas cacheadas en Redis Cloud Essentials.

### 🌐 Acceder a la API en AWS
- **Estado general**: `https://<API_ID>.execute-api.<REGION>.amazonaws.com/`
- **Estado de la API**: `https://<API_ID>.execute-api.<REGION>.amazonaws.com/status`

### ❗️ Notas Importantes
- **No necesitas modificar el código ni las configuraciones**.
- **Todo está preconfigurado y listo para desplegar en AWS Lambda**.
- **Funciona automáticamente** y **sin intervención**.

## 📁 Configuración Mejorada y Funcionalidades Avanzadas

### ✅ `interactions_db.json`
- **Interacciones más completas y detalladas**:
  - **Incluye interacciones críticas** entre medicamentos y suplementos.
  - **Riesgos de deficiencias** (ej. Metformina y Vitamina B12).
  - **Recomendaciones clínicas detalladas**:
    - **"Evitar combinación o monitorizar INR"** en interacciones críticas.
    - **"Monitorizar niveles de B12 anualmente"** para deficiencias potenciales.
  - **Óptimo para análisis clínicos y recomendaciones personalizadas**.

### ✅ `report_templates.yaml`
- **Plantillas de informes más flexibles y personalizables**:
  - **Formatos disponibles**: **PDF, Excel, Markdown**.
  - **Secciones adicionales**:
    - **Resumen Ejecutivo**.
    - **Análisis Comparativo**.
    - **Recomendaciones Personalizadas**.
  - **Optimizado para generar informes médicos** altamente personalizados.

### ✅ `sources_config.yaml`
- **Jerarquización avanzada de fuentes**:
  - **Fuentes adicionales** para análisis de suplementos y farmacología:
    - **Natural Medicines Database**, **Cochrane Library**.
    - **Guías específicas para suplementos** (ODS, NCCIH).
  - **Jerarquización detallada**:
    - **Prioriza fuentes basadas en evidencia clínica**.
    - **Define reglas claras de uso** según la consulta.
  - **Óptimo para análisis de suplementos y decisiones clínicas**.

### ✅ `supplement_validation.yaml`
- **Validación específica y avanzada de suplementos**:
  - **Incluye validaciones avanzadas**:
    - **Interacciones con medicamentos**.
    - **Contraindicaciones clínicas**.
    - **Dosis seguras y fuentes confiables**.
  - **Optimizado para pacientes polimedicados**.
  - **Ideal para análisis de suplementos** en contexto clínico.

### 🔥 Funcionalidades Completamente Integradas
- **Todo está completamente integrado en el flujo de trabajo**.
- **No requiere intervención del usuario**.
- **Funciona automáticamente y sin errores**.
- **Totalmente transparente y seguro**.

### 🌐 Ejecución en Local y Despliegue en AWS Lambda
- **Todo el sistema funciona automáticamente** tanto en local como en AWS Lambda.
- **No se necesita configuración adicional**.


## Configuración de Variables de Entorno con `.env`
Se ha incluido soporte para configuración de variables de entorno mediante `.env`. 
Esto permite personalizar la configuración sin modificar el código.

### Ejemplos de Configuración en `.env`
```
SECRET_KEY=tu_clave_secreta_personalizada
JWT_SECRET_KEY=otra_clave_secreta
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=tu_password_redis
FERNET_KEY=clave_cifrado_fernet
```

### Uso de `.env.example`
- Se incluye un archivo `.env.example` con ejemplos prácticos.
- Para empezar, copia `.env.example` a `.env` y personaliza las variables según tu entorno.
- **No subas `.env` a GitHub**. Está listado en `.gitignore` para proteger datos sensibles.


## 🔧 Configuraciones Recientes y Mejoras

### 1. 📡 Despliegue de FastAPI en Lambda con API Gateway Seguro
- **FastAPI ahora es accesible públicamente en AWS Lambda** usando:
  - **API Gateway con HTTPS** (TLS 1.2 o superior) para garantizar la seguridad de las conexiones.
  - **CORS configurado** para permitir consultas desde ChatGPT u otros clientes HTTP.
  - **Modo Proxy** en API Gateway para enrutar todas las solicitudes HTTP a FastAPI.
- **Acceso seguro y flexible** compatible con ChatGPT y otras aplicaciones.

### 2. 🗂️ Almacenamiento de Documentos Médicos en DynamoDB
- **DynamoDB ahora crea automáticamente las tablas necesarias**:
  - `MedicalRecords`: Para almacenar documentos médicos y analíticas en formato JSON.
    - **Clave primaria:** `RecordID` (Tipo: String)
    - **Índice secundario:** `Date` (Tipo: String) para ordenar cronológicamente.
  - `UserQueries`: Para almacenar consultas realizadas (por ejemplo, a ChatGPT).
    - **Clave primaria:** `QueryID` (Tipo: String)
    - **Índice secundario:** `Timestamp` (Tipo: String) para orden cronológico.

### 3. 📥 Carga Automática de Documentos JSON
- **Se pueden cargar documentos JSON directamente** en la tabla `MedicalRecords`.
- **No es necesario crear tablas para cada biomarcador**. La estructura JSON es flexible y dinámica.

### 4. 🚀 Despliegue Automático
- **Despliegue automatizado con GitHub Actions**:
  - `deploy_to_lambda.yml`: Despliega FastAPI en Lambda y configura API Gateway.
  - `deploy_to_dynamodb.yml`: Crea tablas en DynamoDB y carga documentos JSON.

### 5. 🔐 Seguridad Mejorada
- **Cifrado HTTPS** y **CORS configurado** para seguridad en API Gateway.
- **TLS 1.2 o superior** para proteger los datos en tránsito.

### ℹ️ Notas Importantes
- **`deploy_dynamodb.yml` ha sido eliminado** para limpiar el proyecto.
- **No es necesario configurar tablas manualmente**. Se crean automáticamente al desplegar.
- **La estructura JSON permite flexibilidad total** para documentos médicos y analíticas.


## 🚀 Nuevas Funcionalidades Implementadas

### 1. 📊 Predicciones de Series Temporales
- **Ubicación:** `modules/analytics/time_series_predictor.py`
- **Dependencias utilizadas:** `prophet`, `pmdarima`, `matplotlib`, `plotly`
- **Descripción:**
  - Permite realizar **predicciones de tendencias en biomarcadores** (como glucosa, colesterol, presión arterial).
  - Utiliza **Prophet** y **pmdarima** para predicciones a corto y largo plazo.
  - Incluye **visualizaciones interactivas** con **plotly**.
- **Funciones implementadas:**
  - `prophet_prediction(periods=30)`: Realiza predicciones con Prophet para los próximos 30 días (o el periodo especificado).
  - `plot_prophet(df, forecast)`: Genera gráficos interactivos con `plotly` para visualizar las tendencias.

### 2. 🧠 Inteligencia Contextual
- **Ubicación:** `modules/nlp/intelligent_context.py`
- **Dependencias utilizadas:** `langdetect`, `transformers`, `nltk`
- **Descripción:**
  - **Detecta el idioma** de un texto automáticamente.
  - **Resume documentos médicos** utilizando modelos avanzados de lenguaje con `transformers`.
  - **Extrae palabras clave** relevantes de un documento.
- **Funciones implementadas:**
  - `detect_language()`: Detecta el idioma del texto proporcionado.
  - `summarize_text()`: Genera un **resumen automático** utilizando `transformers`.
  - `extract_keywords()`: Extrae **palabras clave** utilizando `nltk`.

### 3. 🌐 WebSockets Mejorada
- **Ubicación:** `modules/websockets/websockets_chat.py`
- **Dependencias utilizadas:** `websockets`, `fastapi-websockets`, `asyncio`
- **Descripción:**
  - **Comunicación en tiempo real** con WebSockets utilizando FastAPI.
  - Incluye un **chat bidireccional** con una interfaz en HTML para demostrar la funcionalidad.
- **Funciones implementadas:**
  - `websocket_endpoint(websocket: WebSocket)`: Maneja la **comunicación bidireccional** con el cliente.
  - **Interacción en tiempo real** con mensajes que se actualizan instantáneamente en la interfaz de usuario.

### 📘 Instrucciones de Uso
1. **Instalar dependencias** si aún no están instaladas:
    ```bash
    pip install prophet pmdarima matplotlib plotly langdetect transformers nltk websockets fastapi-websockets asyncio
    ```
2. **Ejemplos de uso:**
    - Para **predicciones de series temporales**:
      ```python
      from modules.analytics.time_series_predictor import TimeSeriesPredictor
      predictor = TimeSeriesPredictor(data, 'date', 'value')
      forecast = predictor.prophet_prediction(periods=30)
      ```
    - Para **inteligencia contextual**:
      ```python
      from modules.nlp.intelligent_context import IntelligentContext
      context = IntelligentContext("Texto de ejemplo en varios idiomas...")
      print(context.detect_language())
      print(context.summarize_text())
      print(context.extract_keywords())
      ```
    - Para **WebSockets Mejorada**:
      - Ejecutar el servidor con:
        ```bash
        uvicorn modules.websockets.websockets_chat:app --reload
        ```
      - Acceder a `http://localhost:8000` en el navegador para probar el **chat en tiempo real**.

### 🔧 Notas Técnicas y Recomendaciones
- **Prophet** requiere `pystan` como dependencia adicional para predicciones de series temporales.
- **Transformers** puede requerir modelos pre-entrenados; asegúrate de tener **conexión a internet** para descargarlos.
- **WebSockets Mejorada** está configurada para **interacción en tiempo real**, ideal para **consultas a IA** o **actualizaciones dinámicas**.


## 🚀 Nuevas Funcionalidades Implementadas para Aprovechar Dependencias

### 1. 📊 Dashboards Interactivos con Dash
- **Ubicación:** `modules/dashboards/interactive_dashboard.py`
- **Dependencias utilizadas:** `dash`, `plotly`, `pandas`
- **Descripción:**
  - Permite crear **dashboards interactivos** para visualizar **tendencias en biomarcadores**.
  - Incluye **gráficos interactivos** de series temporales con `plotly`.
- **Funciones implementadas:**
  - `app.layout`: Configura el **layout del dashboard** en Dash.
  - `app.run_server(debug=True)`: Inicia el **servidor local de Dash**.

### 2. 🚀 ML Optimization con scikit-learn-intelex
- **Ubicación:** `modules/ml_optimization/ml_optimization.py`
- **Dependencias utilizadas:** `scikit-learn-intelex`, `numpy`
- **Descripción:**
  - **Acelera modelos de Machine Learning** utilizando **optimizaciones de Intel**.
  - Mejora el **rendimiento en predicciones** de series temporales.
- **Funciones implementadas:**
  - `patch_sklearn()`: Aplica **optimizaciones de Intel** a scikit-learn.
  - `model.predict()`: Realiza **predicciones optimizadas** con scikit-learn.

### 3. 🌐 Análisis de Redes con NetworkX
- **Ubicación:** `modules/network_analysis/network_analysis.py`
- **Dependencias utilizadas:** `networkx`, `matplotlib`
- **Descripción:**
  - Analiza **relaciones complejas entre biomarcadores**.
  - Visualiza **redes de interacciones** entre medicamentos o biomarcadores.
- **Funciones implementadas:**
  - `nx.community.label_propagation_communities(G)`: Detecta **comunidades** en la red.
  - `nx.draw_networkx()`: Visualiza **grafos de relaciones**.

### 4. 🖼️ OCR Avanzado con Tesseract y Pillow
- **Ubicación:** `modules/ocr/ocr_advanced.py`
- **Dependencias utilizadas:** `pytesseract`, `Pillow`
- **Descripción:**
  - Realiza **OCR avanzado** en documentos médicos.
  - Extrae **texto de imágenes o PDFs** en múltiples idiomas.
- **Funciones implementadas:**
  - `pytesseract.image_to_string(img, lang='spa')`: Extrae texto en **español** desde imágenes.
  - `Image.open(image_path)`: Carga imágenes utilizando `Pillow`.

### 5. 🚀 Cache Optimizada con Redis
- **Ubicación:** `modules/cache/cache_redis.py`
- **Dependencias utilizadas:** `redis`
- **Descripción:**
  - Implementa **cache optimizada** para **acelerar consultas a IA médica**.
  - Cachea **resultados de predicciones** para respuestas más rápidas.
- **Funciones implementadas:**
  - `cache.set('clave', 'valor cacheado')`: Almacena **datos en cache**.
  - `cache.get('clave')`: Recupera **datos cacheados** de Redis.

### 📘 Instrucciones de Uso
1. **Instalar dependencias** si aún no están instaladas:
    ```bash
    pip install dash plotly pandas scikit-learn-intelex numpy networkx matplotlib pytesseract Pillow redis
    ```
2. **Ejemplos de uso:**
    - Para **Dashboards Interactivos**:
      ```bash
      python modules/dashboards/interactive_dashboard.py
      ```
    - Para **ML Optimization**:
      ```bash
      python modules/ml_optimization/ml_optimization.py
      ```
    - Para **Análisis de Redes**:
      ```bash
      python modules/network_analysis/network_analysis.py
      ```
    - Para **OCR Avanzado**:
      ```bash
      python modules/ocr/ocr_advanced.py
      ```
    - Para **Cache Optimizada**:
      ```bash
      python modules/cache/cache_redis.py
      ```

### 🔧 Notas Técnicas y Recomendaciones
- **Dashboards Interactivos** requieren tener **Dash y Plotly** correctamente instalados.
- **ML Optimization** aprovecha **procesadores Intel** para acelerar el rendimiento.
- **Análisis de Redes** permite **visualizar relaciones complejas** y detectar comunidades.
- **OCR Avanzado** soporta **múltiples idiomas** si se instalan paquetes de idiomas de Tesseract.
- **Cache Optimizada** requiere tener **Redis en ejecución** localmente o en la nube.



## 🚀 Nuevas Funcionalidades Implementadas: Autenticación y WebSockets en Tiempo Real

### 1. 🔐 Autenticación con FastAPI OAuth2PasswordBearer
- **Ubicación:** `modules/auth/auth.py`
- **Dependencias utilizadas:** `FastAPI`, `OAuth2PasswordBearer`
- **Descripción:**
  - Proporciona **autenticación segura** para **proteger rutas sensibles**.
  - Utiliza **OAuth2 con Bearer Token** para una **autenticación sencilla y segura**.
  - **No requiere gestión de claves** ni configuración manual de tokens.
  - **Almacenamiento en memoria** para simplificar el manejo de usuarios.
- **Funciones implementadas:**
  - `get_current_user(token: str)`: Verifica el **token de usuario** y autentica el acceso.

### 2. 🌐 WebSockets en Tiempo Real
- **Ubicación:** `modules/websockets_real_time/websockets_real_time.py`
- **Dependencias utilizadas:** `FastAPI`, `WebSocket`, `HTMLResponse`
- **Descripción:**
  - Proporciona **interacción en tiempo real** con **IA médica** y **predicciones de series temporales**.
  - Incluye **alertas inmediatas** basadas en resultados críticos.
  - **HTML separado** en `templates/index.html` para **evitar problemas de indentación**.
- **Funciones implementadas:**
  - `websocket_endpoint(websocket: WebSocket)`: Gestiona **comunicación en tiempo real** con el cliente.
  - **Alertas inmediatas** y **mensajería bidireccional**.

### 📘 Instrucciones de Uso
1. **Instalar dependencias** si aún no están instaladas:
    ```bash
    pip install fastapi uvicorn
    ```
2. **Ejemplos de uso:**
    - Para **Autenticación OAuth2**:
      ```python
      from modules.auth.auth import get_current_user
      # Utilizar en rutas protegidas
      @app.get("/perfil/")
      async def perfil(current_user: User = Depends(get_current_user)):
          return {"usuario": current_user.username}
      ```
    - Para **WebSockets en Tiempo Real**:
      ```bash
      uvicorn modules.websockets_real_time.websockets_real_time:app --reload
      ```
      - Acceder a `http://localhost:8000` en el navegador para probar la **interacción en tiempo real**.

### 🔧 Notas Técnicas y Recomendaciones
- **OAuth2PasswordBearer** utiliza **Bearer Tokens** almacenados en memoria.
- **WebSockets en Tiempo Real** requiere acceso a `ws://localhost:8000/ws`.
- **HTML separado en `templates/index.html`** para facilitar la edición del frontend.



## 🔒 Actualizaciones de Cifrado para Mejor Seguridad y Rendimiento

### 1. 🚀 AES-256-GCM
- **Ubicación:** `modules/encryption/aes_gcm.py`
- **Descripción:**
  - Se actualizó de **AES-256-CBC** a **AES-256-GCM** para:
    - Mejorar el **rendimiento en hardware moderno**.
    - Añadir **autenticación integrada** con **Tag GCM**.
    - Garantizar **confidencialidad** e **integridad** de los datos.
- **Usos en el Proyecto:**
  - **Cifrado de datos locales** (documentos médicos, tokens).
  - **Cifrado en tránsito** en WebSockets y OAuth2.

### 2. 🔐 ES256 (ECDSA) en OAuth2
- **Ubicación:** `modules/auth/auth_es256.py`
- **Descripción:**
  - Se actualizó de **HS256 (HMAC-SHA256)** a **ES256 (ECDSA)** para:
    - **Firmas asimétricas** (clave privada para firmar, clave pública para verificar).
    - Mejorar **seguridad en entornos distribuidos**.
    - Eliminar la necesidad de **compartir una clave secreta**.
    - **Firmas más rápidas** con **claves más cortas**.
- **Usos en el Proyecto:**
  - **Tokens de autenticación** en OAuth2.

### 3. 🌐 TLS 1.3 en WebSockets y API Gateway
- **Ubicación:** `modules/websockets_real_time/websockets_real_time_tls13.py`
- **Descripción:**
  - Se actualizó de **TLS 1.2** a **TLS 1.3** para:
    - **Menos latencia** con **menos intercambios de claves**.
    - **Cifrado más robusto** con **algoritmos mejorados**.
    - **Compatibilidad con navegadores modernos**.
- **Usos en el Proyecto:**
  - **WebSockets**.
  - **API Gateway**.

### 🔧 Notas Técnicas y Recomendaciones
- **AES-GCM** proporciona **confidencialidad** e **integridad** en un solo paso.
- **ES256 (ECDSA)** utiliza **firmas asimétricas** para **mejor seguridad y rendimiento**.
- **TLS 1.3** ofrece **mayor seguridad y rendimiento** en **conexiones en tránsito**.



### Autenticación con JWT
Este proyecto utiliza **ES256 (Elliptic Curve)** para firmar y verificar Tokens JWT, garantizando 
un **alto nivel de seguridad y rendimiento**.

En la versión refactorizada, **`auth_es256.py` maneja toda la lógica de autenticación**, 
mientras que `auth.py` ha sido eliminado para **evitar conflictos en la verificación de Tokens**.

Si ves referencias a `auth.py` en versiones anteriores, **puedes ignorarlas**, ya que toda la 
funcionalidad está cubierta en `auth_es256.py`.

## 🔐 Cifrado de GitHub Token con AES-256-GCM

Este proyecto utiliza **AES-256-GCM** para cifrar el GitHub Token, garantizando máxima seguridad mediante:
- **Integridad y Autenticidad**: Utilizando `TAG` para validar que el token no ha sido manipulado.
- **Confidencialidad**: Utilizando `NONCE` para garantizar la unicidad del cifrado.

### 🛠️ Configuración de `.env`
Para habilitar el descifrado automático, añade las siguientes variables en `.env`:

```env
# GitHub Token Cifrado con AES-256-GCM
GITHUB_TOKEN_CIFRADO=<TOKEN_CIFRADO>
NONCE=<NONCE>
TAG=<TAG>

# Contraseña del ZIP en Base64 (preconfigurada)
ZIP_PASSWORD_BASE64=dzFmMXNsNHhyYWdhcmNo
```

- **`GITHUB_TOKEN_CIFRADO`**: Token cifrado con AES-256-GCM.
- **`NONCE`**: Valor único utilizado para el cifrado GCM.
- **`TAG`**: Tag de autenticación para validar integridad.

### 🔒 Seguridad Adicional
- El token nunca se almacena en texto plano.
- El descifrado se realiza **solo en tiempo de ejecución**, garantizando máxima seguridad.

### ✅ Flujo de Descifrado
1. **El script `update_prompts.py` carga las variables desde `.env`.**
2. **Descifra el token utilizando AES-256-GCM con `NONCE` y `TAG`.**
3. **Verifica la integridad del token utilizando el `TAG`.**
4. **Utiliza el token descifrado para acceder automáticamente al repositorio de GitHub.**

Este método garantiza la seguridad e integridad del token, cumpliendo con **GDPR** y **mejores prácticas de seguridad**.

---

## 🔐 Cifrado de GitHub Token con AES-256-GCM y PBKDF2

Este proyecto utiliza **AES-256-GCM con PBKDF2 y SHA-256** para cifrar el GitHub Token, garantizando máxima seguridad mediante:
- **Integridad y Autenticidad**: Utilizando `TAG` para validar que el token no ha sido manipulado.
- **Confidencialidad**: Utilizando `NONCE` para garantizar la unicidad del cifrado.
- **Derivación de Claves Segura**: Utilizando **PBKDF2 con SHA-256** y un `Salt` fijo para generar la clave AES de 256 bits.

### 🛠️ Configuración de `.env`
Para habilitar el descifrado automático, añade las siguientes variables en `.env`:

```env
# GitHub Token Cifrado con AES-256-GCM
GITHUB_TOKEN_CIFRADO=<TOKEN_CIFRADO>
NONCE=<NONCE>
TAG=<TAG>

# Contraseña del ZIP en Base64 (preconfigurada)
ZIP_PASSWORD_BASE64=dzFmMXNsNHhyYWdhcmNo
```

- **`GITHUB_TOKEN_CIFRADO`**: Token cifrado con AES-256-GCM.
- **`NONCE`**: Valor único utilizado para el cifrado GCM.
- **`TAG`**: Tag de autenticación para validar integridad.

### 🔒 Seguridad Adicional
- Utiliza **PBKDF2 con SHA-256** para derivación de claves.
- Incluye un `Salt` fijo para fortalecer la seguridad.
- El token nunca se almacena en texto plano.
- El descifrado se realiza **solo en tiempo de ejecución**, garantizando máxima seguridad.

### ✅ Flujo de Descifrado
1. **El script `update_prompts.py` carga las variables desde `.env`.**
2. **Deriva la clave utilizando PBKDF2 con SHA-256 y un `Salt` fijo.**
3. **Descifra el token utilizando AES-256-GCM con `NONCE` y `TAG`.**
4. **Verifica la integridad del token utilizando el `TAG`.**
5. **Utiliza el token descifrado para acceder automáticamente al repositorio de GitHub.**

Este método garantiza la seguridad e integridad del token, cumpliendo con **GDPR** y **mejores prácticas de seguridad**.

---
