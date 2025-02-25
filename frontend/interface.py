import gradio as gr

def compare_versions(local_data, backup_data):
    """Compara dos versiones de datos y devuelve las diferencias."""
    differences = []

    for key in local_data:
        if key in backup_data and local_data[key] != backup_data[key]:
            differences.append(f"🟡 Cambio en {key}: \n - Anterior: {backup_data[key]} \n - Nuevo: {local_data[key]}")

    return differences if differences else ["✅ No hay cambios significativos."]

iface = gr.Interface(fn=compare_versions, inputs=[], outputs="text", title="Comparar versiones de Prompts")
iface.launch()
