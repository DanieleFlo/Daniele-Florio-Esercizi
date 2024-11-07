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
    def __init__(self, nome, eta, piatto=False, occupato=False):
        self._nome = nome
        self._eta = eta
        self._occupato = occupato
        self._piatto = piatto
    
    # metodo generico che può essere sovrascritto per specificare il tipo di lavoro svolto
    def lavora(self):
        pass
    
    def get_occupato(self):
        return self._occupato
    
    def get_nome(self):
        return self._nome
    
    def get_piatto(self):
        return self._piatto
    
    def set_piatto(self, piatto):
        self._piatto = piatto
    
    def set_occupato(self, occupato):
        self._occupato = occupato


class Chef(PersonaleCucina):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
        self._menu = []
        # Attributi aggiuntivi come specialità (tipo di cucina in cui è specializzato)
        self._tipo_cucina = ''
    
    def get_menu(self):
        return self._menu
    
    # dettaglia come lo chef crea nuovi piatti e menu
    def prepara_menu(self):
        print(f"Lo chef { self.get_nome()} ha preparato il menu!")
        self._menu = [
        {
            "nome": "pasta Alfredo",
            "ingredienti": ["fettuccine", "pancetta", "formaggio", "broccoli"]
        },
        {
            "nome": "carbonara cheese",
            "ingredienti": ["uova", "panna", "pasta"]
        },
        {
            "nome": "pizza Hawaii",
            "ingredienti": ["Ananas", "farina", "pancetta"]
        },]
        return self.get_menu()


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


"""
Crea una classe ristorante con una lista di liste chiamata menu e una 
lista chiamata ordinazione, Nel menu ci devono essere X piatti composti 
ogniuno da una lista propria di ingredienti, e la lista ordinazione invece e 
composta dalle singole ordinazioni del cleinte, Servirrà quindi una classe cliente e 
ogni membro della cucina potrà servire solo X piatti

Exstra:
- Aggiunggi personale
- Budget (random 10-100) e costi
- FeedBack
"""

class Cliente():
    _budget = 0
    _feedback = ''
    def __init__(self, nome):
        self._nome = nome
        
    def get_nome(self):
        return self._nome

class Ristorante():
    
    
    _ordinazioni =[]
    _clienti = []
    _chef = Chef('Luigi', 41)
    _sous_chef = SousChef('Mario', 35)
    _personale= [_chef,_sous_chef, CuocoLinea('Pippo', 21)]
    
    def __init__(self, nome):
          self._nome_ristorante = nome
          self._menu = self._chef.prepara_menu()
          
    def assegna_piatto(self):
        for i, persona in enumerate(self._personale):
            if persona.get_piatto() == False:
                if i<len(self._menu):
                    print(f'{persona.get_nome()} si è assegna il piatto: {self._menu[i]['nome']}')
                    persona.set_piatto(self._menu[i])
                    
                else: 
                    print('Piatti finiti!\n')
    
    def get_menu(self):
        print('\nEcco il menu:')
        for piatto in self._menu:
            print(f"Piatto: {piatto['nome']}")
            print(f"Ingredienti: {', '.join(piatto['ingredienti'])}")
        print()
        
    def get_client(self):
        if len(self._clienti):
            for cliente in self._clienti:
                print(f"{cliente.get_nome()}", end=', ')
            print()
        else:
            print('Nessun cliente!\n')
    
    def __input(self, tipo_input, opzioni, msg='', msg_error='Scelta non valida!'):
        while True:
            if isinstance(tipo_input, int):
                val = input(msg +': ')
                if val.isdigit():
                    new_val = int(val)
                    if opzioni==False or new_val in opzioni:
                        return new_val
                    else:
                        print(msg_error)
                else:
                    print(msg_error)
            elif isinstance(tipo_input, str):
                val = input(msg +': ')
                if val!= '':
                    if opzioni==False or val in opzioni:
                        return val
                    else:
                        print(msg_error)
                else:
                    print(msg_error)
            else:
                print('tipo di input non valido')
                break


    def start(self):
        self.assegna_piatto()
        while True:
            nav  = self.__input('', ['1','2'], 'Nuovo cliente: 1, Lista clienti: 2,  esci: 3')
            if nav == '1':
                nome_cliente = self.__input('', False, 'Nome cliente')
                self._clienti.append(Cliente(nome_cliente))
                self.gestione_cliente()
            elif nav == '2':
                self.get_client()
            elif nav == '3':
                break
    
    def __assegna_ordine(self, piatto):
        for persona in self._personale:
            if persona.get_occupato() == False and persona.get_piatto()['nome']==piatto:
                print(f'Lo chef {persona.get_nome()} cucina il piatto: {piatto}')
                persona.set_occupato(True)
            
    def gestione_cliente(self):
        while True:
            nav_cliente = self.__input('', ['1','2'], 'Chiedi menu: 1, ordina: 2')
            if nav_cliente == '1':
                self.get_menu()
            elif nav_cliente == '2':
                ordine = self.__input('', [piatto['nome'] for piatto in self._menu ], 'Qaule piatto vuoi ordinare?')
                self._ordinazioni.append(ordine)
                self.__assegna_ordine(ordine)
                break

ristorante = Ristorante('Da Luigi')

ristorante.start()