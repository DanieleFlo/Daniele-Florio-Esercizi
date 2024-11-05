class Libro():
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        
    def stampa_info(self):
        print(f"Il libro '{self.titolo}' è stato scritto da '{self.autore}' e ha '{self.pagine}' pagine.")


# libro1 = Libro("Harry Potter e i Doni della Morte", "J. K. Rowling" , 704)
# libro1.stampa_info()