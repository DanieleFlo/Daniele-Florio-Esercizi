# Gestione file

# r -> read (da errore se il file non esiste)
# x -> crea solo il file
# w -> scrive solo il file
# a -> aggiunge all'ultima riga del file

"""
with open("./11 Novembre/prova.txt", 'w') as f: 
    f.write('esempio di file \nciao')

with open("./11 Novembre/prova.txt", 'r') as f: 
    contenuto = f.read() #f.readlines()

print(contenuto)
"""

with open("./11 Novembre/tabella.csv", 'r') as f:
    print(type(f))
    for i, line in enumerate(f):
        if i == 0: continue
        print(i, end=' - ')
        for j, var in enumerate(line.strip().split(',')):
            print(var, end='; ')
        print()
    # righe = f.read()
    # print(righe)
    
