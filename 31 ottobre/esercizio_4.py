# def fn(*args, **kwargs):
#     print(args)
#     print(kwargs)
    
    
# fn(10, b=12)


# lista = [1, 2, 3, 4, 5, 6]

# lista2 = list(map(lambda x: x**2, lista))

# filtrata = list(filter(lambda x: x%2==0, lista))
# # lista2 = map(lista%2==0, lista)

# print(list(lista2))
# print(filtrata)


#Esercizio sulle frasi palindrome...
frasi_test = ["I topi non avevano nipoti!",
              "Ai rimpianti rimediamo Maria",
              "Ciao"]

def is_char(c):
    return c.isalpha()

def is_palindrome(s):
    s = s.lower()
    s = list(filter(is_char, s))
    s = ''.join(s)
    print(f"Frase filtrata -> {s}")
    return s == s[::-1]

for frase in frasi_test:
    print(f"Pal.: {is_palindrome(frase)}; Frase: {frase}\n")