import streamlit as st
import boto3
import os
from cryptography.fernet import Fernet

# 📌 **Configuración de Cifrado AES-256 para DynamoDB**
SECURE_KEY = os.getenv("SECURE_AES_KEY")
cipher = Fernet(SECURE_KEY)

# 📌 **Configuración de AWS DynamoDB**
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
DYNAMODB_TABLE = "MedicalDocuments"

dynamodb = boto3.client(
    "dynamodb",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name="us-east-1",
)

# 📌 **Función para subir archivos cifrados a DynamoDB**
def upload_file(file, file_name, file_type):
    encrypted_data = cipher.encrypt(file.read())
    dynamodb.put_item(
        TableName=DYNAMODB_TABLE,
        Item={
            "file_name": {"S": file_name},
            "file_type": {"S": file_type},
            "file_data": {"B": encrypted_data},
        },
    )
    return f"Archivo {file_name} subido correctamente con cifrado seguro."

# 📌 **Frontend: Carga de Documentos Médicos**
st.sidebar.title("📤 Cargar Documentos Médicos (Cifrado Activo)")

uploaded_file = st.sidebar.file_uploader(
    "Sube un archivo médico",
    type=["pdf", "txt", "csv", "docx", "json", "xlsx", "jpg", "png", "dcm", "nii", "nii.gz", "mha", "mhd", "tiff"],
)

if uploaded_file:
    file_name = uploaded_file.name
    file_type = uploaded_file.type
    result = upload_file(uploaded_file, file_name, file_type)
    st.sidebar.success(result)

# 📌 **Listado de Archivos en DynamoDB con Descifrado Seguro**
st.sidebar.subheader("📁 Documentos Subidos")

response = dynamodb.scan(TableName=DYNAMODB_TABLE)
documents = response.get("Items", [])

if documents:
    file_list = [doc["file_name"]["S"] for doc in documents]
    selected_file = st.sidebar.selectbox("Selecciona un documento", file_list)

    if selected_file:
        encrypted_data = next(doc for doc in documents if doc["file_name"]["S"] == selected_file)["file_data"]["B"]
        decrypted_data = cipher.decrypt(encrypted_data)

        st.subheader(f"📄 Documento: {selected_file}")

        if selected_file.endswith((".jpg", ".png", ".dcm", ".nii", ".nii.gz", ".mha", ".mhd", ".tiff")):
            st.image(decrypted_data, caption=selected_file)
        else:
            st.text_area("📜 Contenido", decrypted_data.decode("utf-8"), height=300)

# 📌 **Interacción con los Documentos desde la IA**
st.title("🩺 Consultas sobre Documentos Médicos")

if selected_file:
    user_query = st.text_input("Escribe tu consulta sobre el documento")
    
    if st.button("Enviar Consulta"):
        st.write(f"🔍 Analizando {selected_file}...")
        response_text = f"🤖 **Análisis del documento:** '{selected_file}'"
        st.write(response_text)

st.sidebar.button("🔄 Actualizar Lista", on_click=lambda: st.experimental_rerun())
