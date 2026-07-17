import json

def carregar_hoteis():
    with open('hotels.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        return dados    


hoteis  = carregar_hoteis()
print(hoteis)