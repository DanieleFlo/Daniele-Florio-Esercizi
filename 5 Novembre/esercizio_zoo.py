#Esercizio sull'ereditarietà
import random

class Animale():
    suono = ''
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
        
    def fai_suono(self):
        return f"Il {self.nome} fa {self.suono}!"
    
    def stampa_eta(self):
        return self.eta
    
    def stampa_nome(self):
        return self.nome
        
class Leone(Animale):
    def __init__(self, eta, nome = 'Leone'):
        Animale.__init__(self, nome, eta)
    
    def fai_suono(self):
        self.suono = 'Roar'
        return super().fai_suono()
        
    def azione(self):
        y = random.randint(0, 1)
        if y == 1:
            return f"Il {self.nome} ha cacciato!"
        else:
            return f"Il {self.nome} non ha cacciato!"
            
            
class Pinguino(Animale):
    def __init__(self, eta, nome = 'Pinguino'):
        Animale.__init__(self, nome, eta)
        
    def fai_suono(self):
        self.suono = 'AAAH'
        return super().fai_suono()
        
    def azione(self):
        y = random.randint(0, 1)
        if y == 1:
            return f"Il {self.nome} sta nuotando!"
        else:
            return f"Il {self.nome} non sta nuotando!"
            


class Zoo():
    lista_animali = []
    choise_animale = ['Pinguino', 'Leone']
    id =  0
    def aggiungi_animale(self, tipo, eta, qty):
        if tipo in self.choise_animale:
            if tipo== 'Pinguino':
                 self.add(Pinguino(eta), qty)
            elif tipo == 'Leone':
                 self.add(Leone(eta), qty)
        else:
            print('Scelta non valida!')
    
    def add(self, classe, qty):
        self.lista_animali.append({
            'id': self.id,
            'classe': classe,
            'qty': qty,
        })
        self.id += 1
            
    def stampa_animali(self):
        for animale in self.lista_animali:
            print(f"Animale: {animale['classe'].stampa_nome()}, eta: {animale['classe'].stampa_eta()}, verso: {animale['classe'].fai_suono()},  qty: {animale['qty']}, azione: {animale['classe'].azione()}")
    
zoo = Zoo()
zoo.aggiungi_animale('Pinguino', 1, 12)
zoo.aggiungi_animale('Pinguino', 2, 12)
zoo.aggiungi_animale('Leone', 12, 1)
zoo.aggiungi_animale('Leone', 5, 2)
zoo.stampa_animali()