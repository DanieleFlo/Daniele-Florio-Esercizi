numb = int(input('Dammi un int: '))
bl = bool(int(input('Dammi un bool: ')))
str = input('Dammi un string: ')

dict_prova = {
    'numero': numb,
    'buleano': bl,
    'stringa': str,
}

print(dict_prova)
# print(dict_prova.keys())
# print(dict_prova.values())
# print(dict_prova.items())

for chiave, valore in dict_prova.items():
    print(f'{chiave}: {valore}')