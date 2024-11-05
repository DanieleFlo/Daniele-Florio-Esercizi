#Esercizio ristorante parte 1

class Ristorante():
    aperto = False
    menu = {
        "Pizza Alfredo": 15,
        "Pizza Mario": 20,
        "Pizza Pepperoni": 25,
        "Pizza Hawaii": 25,
    }
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        
    def descrivi_ristorante(self):
        print(f"Benvenuto nel ristorante {self.nome}, qui offriamo cucina {self.tipo_cucina}.")
        
    def stato_apertura(self):
        print(f"Il ristorante è {"aperto" if self.aperto else "chiuso"}.")
        
    def apri_ristorante(self):
        self.aperto = True
        print(f"Il ristorante {self.nome} è ora aperto")
    
    def chiudi_ristorante(self):
        self.aperto = False
        print(f"Il ristorante {self.nome} è chiuso")
    
    def aggiungi_menu(self):
        print('\nAggiungi nuovo piatto al menu:')
        while True:
            nome = input('Nome del piatto: ')
            prezzo = input('Prezzo del piatto: ')
            if not prezzo.isdigit() or len(nome) == 0:
                print('Prezzo non valido o nome vuoto.')
            else:
                break
        self.menu[nome] = int(prezzo)
    
    def toggli_menu(self):
        print('\nTogli un piatto dal menu:')
        while True:
            nome = input('Nome del piatto: ')
            if len(nome) == 0 or nome not in list(self.menu.keys()):
                print('Nome non valido o non esiste.')
            else:
                del self.menu[nome]
                break
        print('\nMenu aggiornato:')
        self.stampa_menu()
        
    def stampa_menu(self):
        for el in self.menu:
            print(f'{el}; prezzo: {self.menu[el]}')
            
            
ristorante = Ristorante('Da Mario', 'Italiana')

ristorante.descrivi_ristorante()
ristorante.stato_apertura()
ristorante.apri_ristorante()
ristorante.stato_apertura()
ristorante.chiudi_ristorante()
ristorante.stato_apertura()
ristorante.aggiungi_menu()
ristorante.toggli_menu()
ristorante.stampa_menu()