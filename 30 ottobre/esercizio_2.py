#Esercizio 1
# import random

# gen_n = random.randint(1, 100)
# print(gen_n)

# #Funzione che valuta se hai indovinato il numero casuale
# def valuta(n):
#     if n <1 or n > 100: #Se il numero inserito non è nel renge voluto
#         return {
#             "status": False,
#             "msg":'Il numero deve essere compreso tra 1 e 100'
#             }
#     elif n==gen_n: # Hai indovinato
#         return {
#                 "status": True,
#                 "msg":'Hai indovinato bravo!'
#             }
#     elif n < gen_n:
#         return {
#                 "status": False,
#                 "msg":'Il numero da indovinare è più grande'
#             }
#     elif n > gen_n:
#         return {
#                 "status": False,
#                 "msg":'Il numero da indovinare è più piccolo'
#             }
#     else:
#         return {
#                 "status": False,
#                 "msg":'Problema nel codice'
#             }


# while True:
#     n = int(input('Tenta la fortuna: '))
#     risultato = valuta(n) # ottiene il risultato
#     print(risultato["msg"]) # Stampa il messaggio
#     if risultato['status']==True: # Se indovini termina il programma
#         break

#Esercizio 2

def req_number():
    return int(input('Dammi un numero: '))

def F(i):
    if i == 1:
        return 1
    elif i == 2:
        return 1
    else:
        return F(i-1)+F(i-2)

N = req_number()
for i in range(1, N+1, 1):
    print(F(i))

