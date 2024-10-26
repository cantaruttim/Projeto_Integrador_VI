import os
from llama_parse import LlamaParse

os.environ["LLAMA_CLOUD_API_KEY"] = "llx-X6eyftaZPqtXgYDxBVrgG4jKkt4C6W07kyMvO9D1OtK8U4ol"

documento = LlamaParse(result_type="markdown"
                       , language="pt"
                       , parsing_instruction = "This file contains text and tables. I would like to get only the tables from the file."
                       ).load_data("file/Divulgação de Resultados 2T24.pdf")

if not os.path.exists("./saida_pdf"):
    os.makedirs("./saida_pdf")

for i, pagina in enumerate(documento):
    with open(f"./saida_pdf/pagina{i+1}.md", "w", encoding="utf-8") as arquivo:
        arquivo.write(pagina.text)
