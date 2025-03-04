import pytest
import os
from modules.analytics_comparison import plot_clinical_trends

def test_plot_clinical_trends(tmp_path):
    sample_data = tmp_path / "sample_data.json"
    sample_data.write_text('{"glucose": [90, 100, 110]}')
    
    try:
        plot_clinical_trends(str(sample_data))
        assert True, "Se generó el gráfico correctamente."
    except Exception as e:
        pytest.fail(f"Error al generar el gráfico: {e}")
