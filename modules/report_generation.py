"""
Módulo de generación automática de reportes en RAGArch, ahora con cifrado en PDF.
"""

import os
import pandas as pd
import pdfkit
from cryptography.fernet import Fernet

# Obtener clave de cifrado para PDFs
PDF_ENCRYPTION_KEY = os.getenv("PDF_ENCRYPTION_KEY", Fernet.generate_key())

def generate_biomarker_report(data: pd.DataFrame, output_file="biomarker_report.pdf"):
    """
    Genera un reporte en PDF con cifrado de información.
    """
    html_content = f"""
    <html>
    <head><title>Reporte de Biomarcadores</title></head>
    <body>
    <h2>Reporte de Biomarcadores</h2>
    {data.to_html(index=False)}
    </body>
    </html>
    """

    pdfkit.from_string(html_content, output_file)

    # Cifrar el PDF
    cipher = Fernet(PDF_ENCRYPTION_KEY)
    with open(output_file, "rb") as file:
        encrypted_data = cipher.encrypt(file.read())

    with open(output_file, "wb") as file:
        file.write(encrypted_data)

    print(f"Reporte cifrado generado: {output_file}")
