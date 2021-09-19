import os
import requests
import json
with open('poke_names.json', encoding="utf8") as pkmns:
    data = json.load(pkmns)


def down_sprite(url, endereco):
    print(url)
    resposta = requests.get(url)
    with open(endereco, 'wb') as novo_arquivo:
        novo_arquivo.write(resposta.content)
        print('concluido. Salvo em: {}'.format(endereco))


if __name__ == "__main__":
    BASE_URL = 'https://img.pokemondb.net/artwork/large/{}.jpg'
    OUTPUT_DIR = 'sprites'
    for i in range (1, 152):        
        name = data[i]      
        endereco = os.path.join(OUTPUT_DIR, '{}.jpg'.format(name.lower()))
        down_sprite(BASE_URL.format(name.lower()), endereco)