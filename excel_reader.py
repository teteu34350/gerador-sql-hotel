import pandas as pd

def ler_arquivo():
    dados = pd.read_excel(
        "teste.xlsx",
        sheet_name="JUL-26",
        usecols=["Data", "Manutenção"],dtype={"Manutenção":str}
    )
    return dados

print(ler_arquivo())