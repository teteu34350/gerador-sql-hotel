import json

def carregar_hoteis():
    with open('hotels.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        return dados    
def listar_nomes():
     hoteis = carregar_hoteis()
     nome  = []
     for hotel in hoteis:
         nome.append(hotel['Nome'])
     return nome
def buscar_id(nome_hotel):
    hoteis  = carregar_hoteis()
    for hotel in hoteis:
        if hotel['Nome'] == nome_hotel:
            return hotel['ID_hotel']
    return None

print(carregar_hoteis())
print(listar_nomes())
print(buscar_id('Máceio Mar RESORT'))
