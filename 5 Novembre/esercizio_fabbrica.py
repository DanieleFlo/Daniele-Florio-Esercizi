#Esercizio fabbrica

class Prodotto():
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
    
    def calcola_profitto(self):
        print(f"Il profitto su questo prodotto è di: {self.prezzo_vendita - self.costo_produzione} €")
        return self.prezzo_vendita - self.costo_produzione
        
    def show_info(self):
        return {
            'Nome': self.nome,
            'Costo di produzione': self.costo_produzione,
            'Prezzo vendita': self.prezzo_vendita,
            'Profitto': self.calcola_profitto(),
        }
        
class  Elettronica(Prodotto):
    __materiale = ''
    __garanzia = 0
    
    _materiali = ['ferro', 'legnome', 'plastica']
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        Prodotto.__init__(self, nome, costo_produzione, prezzo_vendita)
        
    def set_materiale(self, materiale):
        if materiale in self._materiali:
            self.__materiale = materiale
            self.get_materiale()
        else:
            print(f"Il materiale non è valido. Utilizzare uno dei seguenti: {', '.join(self._materiali)}")
    
    def get_materiale(self):
        print(f"Il materiale del prodotto {self.nome} è {self.__materiale}")
    
    def set_garanzia(self, garanzia):
        if garanzia>0 and garanzia<40:
            self.__garanzia = garanzia
            self.get_garanzia()
    
    def get_garanzia(self):
        print(f"La garanzia del prodotto {self.nome} è di {self.__garanzia} anni")
        
    def show_info(self):
        old_info = super().show_info()
        new_info = old_info.copy()
        new_info['materiale'] = self.__materiale
        new_info['garanzia'] = self.__garanzia
        return new_info
        
        
class  Abbigliamento(Prodotto):
    __taglia = ''
    __materiale = ''
    _taglie = ['S','M','L']
    _materiali = ['lino', 'seta', 'velluto']
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        Prodotto.__init__(self, nome, costo_produzione, prezzo_vendita)
        
    def set_taglia(self, taglia):
        if taglia in self._taglie:
            self.__taglia = taglia
            self.get_taglia()
        else:
            print(f"La taglia non è valida. Utilizzare una delle seguenti: {', '.join(self._taglie)}")
            
    def get_taglia(self):
        print(f"La taglia del prodotto {self.nome} è {self.__taglia}")
    
    def set_materiale(self, materiale):
        if materiale in self._materiali:
            self.__materiale = materiale
            self.get_materiale()
        else:
            print(f"Il materiale non è valido. Utilizzare uno dei seguenti: {', '.join(self._materiali)}")
    
    def get_materiale(self):
        print(f"Il materiale del prodotto {self.nome} è {self.__materiale}")
        
    def show_info(self):
        old_info = super().show_info()
        new_info = old_info.copy()
        new_info['materiale'] = self.__materiale
        new_info['taglia'] = self.__taglia
        return new_info


class Fabbrica():
    inventario = {}
    
    def aggiungi_prodotto(self, nome, costo_produzione, prezzo_vendita):
        nav = input("Scegli il tipo di prodotto: 1 elettronica, 2 abbiliamento: ")
        if nav == '1':
            prodotto = Elettronica(nome, costo_produzione, prezzo_vendita)
        elif nav == '2':
            prodotto = Abbigliamento(nome, costo_produzione, prezzo_vendita)
        
        if nome in self.inventario.keys():
            self.inventario[nome]['qty'] += 1
        else:
            self.inventario[nome] = prodotto.show_info()
            self.inventario[nome].setdefault('qty', 1)
        print(f"Il prodotto {nome} è stato aggiunto all'invetario")
            
        self.stampa_inventario()
    
    def vendi_prodotto(self, nome):
        if nome in self.inventario.keys():
            if self.inventario[nome]['qty'] >1:
                 self.inventario[nome]['qty'] -=1
            else:
                del self.inventario[nome]
            print(f"Un prodotto {nome} è stato rimosso dal nostro inventario.")
        else:
            print("Il prodotto non è presente nel nostro inventario.")
        self.stampa_inventario()
    
    def resi_prodotto(self, nome):
        if nome in self.inventario.keys():
            self.inventario[nome]['qty'] +=1
            print(f"Hai fatto il reso del prodotto: {nome}")
            self.stampa_inventario()
        else:
            print("Il prodotto non è presente nel nostro inventario.")
    
    def stampa_inventario(self):
        print("Inventario:")
        for prodotto, info in self.inventario.items():
            print(f"Nome: {prodotto}")
            print(f"Quantità: {info['qty']}")
            print(f"Costo di produzione: {info['Costo di produzione']}€ x {info['qty']} = {info['Costo di produzione']*info['qty']}€")
            print(f"Prezzo vendita: {info['Prezzo vendita']}€ x {info['qty']} = {info['Prezzo vendita']*info['qty']}€")
            print(f"Profitto: {info['Profitto']}€ x {info['qty']} = {info['Profitto']*info['qty']}€")
        print("---\n")
    
    
fabbrica = Fabbrica()

# fabbrica.aggiungi_prodotto('pasta', 5, 10)
# fabbrica.aggiungi_prodotto('pasta', 5, 10)
# fabbrica.aggiungi_prodotto('maccaroni', 5, 10)
# fabbrica.vendi_prodotto('pasta')
# fabbrica.vendi_prodotto('maccaroni')
# fabbrica.resi_prodotto('pasta')

# Test nuuove classi
elettronica = Elettronica('ventilatore', 10, 30)
elettronica.set_materiale('ferro')
elettronica.set_garanzia(2)
# elettronica.calcola_profitto()
# print("---")
maglia = Abbigliamento('Maglia', 4, 30)
maglia.set_taglia('M')
maglia.set_materiale('seta')
# maglia.calcola_profitto()
print("\n*******----------------*******\n")

# funzione polimorfica
prodotto_base = Prodotto("Cappello di Trump", 300, 0)
def polimorfica(fnp):
    print(f"Risultato funzione polimorfica")
    data = fnp.show_info()
    for key, info in data.items():
        print(f"{key}: {info}")
    print('')

# Test funzione polimorfica
polimorfica(prodotto_base)
polimorfica(elettronica)
polimorfica(maglia)