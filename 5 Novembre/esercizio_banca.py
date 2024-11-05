#Esercizio sulla gestione di un conto bancario

class ContoBancario():
    __titolare = ''
    __saldo = 0
    
    def __control_titolare(fn):
        def wrapper(self, *args, **kwargs):
            if len(self.__titolare)==0:
                print("Devi impostare un titolare prima di poter accedere al conto bancario!")
            else:
                return fn(self, *args, **kwargs)
        return wrapper

    @__control_titolare
    def deposita(self, importo):
        if importo>0:
            self.__saldo += importo
            print(f'Importo di {importo}€ depositato con successo. Saldo attuale: {self.__saldo}€')
    
    @__control_titolare
    def preleva(self, importo):
        if self.__saldo-importo>0:
            self.__saldo -= importo
            print(f'Importo di {importo}€ prelevato con successo. Saldo attuale: {self.__saldo}€')
        else:
            print('Saldo insufficiente!')
    
    @__control_titolare
    def visualizza_saldo(self):
        print(f'Saldo disponibile: {self.__saldo}€')
    
    def set_titolare(self, titolare):
        if len(titolare)>0:
            self.__titolare = titolare
        else:
            print('Nome titolare non valido')
    
    @__control_titolare
    def get_titolare(self):
        print(f'Nome titolare: {self.__titolare}.')


conto = ContoBancario()
conto.get_titolare()
conto.set_titolare('Mario')
conto.get_titolare()
conto.visualizza_saldo()
conto.deposita(10)
conto.visualizza_saldo()
conto.preleva(30)
conto.preleva(5)
