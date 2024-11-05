#Self è un placeholder

# Init è il costruttore -> costruisce
# l'oggetto della classe automobile, 
# ogni classe lo ha per froza e coincide sempre col nome della classe


class Automobile:
    numero_di_ruote = 4 # Attributo di classe
    def __init__(self,  marca, modello): # Meto di costruttore
        self.marca = marca # Attributo di istanza
        self.modello = modello
    
    def stampa_info(self): # Metodo di istanza
        print(f"L'automobile è una {self.marca} {self.modello}, ruote: {self.numero_di_ruote}")
        
auto1 = Automobile('Fiat', 'panda') # Auto1 è il nostro self
auto2 = Automobile('BMW', 'x3') # <- Polimorfismo self ha un nome diverso

auto1.numero_di_ruote = 6
auto1.stampa_info()
auto2.stampa_info()

print(type(auto1))