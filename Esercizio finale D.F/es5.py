class Libro():
    def __init__(self, titolo, autore, anno):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        
    def stampa_info(self):
        print(f"Il libro '{self.titolo}' è stato scritto da '{self.autore}', pubblicato nell'anno: '{self.anno}'")



#Gestisce la biblioteca
class Biblioteca():
    libri =[]

    # Permette di aggiungere un nuovo libro
    def crea_libro(self, titolo, autore, anno):
        libro = Libro(titolo, autore, anno)
        self.libri.append(libro)
    
    # Permette di cercare un libro e di stamparlo
    def cerca_libro(self, titolo=""):
        libri_trovati = []
        for libro in self.libri:
            if titolo in libro.titolo and titolo!='':
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
    
    # Permette di stampare tutti i libri  
    def tutti_libri(self):
        for libro in self.libri:
            libro.stampa_info()
        print()
                
        
        
biblioteca = Biblioteca()

#Menu di gestione della biblioteca
while True:
    nav = input("Crea libro -> c\nCerca libro -> s\nStampa tutti i libri -> t\nEsci -> q\n-> ").lower()
    if nav=="q":
        break
    elif nav=="c":
        titolo = input("Titolo: ")
        autore = input("Autore: ")
        anno = input("Anno pubblicazione: ")
        biblioteca.crea_libro(titolo=titolo, autore=autore, anno=anno)
    elif nav=="s":
        titolo = input("Titolo: ")
        biblioteca.cerca_libro(titolo=titolo)
    elif nav=="t":
        biblioteca.tutti_libri()
    else:
        print("Scelta non valida!")
