
# Medical-RAGArch-System

## Descripción
Medical-RAGArch-System es un sistema avanzado para el despliegue automático de FastAPI en AWS Lambda, con integración segura utilizando GitHub Actions y OpenID Connect (OIDC). Se conecta automáticamente a DynamoDB con cifrado AES-256 y KMS.

---

## Características Clave
- **GitHub Actions con OIDC** para autenticación segura sin manejo de claves.
- **Despliegue automático en AWS Lambda** utilizando CloudFormation y SAM CLI.
- **Conexión segura a DynamoDB** con cifrado AES-256 y almacenamiento de claves en AWS KMS.
- **Permisos mínimos en IAM Roles** aplicando el principio de privilegios mínimos.
- **Rotación automática de tokens** en `update_prompts.py` para mayor seguridad.

---

## Configuración de OIDC en GitHub Actions
1. **Crear un Role en AWS para OIDC:**
   - Acceder a AWS IAM y crear un Role con `Web Identity`.
   - Establecer el `Provider` como `https://token.actions.githubusercontent.com`.
   - Configurar el `Audience` como `sts.amazonaws.com`.
   - Añadir la siguiente `Trust Policy`:
     ```json
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Principal": {
             "Federated": "arn:aws:iam::<AWS_ACCOUNT_ID>:oidc-provider/token.actions.githubusercontent.com"
           },
           "Action": "sts:AssumeRoleWithWebIdentity",
           "Condition": {
             "StringEquals": {
               "token.actions.githubusercontent.com:aud": "sts.amazonaws.com",
               "token.actions.githubusercontent.com:sub": "repo:Melkoroth/Medical-RAGArch-System:*"
             }
           }
         }
       ]
     }
     ```
2. **Configurar GitHub Secrets:**
   - Añadir `AWS_ACCOUNT_ID` como secreto en el repositorio.

---

## Despliegue Automático en AWS Lambda
1. **Requisitos previos:**
   - Instalar **AWS CLI** y **SAM CLI**.
   - Configurar credenciales de AWS con:
     ```bash
     aws configure
     ```

2. **Despliegue con GitHub Actions:**
   - Se utilizan los workflows:
     - `.github/workflows/deploy_to_dynamodb.yml`
     - `.github/workflows/deploy_to_lambda.yml`

3. **Pasos de Despliegue:**
   - Al hacer `push` en la rama `main`, el workflow se ejecuta automáticamente:
     - Compila el proyecto y genera un paquete de despliegue.
     - Despliega en AWS Lambda usando `zip` y `aws lambda update-function-code`.
     - Actualiza configuración de Lambda con Auto Scaling (`memory-size` y `timeout`).

4. **Verificación del Despliegue:**
   - Navegar a **AWS Lambda Console** y verificar la función `MyRAGArchLambda`.
   - Probar la API utilizando **API Gateway** configurado en `template.yaml`.

---

## Conexión Segura a DynamoDB
1. **Cifrado AES-256 y KMS:**
   - Se utiliza `dynamodb_optimization.py` con **AWS KMS** para cifrar y descifrar datos.
   - **Verificación de Integridad** con SHA-256 al almacenar y recuperar datos.

2. **Permisos Mínimos en `template.yaml`:**
   - Se utiliza la política `DynamoDBLeastPrivilegePolicy` para limitar permisos a:
     - `dynamodb:GetItem`
     - `dynamodb:Query`
     - `dynamodb:PutItem`
     - `dynamodb:UpdateItem`
     - `dynamodb:DeleteItem`

3. **Prueba de Conexión:**
   - Verificar conexión ejecutando:
     ```bash
     aws dynamodb scan --table-name MyRAGArchTable
     ```

---

## Rotación Automática de Tokens en `update_prompts.py`
- La rotación automática de tokens se implementa para mayor seguridad.
- **`password_text`** se obtiene ahora de una variable de entorno (`GITHUB_TOKEN_PASSWORD`).
- Ejemplo de configuración de variable de entorno en GitHub Actions:
  ```yaml
  env:
    GITHUB_TOKEN_PASSWORD: ${{ secrets.GITHUB_TOKEN_PASSWORD }}
  ```

---

## Ejemplos Prácticos
1. **Despliegue de FastAPI en AWS Lambda:**
   ```bash
   sam build
   sam deploy --guided
   ```

2. **Prueba de API en API Gateway:**
   ```bash
   curl -X GET https://<API_ID>.execute-api.us-east-1.amazonaws.com/dev/health
   ```

3. **Rotación de Token en `update_prompts.py`:**
   ```python
   from update_prompts import rotate_github_token
   new_token = rotate_github_token()
   print(f"Nuevo token: {new_token}")
   ```

---

