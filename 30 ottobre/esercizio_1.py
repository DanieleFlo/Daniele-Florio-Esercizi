"""
Descrizione: Scrivi un programma che chieda all'utente di inserire 
un numero intero positivo n. Il programma deve poi eseguire le 
seguenti operazioni:

Utilizzare un ciclo while per garantire che l'utente inserisca un 
numero positivo. Se l'utente inserisce un numero negativo o zero, 
il programma deve continuare a chiedere un numero fino a quando non 
viene inserito un numero positivo.
Utilizzare un ciclo for con range per calcolare e stampare la somma 
dei numeri pari da 1 a n.
Utilizzare un ciclo for per stampare tutti i numeri dispari da 1 a n.
Utilizzare una struttura if per determinare se n è un numero primo. 
Un numero primo è divisibile solo per 1 e per se stesso. 
Il programma deve stampare se n è primo o no.
"""

# Input numero utente
n = 0
while True:
    n = int(input('Dammi un numero maggiore di 0: '))
    if n > 0: # Controllo che il numero sia maggiore di 0
        break

# Sommo i numeri pari da 1 a n con n compreso (se è pari ovviamente)
sum = 0
for i in range(1, n+2, 2): # Conto a due a due fino a n+2 per considerare n stesso
    sum += i-1 #Dato che contro sui dispari per partire da 1, sottrago -1
    print(i-1)
print(f'Somma dei numeri pari: {sum}')

# Stampo i numeri dispari
for i in range(1, n+1, 2):
    print(i)

# Controllo se n è primo
divisori = False
for i in range(2, n, 1): # Controllo che il numero non abbia divisori
    if n % i == 0:
        divisori = True # Se trovo un divisore esco, di sicuro non è primo
        break

if divisori==False: # Se non ho trovato divisori è primo
    print(f'{n} è un numero primo')
else: #Viceversa
    print(f'{n} non è un numero primo')