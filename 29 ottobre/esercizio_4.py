"""
Esercizio su Python: Cicli e Condizioni
Punto 1: Utilizzo di if
Scrivi un sistema che prende in input un numero e stampa "Pari" 
se il numero è pari e "Dispari" se il numero è dispari.

Punto 2: Utilizzo di while e range
Scrivi un sistema che prende in input un numero intero positivo n e
stampa tutti i numeri da n a 0 (compreso), 
decrementando di 1.Deve potersi ripete all’infinito

Punto 3: Utilizzo di for
Scrivi un sistema che prende in input una lista di numeri e 
stampa il quadrato di ciascun numero nella lista.

Punto 4: Utilizzo di if, while e for insieme Scrivi un sistema 
che prende in input una lista di numeri interi che precedente è 
stata valorizzata dall’utente.
Il sistema deve:
Utilizzare un ciclo for per trovare il numero massimo nella lista.
Utilizzare un ciclo while per contare quanti numeri sono presenti 
nella lista.
Utilizzare una condizione if per stampare "Lista Vuota" 
se la lista è vuota, altrimenti stampare il numero massimo 
trovato e il numero di elementi nella lista.
"""

#Punto 1
# n = int(input('Dammi un numero: '))
# if n%2 == 0: # Se il resto è zero vul dire che è pari
#     print('Il numero è pari')
# else:
#     print('Il numero è dispari')
    
#Punto 2
# while True:
#     n = int(input('Dammi un numero: '))
#     if n>=0: # Controllo che il numero sia positivo
#         for i in range(n, -1,-1): # Stampo il numero in modo decrescente
#             print(i)
#     else:
#         print('Il numero deve essere positivo')
#     nav = input('Vuoi continuare? (yes/no)')
#     if nav == 'no' or nav=='n': # Se l'utente scrive no esco
#         break

#Punto 3
# n_list = list(range(1,10, 1))
# for i in range(len(n_list)): # Scorro sulla lista è moltiplico ogni valore per sestesso
#     n_list[i] *=n_list[i]
# print(n_list)
    
#Punto 4
lista_mista = []
for i in range(5):
    val = input('Inserisci nella lista: ')
    lista_mista.append(val)

num = list(range(10))
for i in range(10):
    num[i] = str(num[i])

list_numb = []
list_str = []
for el in lista_mista:
    is_numero = False
    count = 0
    for char in el:
        if char in num:
            is_numero = True
            count += 1
    if count == len(el) and is_numero==True:
        list_numb.append(int(el))
    else:
        list_str.append(el)
print(list_numb)
print(list_str)

#Cerco il max
max = -10e-10
if len(list_numb)>0:
    for n in list_numb:
        if n > max:
            max = n
    print(max)

if len(list_str)>0:
    max_str = 0
    for n in list_str:
        if len(n)> max_str:
            max_str = len(n)
    print(max_str)

count = 0
while count >len(list_numb):
    count += 1
if count!=0:
    print(count)
else:
    print('La lista numb è vuota')
    
count_str = 0
while count_str >len(list_str):
    count_str += 1
if count_str!=0:
    print(count_str)
else:
    print('La lista str è vuota')