
# Medical-RAGArch-System

## 📌 ¿Qué es este proyecto?
Medical-RAGArch-System es un sistema de **IA aplicada a documentos médicos**, que permite:
- **Almacenar, procesar y recuperar información estructurada** de documentos médicos.
- **Optimizar la infraestructura en la nube con AWS Lambda y DynamoDB**.
- **Automatizar despliegues y mantenimiento** con GitHub Actions y AWS CDK.

Esta versión incluye mejoras clave en rendimiento, seguridad y escalabilidad.

## 🚀 Mejoras Implementadas en esta Versión

# Medical-RAGArch-System

## 🚀 Mejoras Implementadas en esta Versión

### 🔹 1. Optimización del Despliegue en AWS (GitHub Actions + AWS CDK)
- **Se ha agregado caching en GitHub Actions** para acelerar la instalación de dependencias.
- **Se ha migrado el uso de variables de entorno a AWS Secrets Manager** para mayor seguridad.
- **Se ha sustituido el despliegue manual por CDK Pipelines**, lo que mejora la automatización.

### 🔹 2. Optimización de FastAPI en AWS Lambda (aarch64)
- **Se ha integrado AWS Lambda Power Tuning** para optimizar memoria y CPU.
  - Para ejecutarlo manualmente, sigue estos pasos:
    1. Ve a la consola de AWS Lambda.
    2. Busca tu función Lambda.
    3. Usa la herramienta AWS Lambda Power Tuning para encontrar la mejor configuración.
- **Se ha añadido compatibilidad con AWS Lambda SnapStart**.
  - *Antes de activarlo, verifica si es compatible con FastAPI en la consola de AWS.*
  - Pasos para activarlo:
    1. Ve a la consola de AWS Lambda.
    2. Selecciona la función de FastAPI.
    3. En la pestaña "Configuración", busca "SnapStart" y actívalo.

### 🔹 3. Escalabilidad de DynamoDB
- **Se ha habilitado Auto Scaling y Adaptive Capacity** para mejorar el rendimiento.
- **Se ha optimizado la escritura con BatchWriteItem**, reduciendo latencias.
- **Se ha preparado el soporte para DAX (DynamoDB Accelerator)**.
  - Para activarlo manualmente:
    1. Ve a la consola de AWS DynamoDB.
    2. Crea una nueva instancia de DAX.
    3. Configura la aplicación para conectarse a la instancia DAX.

### 📌 Notas Adicionales
- **Si usas AWS Lambda SnapStart o DAX, debes activarlos manualmente en AWS Console.**
- **Si tienes tráfico predecible en DynamoDB, considera cambiar a "Provisioned" con Auto Scaling.**

### 🔹 4. Creación Automática de DynamoDB Accelerator (DAX)
- **DAX (DynamoDB Accelerator) mejora la velocidad de las consultas**.
- **Este sistema ahora crea automáticamente un clúster DAX en AWS CDK.**

📌 **Configuración Manual Necesaria**:
1. **Configurar Subnet Group en AWS Console** para que el clúster pueda operar.  
2. **Agregar Security Groups si es necesario**, según la arquitectura de red de AWS.  
3. **Actualizar la configuración de la aplicación para conectarse a DAX en vez de DynamoDB directamente.**

### 🔹 5. Activación Manual de AWS Lambda SnapStart
- **SnapStart reduce el tiempo de arranque de Lambda** y mejora la latencia.
- **Debe activarse manualmente en la consola de AWS**, ya que AWS no permite su activación automática desde CDK.

📌 **Pasos para activarlo**:
1. Ir a **AWS Lambda Console** y seleccionar la función Lambda de FastAPI.
2. En la pestaña **Configuración**, buscar la opción **SnapStart** y activarla.
3. Guardar los cambios y probar la ejecución.


## 🔹 6. Automatización Completa de la Infraestructura en AWS

### ✅ **¿Qué se crea automáticamente en AWS?**
Cuando ejecutas el despliegue, **AWS CDK crea y configura automáticamente los siguientes recursos:**

1. **DynamoDB**: Base de datos NoSQL con Auto Scaling.
2. **DAX (DynamoDB Accelerator)**: Caché de alto rendimiento para DynamoDB.
3. **S3 Bucket**: Almacenamiento para documentos.
4. **IAM Roles**: Permisos para Lambda, DynamoDB y S3.
5. **FastAPI en AWS Lambda**: Aplicación desplegada sin necesidad de servidores.

### 🚀 **Pasos para Desplegar el Proyecto en AWS**

1️⃣ **Crear una cuenta en AWS (si no tienes una):**  
   - Ir a [AWS](https://aws.amazon.com/) y registrarse.
   - Configurar un usuario en IAM con permisos administrativos.
   - Obtener **AWS_ACCESS_KEY_ID** y **AWS_SECRET_ACCESS_KEY** en la consola de IAM.

2️⃣ **Configurar Credenciales en GitHub:**  
   - Ir a **Settings** → **Secrets and variables** → **Actions**.
   - Crear dos secrets:
     - `AWS_ACCESS_KEY_ID`: Tu clave de acceso de AWS.
     - `AWS_SECRET_ACCESS_KEY`: Tu clave secreta de AWS.

3️⃣ **Ejecutar el Despliegue en GitHub Actions:**  
   - Ir a **GitHub Actions** en tu repositorio.
   - Seleccionar `Deploy to AWS`.
   - Hacer clic en **Run workflow**.

4️⃣ **Configurar Manualmente en AWS Console (Solo 2 pasos):**  
   - **DAX (DynamoDB Accelerator)**: Configurar **Subnet Groups y Security Groups** en AWS Console.  
   - **Lambda SnapStart**: Activarlo manualmente en la consola de AWS.  

### ✅ **¿Qué NO tienes que hacer manualmente?**
✅ No necesitas crear ni configurar DynamoDB.  
✅ No necesitas configurar roles IAM ni permisos.  
✅ No necesitas subir archivos a S3 manualmente.  
✅ No necesitas hacer despliegues manuales en AWS Lambda.  

Este sistema está **100% automatizado**, excepto por la creación de la cuenta y la activación de DAX/SnapStart.

