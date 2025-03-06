
# Medical-RAGArch-System (Versión Básica)

## 🚀 Cambios Recientes
- Se ha optimizado el despliegue con GitHub Actions y AWS CDK.
- Se ha mejorado la ejecución en AWS Lambda con Power Tuning y SnapStart (*requiere activación manual*).
- Se ha escalado DynamoDB con Auto Scaling y optimización de escrituras.

## 📌 Configuraciones Manuales Necesarias
Si quieres aprovechar todas las optimizaciones, revisa:
1. **Ejecutar Lambda Power Tuning** en AWS.
2. **Activar SnapStart** en la consola de AWS Lambda.
3. **Activar DAX en DynamoDB** (si lo necesitas).

## 📚 Documentación Completa
Consulta `README.md` para más detalles.

## 🚀 **Despliegue Rápido en AWS**

### ✅ **Pasos para ponerlo en marcha:**
1️⃣ **Crear una cuenta en AWS (si no tienes una).**  
2️⃣ **Ir a GitHub → Settings → Secrets → Actions** y agregar:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
3️⃣ **Ejecutar el Despliegue en GitHub Actions.**  

📌 **Solo necesitas configurar manualmente en AWS:**  
- **DAX (DynamoDB Accelerator):** Configurar Subnet Groups y Security Groups.  
- **Lambda SnapStart:** Activarlo en la consola de AWS.  

📚 Para detalles completos, revisa `README.md`.
