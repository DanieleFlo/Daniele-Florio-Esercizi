# def es_decoratore(fn):
#     def wrapper(*args, **kwargs):
#         print('prima')
#         r = fn(*args, **kwargs)
#         print('Dopo', r)
#         return r
#     return wrapper

# @es_decoratore
# def somma(a,b):
#     return a+b
    

# print(somma(1,2))

#Esercizio 1
# results = []

# def save_results(fn):
#     def wrapper(*args, **kwargs):
#         r = fn(*args, **kwargs)
#         print(f'Save ok. Info: len: {len(results)}, val: {r}')
#         results.append(r)
#         return r
#     return wrapper



# @save_results
# def area_triangolo(b,h):
#     return b*h/2.

# @save_results
# def area_quadrato(l):
#     return l*l

# @save_results
# def area_rettangolo(b,h):
#     return b*h

# area_rettangolo(2,3)
# area_triangolo(3,3)
# area_quadrato(5)

# print('Lista: ', results)


#Esercizio 2
# @save_results
# def primo(n):
#     divisore = False
#     for i in range(2, n):
#         if n % i == 0:
#             divisore = True
#             break
#     return not divisore, n

# while True:
#     n  = int(input('Dammi un numero: '))
#     r, _ = primo(n)
#     if r:
#         break
    
#Esercizio 3
def filter(fn):
    def wrapper(*args, **kwargs):
        a, b, cond = fn(*args, **kwargs)
        if cond:
            return a
        else: 
            return b
    return wrapper

def stamp(fn):
    def wrapper(*args, **kwargs):
        r = fn(*args, **kwargs)
        print(r)
        return r
    return wrapper

def input_string(fn):
    def wrapper(*args, **kwargs):
        s = input('Dammi un stringa: ')
        r = fn(s, *args, **kwargs)
        return r
    return wrapper

@input_string
@stamp
@filter
def comprimi_stringa(s):
    res = ''
    cont = 1
    comp = False
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:  
            cont += 1
            comp = True
        else:
            res += s[i - 1] + str(cont)
            cont = 1  
    res += s[-1] + str(cont)

    return s, res, not comp
        


comprimi_stringa()