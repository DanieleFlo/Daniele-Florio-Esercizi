import requests as rq
import random
import json
import os
import time

# Creatte nele un programma python utilizzando le api
# https://pokeapi.co/api/v2/pokemon/ {numero} che simula un
# pokedex, quando troverete un pokemon in maniera randomica
# verificherà se è presen vostro pokedex (pokedex.json), in
# caso non fosse presente vi permetterà di catturarlo salvando il numero identificativo, nome, abilità, xp (punti esperienza),peso
# e altezza.
# (Sul sistema API sono presenti poco più di 1000 pokemon)


class Gioco():
    def __init__(self):
        self.link = 'https://pokeapi.co/api/v2/pokemon/'
        self.pokedex_file = 'pokedex.json'
        self.pokedex = {}
        if not os.path.exists(self.pokedex_file):
            with open(self.pokedex_file, "w", encoding = "utf-8") as f:
                json.dump(self.pokedex, f, indent = 4)
            pkm = self.get_pokemon_to_dex()
            self.set_pokedex(pkm)
            print('Il tuo primo pokemon è:', pkm['nome'])
        
    def get_pokemon_random(self):
        numero = random.randint(1, 1025)
        return self.link + str(numero)
    
    def get_pokemon_from_api(self):
        res = rq.get(self.get_pokemon_random())
        if res.status_code == 200:
            data = res.json()
            return data
        else:
            print('Errore nel recupero del pokemon.')
            return None
        
    def get_pokemons_from_json(self):
        with open(self.pokedex_file, "r", encoding = "utf-8") as f:
            return json.load(f)
    
    def controllo_pokemon_presente(self, id_pokemon):
        data = self.get_pokemons_from_json()
        if data.get(id_pokemon)!=None:
            return True  # pokemon presente in la pokedex
        return False
        
    def set_pokedex(self, pokemon):
        data = self.get_pokemons_from_json()
        data[pokemon['id']]=pokemon
        ## scrivi l'intero pokédex
        with open(self.pokedex_file, "w", encoding = "utf-8") as f:
            json.dump(data, f, indent = 4)
 
    def get_pokemon_to_dex(self):
        data = self.get_pokemon_from_api()
        nome = data['forms'][0]['name']
        ab = random.choice(data['abilities'])['ability']['name']
        weight = data['weight']
        exp = data['base_experience']
        height = data['height']
        stats = data['stats']
        hp = 0
        attack = 0
        speed = 0
        defense = 0
        for s in stats:
            if s['stat']['name']=='hp':
                hp = s['base_stat']
                
            if s['stat']['name']=='attack':
                attack = s['base_stat']
                
            if s['stat']['name']=='speed':
                speed = s['base_stat']
                
            if s['stat']['name']=='defense':
                defense = s['base_stat']
        data_p = {
            'id': data['id'],
            'nome': nome.upper(),
            'abilita': ab,
            'peso': weight,
            'xp': exp,
            'altezza': height,
            'hp': hp,
            'attack': attack,
            'speed': speed,
            'defense': defense,
        }
        return data_p
    
    def show_pokedex(self):
        data = self.get_pokemons_from_json()
        print('\nTutti i tuoi pokemon:')
        for p in data.values():
            print(f'ID: {p["id"]}, Nome: {p["nome"]}, Abilità: {p["abilita"]}, Peso: {p["peso"]/10} Kg, XP: {p["xp"]}, Altezza: {p['altezza']/10}m; HP: {p["hp"]}, Attack: {p["attack"]}')
    
    def scegli_pokemon(self):
        print('Scegli il pokemon con cui lottare')
        self.show_pokedex()
        pkm = self.get_pokemons_from_json()
        while True:
            nav = input('Dimmi l\'ID del pokemon da scegliere: ')
            if pkm.get(nav) is not None:
                break
            else:
                print('ID non valido!')
        return pkm[nav]
    
    def attack(self, attacker, defender):
        pkm_attack, hp_attack = attacker
        pkm_def, hp_def = defender
        print(f'\n-{pkm_attack["nome"]} attacca {pkm_def["nome"]}!\n')
        danno = pkm_attack['attack'] - pkm_def['defense']
        if danno<=0:
            danno = 1
        hp_def -= danno
        print(f'\t-{pkm_def["nome"]} è stato attaccato!')
        if hp_def <= 0:
            print(f'HP {pkm_def["nome"]} : {0}/{pkm_def["hp"]}')
            print(f'\n{pkm_def["nome"]} è esausto!')
        else:
            print(f'HP {pkm_def["nome"]} : {hp_def}/{pkm_def["hp"]}')
        return hp_def
    
    def lotta_pokemon(self, pkm_opp):
        p_temp= self.get_pokemons_from_json()
        if len(list(p_temp.values()))>1:
            my_pkm = self.scegli_pokemon()
        else:
            my_pkm = list(p_temp.values())[0]
        print(f'\nInizi la lotta tra {my_pkm["nome"]} e {pkm_opp["nome"]}')
        time.sleep(1)
        my_hp = my_pkm['hp']
        hp_opp = pkm_opp['hp']
        my_turno = True if my_pkm['speed'] > pkm_opp['speed'] else False
        while my_hp > 0 and hp_opp > 0:
            time.sleep(3)
            if my_turno:
                hp_opp = self.attack((my_pkm, my_hp), (pkm_opp, hp_opp))
                if hp_opp <= 0:
                    return '1'
            else:
                my_hp = self.attack((pkm_opp, hp_opp), (my_pkm, my_hp))
                if my_hp <= 0:
                    print(f'Non puo più continuare la lotta!')
                    return '2'
            my_turno = not my_turno
      
    def start(self):
        while True:
            nav = input('1: Vai nell\'erba alta, 2: Visualizza i tuoi pokemon, 3: Esci ')
            if nav == '1':
                while True:
                    nav_sub= '2'
                    data_p = self.get_pokemon_to_dex()
                    print('Camminando nell\'erba alta...\n')
                    time.sleep(3)
                    print(f'Appare un {data_p["nome"]} selvatico.\n') 
                    if self.controllo_pokemon_presente(data_p['id']):
                        print(f'\tQuesto {data_p["nome"]} è già presente nella tua pokedex!')
                    else:
                        nav_sub = input('1: Lotta, 2: Scappa ')
                        if nav_sub == '1':
                            nav_sub= self.lotta_pokemon(data_p)
                        
                    if nav_sub == '1':
                        rand = random.randint(0,5)
                        if rand >0:
                            self.set_pokedex(data_p) # Salva il pokemon nel pokedex da inseririre
                            time.sleep(3)
                            print(f'\tPreso! {data_p["nome"]} è stato catturato!')
                            print(f'\tInfo:\n\tAbilità: {data_p["abilita"]}\n\tPeso: {data_p["peso"]} Kg\n\tXP: {data_p["xp"]}, Altezza: {data_p['altezza']/10}m; HP: {data_p["hp"]}, Attack: {data_p["attack"]}')
                            
                        else:
                            print('Oh no il pokemon si è liberato ed è scappato!')
                    elif nav_sub == '2':
                        print('Scampato pericolo!')
                        break
                    else:
                        print('Scelta non valida.')
            elif nav == '2':
                self.show_pokedex()
            elif nav == '3':
                break
            else:
                print('Scelta non valida.')
        
gioco =  Gioco()
gioco.start()


