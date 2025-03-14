import json

def validate_supplement_interactions(supplement_data_file, interactions_db_file):
    """Valida interacciones entre suplementos y medicamentos usando una base de datos."""
    with open(supplement_data_file, "r", encoding="utf-8") as sup_file:
        supplements = json.load(sup_file)
    
    with open(interactions_db_file, "r", encoding="utf-8") as db_file:
        interactions_db = json.load(db_file)

    results = []
    for supplement in supplements:
        for interaction in interactions_db["interacciones"]:
            if supplement["name"] in [interaction.get("medicamento_1"), interaction.get("suplemento")]:
                results.append({
                    "suplemento": supplement["name"],
                    "interacción": interaction["efecto"],
                    "nivel_riesgo": interaction["nivel_riesgo"],
                    "recomendación": interaction["recomendacion"]
                })
    
    return results
