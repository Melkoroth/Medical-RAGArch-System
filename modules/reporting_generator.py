
from fpdf import FPDF

# Función para generar reporte en múltiples idiomas
def generar_reporte(titulo, contenido, lang='eng'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font('Arial', 'B', 14)
    
    # Soporte de idiomas
    if lang == 'spa':
        pdf.set_title('Informe Clínico')
        pdf.cell(0, 10, 'Informe Clínico', ln=True, align='C')
    elif lang == 'cat':
        pdf.set_title('Informe Clínic')
        pdf.cell(0, 10, 'Informe Clínic', ln=True, align='C')
    else:
        pdf.set_title('Clinical Report')
        pdf.cell(0, 10, 'Clinical Report', ln=True, align='C')
    
    pdf.set_font('Arial', '', 12)
    pdf.ln(10)
    pdf.multi_cell(0, 10, contenido)
    
    return pdf
