class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def mostra_informazioni(self):
        print(f"Veicolo marca {self.marca}, modello {self.modello}")


#Ereditarietà singola
class Quad(Veicolo):
    pass


quad = Quad('fiat', 'X1')

quad.mostra_informazioni()


# ----------------------------#


class DotazioniSpeciali:
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni

    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")
        
#Ereditarietà multipla
class AutomobileSportiva(Veicolo, DotazioniSpeciali):
    def __init__(self, marca, modello, dotazioni, cavalli):
        Veicolo.__init__(self, marca, modello)
        DotazioniSpeciali.__init__(self, dotazioni)
        self.cavalli = cavalli
        
    def mostra_informazioni(self):
        super().mostra_informazioni()
        print(f"Cavalli: {self.cavalli}")
        self.mostra_dotazioni()
        
auto_sportiva = AutomobileSportiva('Ferrari', 'Enzo', ['Alettone', 'Turbo'], 1000)
auto_sportiva.mostra_informazioni()