import pytest
import json
from modules.supplement_interaction_validation import validate_supplement_interactions

def test_validate_supplement_interactions(tmp_path):
    supplement_data = tmp_path / "supplements.json"
    interactions_db = tmp_path / "interactions.json"
    
    supplement_data.write_text(json.dumps({"Omega 3": ["Warfarina"], "Vitamina C": []}))
    interactions_db.write_text(json.dumps({"Warfarina": ["Omega 3"]}))
    
    conflicts = validate_supplement_interactions(str(supplement_data), str(interactions_db))
    assert "Omega 3" in conflicts, "Debe detectar la interacción con Warfarina."
