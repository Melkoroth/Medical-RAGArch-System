
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

# 🚀 Medical-RAGArch-System - Guía de Despliegue Técnico

Esta guía contiene las instrucciones esenciales para desplegar el sistema en AWS sin configuraciones manuales.

---

## 📌 **1️⃣ Requisitos Previos**

Antes de desplegar, asegúrate de tener:

✅ **Cuenta de AWS** con permisos para Lambda, DynamoDB y API Gateway.  
✅ **GitHub Actions habilitado** en tu repositorio.  
✅ **AWS CLI instalado y configurado** (`aws configure`).  
✅ **Variables de entorno en GitHub Secrets** (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`).  

---

## 📌 **2️⃣ Instalación y Configuración**

1️⃣ **Clonar el repositorio**  
```bash
git clone https://github.com/tu-repositorio/Medical-RAGArch-System.git
cd Medical-RAGArch-System
```  

2️⃣ **Instalar dependencias optimizadas**  
```bash
pip install --prefer-binary -r requirements.txt
```  

3️⃣ **Configurar claves de seguridad con AWS Secrets Manager**  
```bash
python aws/secrets_manager.py
```  

Esto almacenará automáticamente las claves de cifrado en AWS y las hará accesibles para el sistema.  

---

## 📌 **3️⃣ Despliegue en AWS Lambda**

✅ **Automático (Recomendado):**  
Haz un `push` al repositorio y GitHub Actions desplegará en AWS automáticamente:  
```bash
git push origin main
```  

✅ **Manual (Opcional):**  
Si necesitas desplegar manualmente, ejecuta:  
```bash
cd aws/
python lambda_snapstart.py
```  

---

## 📌 **4️⃣ Verificación del Despliegue**

📌 **Después del despliegue, verifica:**  

✅ AWS Lambda tiene la función `"MedicalRAG"` correctamente configurada.  
✅ DynamoDB tiene la tabla `"MedicalData"`.  
✅ Puedes acceder a la API en:  
```bash
https://tu-api.aws.com/docs
```  

---

## 📌 **5️⃣ Estructura de Seguridad con AWS Secrets Manager**

- **`aws/secrets_manager.py`** gestiona las claves de cifrado automáticamente.  
- **`config/aes_config.py`** y **`config/jwt_config.py`** obtienen las claves desde AWS Secrets Manager.  

✅ **No es necesario almacenar claves en el código, todo se gestiona automáticamente.**  

---

## 📌 **6️⃣ Workflows de GitHub Actions para Despliegue**

El despliegue automático usa estos workflows:

| Workflow | Función |
|----------|--------|
| `deploy.yml` | Despliega automáticamente en AWS Lambda |
| `update_prompts.yml` | Sincroniza los prompts con GitHub |
| `deploy_with_secrets.yml` | Configura variables de entorno automáticamente |

📌 **Si hay errores en el despliegue, revisa GitHub Actions en tu repositorio.**  

---

## 📌 **Soporte y Contacto**

Si necesitas ayuda, revisa la documentación principal o contacta con el equipo.

