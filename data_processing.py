import re
import pandas as pd
import io
import os

def tratar_tabelas(texto):
    regra = re.compile(r"((?:\|.+\|(?:\n|\r))+)", re.MULTILINE)
    tabelas = regra.findall(texto)
    return tabelas

def transformar_markdown(texto, num_pagina):
    # identificar as tabelas que estao no texto
    lista_texto = tratar_tabelas(texto)
    if len(lista_texto) > 0:
        for i, texto_tabela in enumerate(lista_texto):
            tabela = pd.read_csv(io.StringIO(texto_tabela)
                                 , sep="|"
                                 , encoding="utf-8"
                                 , engine="python"
                            )
            tabela = tabela.dropna(how="all", axis = 1)
            tabela = tabela.dropna(how="all", axis = 0)

            tabela.to_excel(f"tabelas/Pagina{num_pagina}_Tabela{i+1}.xlsx", index=False)
        
pasta_paginas = "saida_pdf"
list_paginas = os.listdir(pasta_paginas)

for i, pagina in enumerate(list_paginas):
    with open(f"{pasta_paginas}/{pagina}" ,"r", encoding="utf-8") as arquivo:
        texto = arquivo.read()

    num_pagina = i + 1
    transformar_markdown(texto, num_pagina)
    