"""
Classe operaio con due figli

avere 2 classi astratte come secondo genitore, una per uno, dei figli di operaio
classi astratte: cazzuola e martello
"""
from abc import ABC, abstractmethod

# Classi astratte
class Caccuola(ABC):
    
    @abstractmethod
    def impasta_cemento(self):
        pass

class Mazza(ABC):
    
    @abstractmethod
    def piega_ferro(self):
        pass

# Classse padre
class Operaio():
    def __init__(self, nome, cognome, anno_nascita):
        self.nome = nome
        self.cognome = cognome
        self.anno_nascita = anno_nascita

    def presentati(self):
        print(f"Ciao sono: {self.nome} {self.cognome} e ho sono nato nel {self.anno_nascita}.")
        
# Classi figlie
class Muratore(Operaio, Caccuola):
    def __init__(self, nome, cognome, anno_nascita):
        super().__init__(nome, cognome, anno_nascita)
    
    def impasta_cemento(self):
        print("Impasto il cemento e sotto il sole mi spacco le nocche!.")
        
class Fabbro(Operaio):
    def __init__(self, nome, cognome, anno_nascita):
        super().__init__(nome, cognome, anno_nascita)
        
    def piega_ferro(self):
        print("Piego il ferro per il nuovo cancello!")

muratore = Muratore('Luigi', 'Delle Bicocche', 1972)
muratore.presentati()
muratore.impasta_cemento()

muratore = Fabbro('Massimo', 'Delle Bicocche', 1972)
muratore.presentati()
muratore.piega_ferro()