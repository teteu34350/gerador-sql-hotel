import pandas as pd
def listar_abas(caminho_arquivo):
    excel = pd.ExcelFile(caminho_arquivo)
    return excel.sheet_names
def ler_planilha(caminho_arquivo,aba):
    """
    Lê a planilha do Excel e retorna um DataFrame tratado.
    """

    dados = pd.read_excel(
        caminho_arquivo,
        sheet_name= aba,  
        usecols=["Data", "Manutenção"]
    )

    # Remove linhas vazias
    dados = dados.dropna(subset=["Data", "Manutenção"])

    # Converte a data
    dados["Data"] = pd.to_datetime(dados["Data"])

    # Garante que manutenção seja inteiro
    dados["Manutenção"] = dados["Manutenção"].astype(int)

    # Ordena pelas datas
    dados = dados.sort_values("Data")

    return dados

