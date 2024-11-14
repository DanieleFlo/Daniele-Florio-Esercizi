import requests as rq
import random
import json

# Create un programma python utilizzando le api
# https://pokeapi.co/api/v2/pokemon/ {numero} che simula un
# pokedex, quando troverete un pokemon in maniera randomica
# verificherà se è presente nel vostro pokedex (pokedex.json), in
# caso non fosse presente vi permetterà di catturarlo salvando il numero identificativo, nome, abilità, xp (punti esperienza),peso
# e altezza.
# (Sul sistema API sono presenti poco più di 1000 pokemon)


class Gioco():
    def __init__(self):
        self.link = 'https://pokeapi.co/api/v2/pokemon/'
        self.pokedex_file = 'pokedex.json'
        
    def get_pokemon_random(self):
        numero = random.randint(1, 1025)
        print(numero)
        return self.link + str(numero)
    
    def get_pokemon_info(self):
        res = rq.get(self.get_pokemon_random())
        if res.status_code == 200:
            data = res.json()
            return data
        else:
            print('Errore nel recupero del pokemon.')
            return None
        
    def get_pokedex(self):
        pass
        
    def save_pokemon_to_dex(self):
        data = gioco.get_pokemon_info()
        nome = data['forms'][0]['name']
        ab = random.choice(data['abilities'])['ability']['name']
        weight = data['weight']
        exp = data['base_experience']
        height = data['height']
        data_p ={
            'id': data['id'],
            'nome': nome,
            'abilita': ab,
            'peso': weight,
            'xp': exp,
            'altezza': height
        }
        
gioco =  Gioco()
gioco.save_pokemon_to_dex()