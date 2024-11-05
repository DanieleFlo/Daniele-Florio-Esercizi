#Esecizio 1

while True:
    nav = input('Vuoi inserire un numero? (yes/no): ').lower() # Chiede se si vuole inserire un numero o uscire
    if nav == 'yes' or nav=='y':
        numero = int(input('Dammi un numero: ')) # Cheide il numero all'utente
        for i in range(numero+1): #Per stampare anche il numero iniziale parte dal numero +1
            print(numero-i) #Stampa i numeri al contrario rispetto all'ordine di esecuzione
    elif nav == 'no' or nav=='n': #Controlla che si sia inserita la condizione di uscita
        break
    else:
        print('Devi inseriri yes/y o no/n') #Messaggio di errore