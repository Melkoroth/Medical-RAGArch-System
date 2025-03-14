import pytest
import os
from modules.report_generation import generate_report

def test_generate_pdf_report(tmp_path):
    output_pdf = tmp_path / "test_report.pdf"
    generate_report("tests/sample_data.json", str(output_pdf))
    assert output_pdf.exists(), "El PDF no se generó correctamente."
