# Esercizio teatro

class Posto():
    _numero =0
    _fila = ''
    _occupato= False
    
    #Prenota il posto se occupato
    def prenota(self):
        pass
    
    # Libera il posto se occupato
    def libera(self):
        pass
    
    # Indica se il posto è occupato
    def  get_fila(self):
        pass
    
    pass

class PostoVIP(Posto):
    def __init__(self):
        super().__init__()
    
    # accesso a loufe, servizio in posto
    def servizi_extra(self):
        pass
    
    # Include gestione servizi
    def prenota(self):
        pass
    

class PostoStandard(Posto):
    
    # costi in più per la prenotazione online o servizi meno esclusivi
    def prenota(self):
        pass

class Teatro():
    _posti = 0
    
    # Trova e prenota un posto specifico
    def prenota_posto(self):
        pass
    
    # Stampa la lista dei posti occupati
    def stampa_posti_occupati(self):
        pass