## Seguridad y Mejores Prácticas
- **OIDC** elimina la necesidad de manejar secretos estáticos.
- **AES-256 y KMS** protegen los datos en DynamoDB.
- **SHA-256** asegura la integridad de los datos almacenados.
- **Permisos mínimos en IAM** para reducir la superficie de ataque.

---

## Contribuciones y Desarrollo
1. **Clonar el Repositorio:**
   ```bash
   git clone https://github.com/Melkoroth/Medical-RAGArch-System.git
   ```

2. **Crear una Rama Nueva:**
   ```bash
   git checkout -b nueva-funcionalidad
   ```

3. **Hacer Push y Crear Pull Request:**
   ```bash
   git push origin nueva-funcionalidad
   ```

---

## Preguntas Frecuentes (FAQ)
1. **¿Qué es OIDC?**
   - OpenID Connect (OIDC) es un protocolo de autenticación seguro que permite a GitHub Actions asumir roles en AWS sin necesidad de claves estáticas.

2. **¿Cómo funcionan los tokens en `update_prompts.py`?**
   - Se utiliza AES-256-CBC para cifrar el token, y se rota automáticamente para mayor seguridad.

3. **¿Qué permisos son necesarios en AWS?**
   - Los permisos están restringidos a los mínimos necesarios en `template.yaml` y a través de políticas de IAM.

---

## Contacto
Para más información, contactar a **Melkoroth** en GitHub.

---

## Licencia
Este proyecto se distribuye bajo la licencia MIT.

## 📄 OCR Multilingüe en `ocr_aes256_jwt.py`

El módulo `ocr_aes256_jwt.py` ahora soporta reconocimiento de texto en **Español**, **Catalán** e **Inglés**.

### 🔍 Funcionalidades:
- **Detección automática de idioma** en imágenes y PDFs.
- **Preprocesamiento avanzado** de imágenes para mejorar la precisión:
  - Conversión a escala de grises.
  - Umbral binario para reducir ruido.

### ⚙️ Requisitos de Tesseract:
Para asegurar el reconocimiento correcto en múltiples idiomas, instala los paquetes de idioma correspondientes:
```bash
sudo apt install tesseract-ocr-spa tesseract-ocr-cat tesseract-ocr-eng
```
Esto habilita el soporte para:
- **Español (`spa`)**
- **Catalán (`cat`)**
- **Inglés (`eng`)**

### 🚀 Uso:
El OCR detecta automáticamente el idioma del documento y extrae el texto utilizando:
```python
pytesseract.image_to_string(preprocessed_image, lang='spa+cat+eng')
```
Si no se detecta un idioma específico, **usa Inglés (`eng`)** como idioma por defecto.

## ⚙️ Configuraciones y Mejoras Recientes

### 1. 📄 OCR Multilingüe con PSM Avanzado
El módulo `ocr_aes256_jwt.py` ahora utiliza **PSM avanzado en Tesseract** para mejorar la precisión en documentos médicos.

- **Idiomas Soportados:** Español (`spa`), Catalán (`cat`) e Inglés (`eng`).
- **PSM Configurable:** Se utiliza `--psm 6` para bloques de texto uniformes. Puede cambiarse a `--psm 4` para columnas desordenadas.
- **Preprocesamiento Avanzado:** Conversión a escala de grises y umbral binario para reducir ruido.

### 2. 🔒 Conexión Segura con Redis Cloud
El módulo `redis_cloud.py` ahora utiliza **SSL/TLS (`rediss://`)** para cifrar datos en tránsito:
- **Encriptación en tránsito:** Configurada con `ssl=True` y `ssl_cert_reqs='required'`.
- **Mayor seguridad en Redis Cloud Essentials.**

### 3. 🌐 Informes Multilingües
El módulo `reporting_generator.py` permite **generar informes clínicos en múltiples idiomas**:
- **Idiomas Soportados:** 
  - Español (`spa`)
  - Catalán (`cat`)
  - Inglés (`eng`)
- **Parámetro de Idioma:** Se añade `lang='eng'` para seleccionar el idioma del informe.

### 4. 🔑 Rotación Automática de Token de GitHub
El módulo `update_prompts.py` ahora utiliza **OIDC en GitHub Actions** para:
- **Obtener un Token temporal** en tiempo de ejecución.
- **Eliminar la necesidad de un Token estático**, mejorando la seguridad.
- **Rotación automática** para evitar expiración o compromiso de tokens.

### 📝 Notas Importantes
- Asegúrate de tener instalados los paquetes de idioma para Tesseract:
```bash
sudo apt install tesseract-ocr-spa tesseract-ocr-cat tesseract-ocr-eng
```
- Redis Cloud Essentials ahora requiere una **conexión segura con SSL/TLS** (`rediss://`).
- Los informes se generan automáticamente en el idioma seleccionado en base al parámetro `lang`.

