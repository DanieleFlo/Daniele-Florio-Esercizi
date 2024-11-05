
"""
# Esecizio con if
eta = 611
patente = "si"
tasso_alcolico = "alto"

if eta<18:
    print('Non puoi guidare sei minorenne')
elif patente!= 'si':
    print('Non puoi guidare non hai la patente')
elif tasso_alcolico=='altro':
    print('Non puoi guidare sei ubriaco')
else:
    print('La persona può giudare')
    

#Operatore ternario
print('non puoi guidare' if eta<18 else 'Pui guidare')

#Due operatori ternari
print('non puoi guidare' if eta<18 else 'non hai la patente' if patente!='si' else 'Pui guidare')

lista = [1,2,3,4,5]

for num in lista:
    num = 2

print(lista) # La lista NON viene modificata
"""


# Chiedere all'utente una parola 
# e restituisce solo le vocali della parola e l'indice


parola = input('Inserisci una parola: ')

vocali = 'aeiou'

res = ''
for i, c in enumerate(parola):
    if c in vocali:
        res += c+str(i) + '\t'
print(res)