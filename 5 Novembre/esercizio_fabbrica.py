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
        Prodotto.__init__(nome, costo_produzione, prezzo_vendita)
        
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
        
        
class  Abbigliamento(Prodotto):
    __taglia = ''
    __materiale = ''
    _taglie = ['S','M','L']
    _materiali = ['lino', 'seta', 'velluto']
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        Prodotto.__init__(nome, costo_produzione, prezzo_vendita)
        
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


class Fabbrica():
    inventario = {}
    def aggiungi_prodotto(self, nome, costo_produzione, prezzo_vendita):
        prodotto = Prodotto(nome, costo_produzione, prezzo_vendita)
    
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
            print(f"Costo di produzione: {info['Costo di produzione']}")
            print(f"Prezzo vendita: {info['Prezzo vendita']} ")
            print(f"Profitto: {info['Profitto']} €")
            print(f"Quantità: {info['qty']}")
        print("---\n")
    
    
fabbrica = Fabbrica()

fabbrica.aggiungi_prodotto('pasta', 5, 10)
fabbrica.aggiungi_prodotto('pasta', 5, 10)
fabbrica.aggiungi_prodotto('maccaroni', 5, 10)
fabbrica.vendi_prodotto('pasta')
fabbrica.vendi_prodotto('maccaroni')
fabbrica.resi_prodotto('pasta')
