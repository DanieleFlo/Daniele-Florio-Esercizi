# Esercizio teatro

class Posto():
    def __init__(self, numero, fila, occupato):
        self._numero = numero
        self._fila = fila
        self._occupato = occupato
    
    #Prenota il posto se occupato
    def prenota(self):
        self._occupato = True
            
    # Libera il posto se occupato
    def libera(self):
        self._occupato = False
    
    # Indica se il posto è occupato
    def get_fila(self):
        return self._fila
    
    def get_numero(self):
        return self._numero
    
    def get_occupato(self):
        return self._occupato
    

class PostoVIP(Posto):
    lista_servizi_extra = ['Accesso lounge', 'Servizio al posto']
    def __init__(self, numero, fila, occupato, vip):
        Posto.__init__(self, numero, fila, occupato)
        self.vip = vip

    # accesso a loufe, servizio in posto
    def servizi_extra(self):
        return ','.join(self.lista_servizi_extra)
    
    # Include gestione servizi
    def prenota(self):
        super().prenota()
        print("Prenotazione posto VIP avvenuta con successo!")
        print(f"Hai diritto hai seguenti servizi {self.servizi_extra()}")
    

class PostoStandard(Posto):
    def __init__(self, numero, fila, occupato, vip):
        Posto.__init__(self, numero, fila, occupato)
        self.vip = vip
        
    # costi in più per la prenotazione online o servizi meno esclusivi
    def prenota(self):
        super().prenota()
        print("Prenotazione posto standard avvenuta con successo! Non hai sevizi extra.")

class Teatro():
    __posti_riga = 2
    __min_char = 97
    __posti_colonna = list(map(chr, range(__min_char, __min_char+2)))
    
    def __init__(self):
        self._posti = [ [PostoStandard(i, char.upper(), False, False) if n<(len(self.__posti_colonna)//2) else PostoVIP(i, char.upper(), False, True) for i in range(self.__posti_riga)] for n, char in enumerate(self.__posti_colonna) ]
    
    # Controlla se ci sono posti liberi
    def  __controll_posti(fn):
        def wrapper(self, *args, **kwargs):
            full = True
            for riga in self._posti:
                for posto in riga:
                    if not posto.get_occupato():
                        full = False
            if full:
                print("Tutti i posti sono occupati!")
            else:
                return fn(self, *args, **kwargs)
        return wrapper
        
    # Trova e prenota un posto specifico
    @__controll_posti
    def prenota_posto(self):
        while True:
            numero = int(input("Inserisci il numero del posto: "))
            fila = input("Inserisci la fila del posto: ").upper()
            trovato = False
            for riga in self._posti:
                for posto in riga:
                    if posto.get_numero() == numero and posto.get_fila() == fila:
                        trovato = True
                        if not posto.get_occupato():
                            posto.prenota()
                        else:
                            print("Posto occupato!")
            if not trovato:
                print("Posto non trovato!")
            nav = input("Vuoi prenotare un altro posto? (y/n): ")
            if nav!= "y" and nav!="yes":
                break
        self.stampa_posti_occupati()
                
    
    # Stampa la lista dei posti occupati
    def stampa_posti_occupati(self):
        posti_occupati = 0
        for riga in self._posti:
            temp = False
            for posto in riga:
                if posto.get_occupato():
                    temp = True
                    posti_occupati +=1
                    print(f"{posto.get_numero()} - {posto.get_fila()} - { "Occ." if posto.get_occupato() else "Lib."} - { "Vip" if posto.vip else "Sta"}", end="; ")
            if temp:
                print()
        print(f"Posti Occupati: {posti_occupati}")

    def stampa_posti(self):
        print("Ecco tutti i posti del teatro")
        for riga in self._posti:
            for posto in riga:
                print(f"{posto.get_numero()} - {posto.get_fila()} - { "Occ." if posto.get_occupato() else "Lib."} - { "Vip" if posto.vip else "Sta"}", end="; ")
            print()
    

teatro = Teatro()

teatro.stampa_posti()
teatro.stampa_posti_occupati()
teatro.prenota_posto()