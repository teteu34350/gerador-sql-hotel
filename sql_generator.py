def gerar_sql(dados, id_hotel):
    """
    Recebe um DataFrame e gera o SQL.
    """

    data_inicio = dados["Data"].min().strftime("%Y-%m-%d")
    data_fim = dados["Data"].max().strftime("%Y-%m-%d")

    linhas_when = []

    for _, linha in dados.iterrows():

        data = linha["Data"].strftime("%Y-%m-%d")
        quantidade = linha["Manutenção"]

        linhas_when.append(
            f"WHEN '{data}' THEN {quantidade}"
        )

    bloco_when = "\n".join(linhas_when)

    sql = f"""UPDATE data_PMS_maintenance
SET quant = CASE day

{bloco_when}

END
WHERE id_hotel = {id_hotel}
AND day BETWEEN '{data_inicio}' AND '{data_fim}';"""

    return sql