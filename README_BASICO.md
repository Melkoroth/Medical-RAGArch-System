
# Medical-RAGArch-System (Versión Básica)

Este proyecto es una aplicación que permite analizar datos médicos y generar informes personalizados. 
Está diseñado para ser fácil de usar, sin necesidad de conocimientos técnicos avanzados.

---

## Funcionalidad Principal
- Analiza datos médicos como resultados de analíticas. 
- Genera informes personalizados con explicaciones sencillas.
- Permite subir archivos y obtener análisis detallados.

---

## Requisitos Previos
Antes de empezar, asegúrate de tener instalados los siguientes programas:
- **Python 3.x** (Recomendado: Python 3.8 o superior)
- **Git** (Opcional, solo si deseas clonar el repositorio en lugar de descargar el ZIP)

---

## Instalación y Configuración
Sigue estos pasos para instalar y configurar el proyecto:

1. **Descargar el Proyecto**  
   - Puedes descargar el archivo ZIP desde GitHub o desde el enlace proporcionado.
   - Extrae el contenido del ZIP en una carpeta de tu elección.

2. **Instalar Dependencias**  
   Abre una terminal en la carpeta del proyecto y ejecuta los siguientes comandos:
   ```bash
   python -m venv venv  # Crea un entorno virtual
   source venv/bin/activate  # Activa el entorno en Linux/Mac
   .\venv\Scripts\activate  # Activa el entorno en Windows
   pip install -r requirements.txt  # Instala las dependencias
   ```

3. **Ejecutar el Proyecto**  
   Una vez instaladas las dependencias, inicia el servidor con el siguiente comando:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 7860
   ```
   Luego, abre un navegador web y accede a:
   ```
   http://localhost:7860
   ```

---

## Uso Básico
- **Sube un archivo** con los datos médicos que deseas analizar.
- **Obtén un informe personalizado** con explicaciones sencillas.
- **Explora los resultados** y guarda el informe en tu dispositivo.

---

## Soporte y Ayuda
Si tienes problemas o preguntas, puedes obtener ayuda en la sección de **Issues** del repositorio de GitHub.

---

## Notas Importantes
- Este proyecto está diseñado para **usuarios no técnicos**. No necesitas conocimientos de programación para usarlo.
- **No se requiere configurar Redis, CI/CD ni AWS Lambda** para usar las funcionalidades básicas.
