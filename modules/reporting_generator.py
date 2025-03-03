import json
import pandas as pd
from fpdf import FPDF

def generate_report(data_file, output_format="pdf"):
    """Genera informes clínicos en PDF, JSON o Excel según el formato especificado."""
    with open(data_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    if output_format == "json":
        with open("clinical_report.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
        return "clinical_report.json"

    elif output_format == "xlsx":
        df = pd.DataFrame(data)
        df.to_excel("clinical_report.xlsx", index=False)
        return "clinical_report.xlsx"

    elif output_format == "pdf":
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for key, value in data.items():
            pdf.cell(200, 10, f"{key}: {value}", ln=True, align="L")
        pdf.output("clinical_report.pdf")
        return "clinical_report.pdf"
