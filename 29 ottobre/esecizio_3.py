#Esercizio a scelta dalla lista di 3, scelto il terzo
n1 = int(input('Dammi il primo numero: '))
n2 = int(input('Dammi il secondo numero: '))

temp_1 = [] # Lista temporanea dei divisori primo numero
for i in range(1,n1):
    if n1%i==0:
        temp_1.append(i)

temp_2 = []   # Lista temporanea dei divisori secondo numero
for i in range(1,n2):
    if n1%i==0:
        temp_2.append(i)

div_1 = set(temp_1) #Traforma la lista in set
div_2 = set(temp_2) #Traforma la lista in set
intersezione = list(div_1 & div_2) # Calcola intersezione

print('Fattori comuni:', intersezione)
if len(intersezione)==1:
    print('I numeri sono comprimi')
    
    

s1 = input('\nDammi la stringa 1: ')
s2 = input('Dammi la stringa 2: ')

set_1 = set(s1) #Traforma la stringa in set
set_2 = set(s2) #Traforma la stringa in set
op = list(set_1 & set_2) # Calcola intersezione
if len(op)==len(set_1) or len(op)==len(set_2):
    print('Sono complanari')
else:
    print('Non Sono complanari')