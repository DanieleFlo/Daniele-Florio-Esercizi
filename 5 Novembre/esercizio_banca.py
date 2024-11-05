#Esercizio sulla gestione di un conto bancario

class ContoBancario():
    __titolare = ''
    __saldo = 0
    __pin = '1234'
    
    # Controllo che il conto bancario sia intestato a qualcuno
    def __control_titolare(fn):
        def wrapper(self, *args, **kwargs):
            if len(self.__titolare)==0:
                print("Devi impostare un titolare prima di poter accedere al conto bancario!")
            else:
                return fn(self, *args, **kwargs)
        return wrapper

    # Deposita nel saldo
    @__control_titolare
    def deposita(self, importo):
        if importo>0:
            self.__saldo += importo
            print(f'Importo di {importo}€ depositato con successo. Saldo attuale: {self.__saldo}€')
    
    # Preleva dal saldo
    @__control_titolare
    def preleva(self, importo):
        if self.__saldo-importo>0:
            self.__saldo -= importo
            print(f'Importo di {importo}€ prelevato con successo. Saldo attuale: {self.__saldo}€')
        else:
            print('Saldo insufficiente!')
    
    # Restituisce il saldo del titolare
    @__control_titolare
    def visualizza_saldo(self):
        print(f'Saldo disponibile: {self.__saldo}€')
    
    # Setta il nome del titolare
    def set_titolare(self, titolare):
        if len(titolare)>0:
            self.__titolare = titolare
        else:
            print('Nome titolare non valido')
    
    # Restituisce il nome del titolare
    @__control_titolare
    def get_titolare(self):
        print(f'Nome titolare: {self.__titolare}.')
    
    # Metodo privato che valida il pin
    @__control_titolare
    def __control_pin(self, pin):
        if pin is self.__pin:
            return True
        else:
            return False
    
     # Metodo pubblico che controlla il pin del conto bancario
    @__control_titolare
    def valid_pin(self, pin):
        if self.__control_pin(pin):
            print('Accesso riuscito!')
        else:
            print('Accesso negato!')
    


conto = ContoBancario()
conto.get_titolare()
conto.set_titolare('Mario')
conto.get_titolare()
conto.visualizza_saldo()
conto.deposita(10)
conto.visualizza_saldo()
conto.preleva(30)
conto.preleva(5)

conto.valid_pin('123')
conto.valid_pin('1234')

#Verifico che non si possa utilizzare
print(conto._ContoBancario__control_pin('123'))

