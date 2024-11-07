# Esercizio cucina
"""
creare una classe base PersonaleCucina e diverse classi derivate che rappresentano 
differenti ruoli all'interno della cucina di un ristorante. L'obiettivo è di utilizzare 
l'ereditarietà per condividere alcune caratteristiche comuni mentre si distinguono le 
responsabilità e le azioni specifiche di ogni ruolo.

Classe PersonaleCucina:
Attributi:
nome (stringa)
età (intero)
Metodi:
lavora() (metodo generico che può essere sovrascritto per specificare il tipo di lavoro svolto)
Classi Derivate:
Chef:
Attributi aggiuntivi come specialità (tipo di cucina in cui è specializzato)
Metodi come prepara_menu() che dettaglia come lo chef crea nuovi piatti e menu
SousChef:
Metodi come gestisci_inventario() per gestire l'inventario della cucina e assistere lo chef
CuocoLinea:
Metodi come cucina_piatto(nome_piatto) che specifica la preparazione di un piatto specifico nella linea di produzione
"""

class PersonaleCucina():
    _lista_ingredienti = []
    def __init__(self, nome, eta):
        self._nome = nome
        self._eta = eta
    
    # metodo generico che può essere sovrascritto per specificare il tipo di lavoro svolto
    def lavora(self):
        pass


class Chef(PersonaleCucina):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
        
        # Attributi aggiuntivi come specialità (tipo di cucina in cui è specializzato)
        self._tipo_cucina = ''
    
    def set_tipo_cucina(self, tipo_cucina):
        self._tipo_cucina = tipo_cucina
        
    def get_tipo_cucina(self):
        return self._tipo_cucina
    
    # dettaglia come lo chef crea nuovi piatti e menu
    def prepara_menu(self):
        pass


class SousChef(PersonaleCucina):
    __inventario = {}
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
        
    def set_inventario(self, inventario):
        self.__inventario.update( inventario )
        
    def get_inventario(self):
        return self.__inventario
        
    # gestire l'inventario della cucina e assistere lo chef
    def gestisci_inventario(self):
        pass


class CuocoLinea(PersonaleCucina):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
    
    # specifica la preparazione di un piatto specifico nella linea di produzione
    def cucina_paitto(self, nome_piatto):
        pass
    

class Gestione():
    def __init__(self):
        pass
    
    def __input(self, tipo_input, msg='', msg_error=''):
        while True:
            if isinstance(tipo_input, int):
                val = input(msg +': ')
                if val.isdigit():
                    return int(val)
                else:
                    print(msg_error)
            elif isinstance(tipo_input,  str):
                val = input(msg +': ')
                if val!= '':
                    return val
                else:
                    print(msg_error)
            else:
                print('tipo di input non valido')
                break
            
    
    def start(self):
        while True:
            pass