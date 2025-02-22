
# 🚀 Guía Rápida de Despliegue para Medical-RAGArch-System

Esta guía te ayudará a **desplegar este proyecto de manera rápida y sencilla**.  
¡No necesitas conocimientos técnicos avanzados! 🎉

---

## 📌 Requisitos Previos

1. **Cuenta de AWS** (gratuita).  
   - Puedes crearla aquí: [https://aws.amazon.com/free](https://aws.amazon.com/free)  
   - **No necesitas ingresar método de pago** si solo usas el límite gratuito.

2. **Instala AWS CLI en tu computadora:**  
   - Instrucciones aquí: [https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

3. **Instala AWS SAM CLI:**  
   - Instrucciones aquí: [https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)

4. **Instala Python 3.9** y **PIP** (el gestor de paquetes de Python).

---

## 🚀 Despliegue Automático en AWS Lambda

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/TU_USUARIO/TU_FORK.git
cd TU_FORK
```

### Paso 2: Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Paso 3: Configurar Credenciales de AWS

```bash
aws configure
```

- **AWS Access Key:** La recibirás al crear tu cuenta de AWS.  
- **AWS Secret Access Key:** La recibirás junto con la Access Key.  
- **Region:** Usa `us-east-1` para evitar problemas de compatibilidad.  
- **Output Format:** Deja vacío o usa `json`.  

### Paso 4: Desplegar Automáticamente

```bash
sam build
sam deploy --guided
```

- El comando **sam deploy --guided** te pedirá que ingreses algunos datos:  
  - **Stack Name:** Ponle un nombre a tu despliegue, por ejemplo, `Medical-RAGArch-System`.  
  - **AWS Region:** Usa `us-east-1` para evitar problemas de compatibilidad.  
  - **Confirm Changes Before Deploy:** `N` (No necesitas confirmar cada cambio).  
  - **Allow SAM CLI IAM Role Creation:** `Y` (Sí, permite que cree roles en IAM).  

---

## 💡 ¿Cómo funciona el coste en AWS?

- **Si no se usa, el coste es 0.**  
- Incluye el **Nivel Gratuito de AWS Lambda**, que ofrece:  
  - **1 millón de solicitudes al mes gratis.**  
  - **400,000 GB-segundos de tiempo de ejecución gratis.**  
- Ejemplos de costes si se sobrepasa el límite gratuito:  
  - 1 millón de solicitudes adicionales: **0.20 USD**  
  - 1 GB-segundo adicional: **0.00001667 USD**  

**No se te cobrará nada** si no añades un método de pago o si te mantienes en el límite gratuito.  

---

## 🎉 ¡Listo!

Si seguiste todos los pasos, tu proyecto **ya debería estar desplegado en AWS Lambda.**  
Puedes acceder a tu **API usando la URL** que aparecerá al finalizar el despliegue.  

¡Ahora puedes comenzar a utilizar Medical-RAGArch-System sin complicaciones! 🚀

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

