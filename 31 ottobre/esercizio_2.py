# Scrivete un programma che chiede una stringa all’utente e
# restituisce un dizionario rappresentante la "frequenza di
# comparsa" di ciascun carattere componente la stringa.
# Esempio:
# Stringa "ababcc",
# Risultato
# {"a": 2, "b": 2, "c": 2}


stringa = input("Dammi una stringa: ")

uniq_char = set(stringa)
dizionario = {}
for c in  uniq_char:
    dizionario[c] = stringa.count(c)

print(dizionario)

dizionario = {}
for c in  stringa:
    dizionario[c] = stringa.count(c)

print(dizionario)