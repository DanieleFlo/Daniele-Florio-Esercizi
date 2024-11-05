from esercizio_2 import Libro

#Gestisce la biblioteca
class Biblioteca():
    libri =[]

    # Permette di aggiungere un nuovo libro
    def crea_libro(self, titolo, autore, pagine):
        libro = Libro(titolo, autore, pagine)
        self.libri.append(libro)
    
    # Permette di cercare un libro e di stamparlo
    def cerca_libro(self, titolo="", autore="",):
        libri_trovati = []
        for libro in self.libri:
            if (titolo in libro.titolo and titolo!='') or (autore in libro.autore and autore != ""):
                libri_trovati.append(libro)
        if len(libri_trovati)==0:
            print("Libro non trovato.\n")
        elif len(libri_trovati)==1:
            libri_trovati[0].stampa_info()
        else:
            print("Libri trovati:")
            for i, libro in enumerate(libri_trovati):
                print(f"{i}:", end=' ')
                libro.stampa_info()
            nav = int(input("Quale voi stampare: "))
            libri_trovati[nav].stampa_info()
            print()
    
    # Permette di stampare tutti i libri  
    def tutti_libri(self):
        for libro in self.libri:
            libro.stampa_info()
        print()
                
        
        
biblioteca = Biblioteca()

# Aggiungo dei libri
biblioteca.crea_libro("Harry Potter e i Doni della Morte", "J.K. Rowling", 704)
biblioteca.crea_libro("Harry Potter 0", "J.K. Rowling", 74)
biblioteca.crea_libro("Harry Potter 1", "J.K. Rowling", 4)

#Menu di gestione della biblioteca
while True:
    nav = input("Crea libro -> c\nCerca libro -> s\nStampa tutti i libri -> t\nEsci -> q\n-> ").lower()
    if nav=="q":
        break
    elif nav=="c":
        titolo = input("Titolo: ")
        autore = input("Autore: ")
        pagine = input("Pagine: ")
        biblioteca.crea_libro(titolo=titolo, autore=autore, pagine=pagine)
    elif nav=="s":
        titolo = input("Titolo: ")
        autore = input("Autore: ")
        biblioteca.cerca_libro(titolo=titolo, autore=autore)
    elif nav=="t":
        biblioteca.tutti_libri()
    else:
        print("Scelta non valida!")

