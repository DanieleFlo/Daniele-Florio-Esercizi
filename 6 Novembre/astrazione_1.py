""""
creare una classe base Veicolo con attributi comuni a tutti i veicoli 
e metodi per operazioni comuni come l'accensione e lo spegnimento. 
Derivando questa classe, creeranno specifiche classi per Auto, Furgone 
e Motocicletta, aggiungendo caratteristiche uniche per ciascun tipo di veicolo. 
Infine, dovranno implementare una classe GestoreParcoVeicoli per 
amministrare l'insieme dei veicoli.

Classe Veicolo:
Attributi privati:
_marca (stringa)
_modello (stringa)
_anno (intero)
_accensione (booleano)
Metodi:
accendi(): cambia lo stato di _accensione a vero.
spegni(): cambia lo stato di _accensione a falso.
Classi Derivate:
Auto:
Attributi aggiuntivi come _numero_porte
Metodo specifico come suona_clacson()
Furgone:
Attributi per _capacità_carico
Metodo per carica() e scarica()
Motocicletta:
Attributo per _tipo (e.g., sportiva, touring)
Metodo per esegui_wheelie() se il tipo è sportivo
Classe GestoreParcoVeicoli:
Attributi:
_veicoli: lista di tutti i veicoli.
Metodi:
aggiungi_veicolo(veicolo): aggiunge un veicolo alla lista.
rimuovi_veicolo(marca, modello): rimuove un veicolo specifico dalla lista.
lista_veicoli(): stampa un elenco di tutti i veicoli nel parco.
"""

from abc import ABC, abstractmethod

## astratto perché eredita da ABC
class Veicolo(ABC):
    def __init__(self, marca, modello, anno, accensione = "spento"):
        self._marca = marca
        self._modello = modello
        self._anno = anno
        self._accensione = accensione

    def get_marca(self):
        return self._marca
    
    def get_modello(self):
        return self._modello
    
    def get_anno(self):
        return self._anno
    
    def get_accensione(self):
        return self._accensione
    
    def toggle_accensione(self):
        if self._accensione == "acceso": self._accensione = "spento"
        else: self._accensione == "spento"

    def accendi(self):
        if self.get_accensione == "spento": self.toggle_accensione()

    def spegni(self):
        if self.get_accensione == "acceso": self.toggle_accensione()
    
    ## metodo mostra informazioni è astratto e fa solo pass, saranno le sottoclassi a implementarlo
    @abstractmethod
    def mostra_informazioni(self):
        pass

class Furgone(Veicolo):
    def __init__(self, marca, modello, anno, capacita, carico_attuale = 0, accensione = "spento"):
        super().__init__(marca, modello, anno, accensione)
        self.capacita = capacita
        self.carico_attuale = carico_attuale

    ## ho bisogno di controllare se il nuovo peso sia eccessivo o no
    def check_capacita(self, carico):
        return self.capacita >= self.carico_attuale + carico
    
    def carica(self, carico):
        if self.check_capacita(carico): self.carico_attuale += carico

    def scarica(self, carico):
        if not self.carico > self.carico_attuale: self.carico_attuale -= carico
        else: print("Carico da togliere inferiore alla capacità attuale")

    ## implemento il metodo astratto della classe padre Veicolo
    def mostra_informazioni(self):
        stringa = "Il veicolo è della marca " + self._marca + " e del modello: " + self._modello + ". Prodotto nell'anno " + str(self._anno) + " ed è attualmente " + self._accensione
        stringa += ", il furgone ha una capacità di carico pari a: " + str(self.capacita) + " attualmente sta trasportando " + str(self.carico_attuale)
        return stringa


class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte, accensione = "spento"):
        super().__init__(marca, modello, anno, accensione)
        self._numero_porte = numero_porte

    def get_numero_porte(self):
        return self._numero_porte

    ## implemento il metodo astratto della classe padre Veicolo
    def mostra_informazioni(self):
        stringa = "Il veicolo è della marca " + self._marca + " e del modello: " + self._modello + ". Prodotto nell'anno " + str(self._anno) + " ed è attualmente " + self._accensione
        stringa += ", l'auto ha " + str(self._numero_porte) + " porte"
        return stringa


class Motocicletta(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self._tipo = tipo

    ## mi assicuro che il tipo di motocicletta sia sportiva, altrimenti non è adatta al wheelie
    def esegui_wheelie(self):
        if self._tipo.lower() == "sportiva":
            print("La motocicletta sportiva sta facendo un'impennata!")
        else:
            print("Questo tipo di motocicletta non è adatto per le impennate.")

    ## implemento il metodo astratto della classe padre Veicolo
    def mostra_informazioni(self):
        stringa = "Il veicolo è della marca " + self._marca + " e del modello: " + self._modello + ". Prodotto nell'anno " + str(self._anno) + " ed è attualmente " + self._accensione
        stringa += ", la moto è di tipo " + self._tipo
        return stringa




class ParcoVeicoli():
    def __init__(self, nome):
        self.nome = nome
        self._veicoli = []

    def get_veicoli(self):
        return self._veicoli
    
    def aggiungi(self, veicolo : Veicolo):
        self._veicoli.append(veicolo)

    def rimuovi(self, stringa):
        if stringa in self._veicoli: self._veicoli.remove(stringa)
    
    ## qui inizializzo una lista vuota per accogliere le descrizioni dei veicoli
    def get_veicoli(self):
        lista = []
        for veicolo in self._veicoli:
            lista.append(veicolo.mostra_informazioni())
        return lista
    
    def mostra_veicoli(self):
        lista = self.get_veicoli()
        for elemento in lista:
            print(elemento)
    
            


auto1 = Auto("Fiat", "Panda", 2000, 4)
print(auto1.mostra_informazioni())

furgone1 = Furgone("Fiat", "Ducato", 2000, 3000)
print(furgone1.mostra_informazioni())

motocicletta1 = Motocicletta("Fiat", "500 Scooter Elettrico", 2023, "Scooter")
print(motocicletta1.mostra_informazioni())

motocicletta2 = Motocicletta("Yamaha", "R1", 2020, "Sportiva")
motocicletta2.esegui_wheelie()
print(motocicletta2.mostra_informazioni())


print("Creo il mio parco veicoli")
parco1 = ParcoVeicoli("Giannodromo")
parco1.aggiungi(auto1)
parco1.aggiungi(furgone1)
parco1.aggiungi(motocicletta1)
parco1.aggiungi(motocicletta2)
parco1.mostra_veicoli()

print("Sto vendendo la mia Panda")
parco1.rimuovi(auto1)
parco1.mostra_veicoli()