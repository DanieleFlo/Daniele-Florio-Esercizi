#Esecizio 2

num_primi = [] #Lista dei nuemeri primi da trovare

while len(num_primi)<5: #Esegue il le operazioni fin quando non abbiamo trovato 5 numeri primi
    divisibile = False
    num = int(input('Dammi un numero: '))
    if num >1:
        for i in range(2, num): #Verifica che il numero inserito non sia divisibile per altri numeri, parte da 2
            if num % i == 0:
                divisibile = True # Se trova un divisore esce
                break
    else:
        divisibile = True # Se il numero è negativo non va considerato
        
    if divisibile:
        print('Il numero non è primo')
    else:
        num_primi.append(num) #Appende alla lista il numero primo trovato
        print('Il numero è primo')
        print(f'Numeri trovati: {num_primi}')