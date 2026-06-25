import pandas as pd


def gerar_relatorio(dados):


    tabela = pd.DataFrame(dados)


    tabela.to_excel(

        "relatorio.xlsx",

        index=False

    )