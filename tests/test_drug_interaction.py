import pytest
from modules.drug_interaction_api import check_interaction

@pytest.mark.parametrize("med1, med2", [
    ("Paracetamol", "Ibuprofeno"),
    ("Metformina", "Insulina"),
    ("Atorvastatina", "Aspirina")
])
def test_check_interaction(med1, med2):
    result = check_interaction(med1, med2)
    assert isinstance(result, dict), "El resultado debe ser un diccionario."
