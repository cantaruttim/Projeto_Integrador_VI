import streamlit as st
import os

st.title("Upload de Arquivo PDF")

# Permitir upload de arquivo
uploaded_file = st.file_uploader("Escolha um arquivo PDF", type="pdf")

if uploaded_file is not None:
    # Salvar o arquivo na pasta 'files'
    file_path = os.path.join("file", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.write("Você enviou:", uploaded_file.name)
    st.write(f"O arquivo foi salvo em: {file_path}")
    