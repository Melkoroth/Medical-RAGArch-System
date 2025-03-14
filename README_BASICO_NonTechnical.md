
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

# 🚀 Medical-RAGArch-System - Guía de Despliegue Rápido

Esta guía está diseñada para usuarios **sin conocimientos técnicos** que necesiten desplegar el sistema de forma automática.

---

## 📌 **1️⃣ Requisitos Previos**

✅ **Solo necesitas:**  
✔ Una **cuenta de AWS** (con permisos para Lambda, DynamoDB y API Gateway).  
✔ Un **GitHub** (para ejecutar la automatización).  

---

## 📌 **2️⃣ Despliegue Automático (Método Recomendado)**

1️⃣ **Haz un "Fork" del repositorio en GitHub** (Botón "Fork" en la esquina superior derecha).  
2️⃣ **Ve a "Actions" en tu fork** y activa los workflows si es la primera vez.  
3️⃣ **Edita los "Secrets" en tu repositorio de GitHub**:  
   - Ve a **Settings > Secrets and variables > Actions > New Repository Secret**  
   - Agrega las credenciales de AWS:  
     - `AWS_ACCESS_KEY_ID`  
     - `AWS_SECRET_ACCESS_KEY`  
     - `AWS_REGION`  
4️⃣ **Espera unos minutos mientras el sistema se despliega automáticamente.**  

---

## 📌 **3️⃣ Seguridad Automática con AWS Secrets Manager**

✅ **Este sistema protege automáticamente las claves de cifrado.**  
✅ **No necesitas hacer nada manualmente.**  

📌 **¿Cómo funciona?**  
- Las claves de cifrado **se almacenan automáticamente en AWS Secrets Manager**.  
- Esto se configura en el código de forma transparente para el usuario.  
- La primera vez que el sistema se ejecuta, las claves se crean y se guardan solas.  

📌 **¿Tienes que hacer algo manualmente?**  
**No. Todo ocurre de forma automática.**  

---

## 📌 **4️⃣ Comprobación del Despliegue**

Después de la instalación automática:  

✔ Ve a **AWS Lambda** en la consola de AWS y busca "MedicalRAG".  
✔ Ve a **DynamoDB** y verifica que existe la tabla "MedicalData".  
✔ Accede a la API en:  
  ```
  https://tu-api.aws.com/docs
  ```
✔ **Si todo está correcto, la IA ya está operativa.**  

---

## 📌 **5️⃣ Uso del Sistema**

El sistema ya está funcionando. Puedes enviar consultas desde:  

✅ **Interfaz Web**: *(Si está activada en tu despliegue)*  
✅ **ChatGPT / Otras IA**: *(Si lo configuraste con API Keys adicionales)*  

---

## 📌 **Soporte**

Si algo no funciona:  
1️⃣ Revisa los errores en **GitHub Actions > Workflows**.  
2️⃣ Verifica que ingresaste las credenciales correctamente en **Settings > Secrets**.  
3️⃣ Contacta con el equipo de soporte si es necesario.  

