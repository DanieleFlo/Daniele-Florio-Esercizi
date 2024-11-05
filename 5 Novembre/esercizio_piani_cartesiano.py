#Esercizio 1, punto e piano cartesiano

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def muovi_punto(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def distanza_da_origine(self, origigne):
        ox, oy = origigne
        return ((self.x - ox)**2 + (self.y - oy)**2)**0.5
    
    def get_coordinate(self):
        return self.x, self.y


class PianoCartesiano():
    punti = []
    def __init__(self, x,y):
        self.origine = x,y
        
    def control(fn):
        def wrapper(self, *args, **kwargs):
            if len(self.punti)<2:
                print("Devi aggiungere almeno 2 punti.")
            else:
                return fn(self, *args, **kwargs)
        return wrapper
    
    def start(self):
        while len(self.punti)<2:
            x = input("Inserisci la coordinata x del punto: ")
            y = input("Inserisci la coordinata y del punto: ")
            if x.isdigit() and y.isdigit():
                x, y = float(x), float(y)
                punto = Punto(x, y)
                self.punti.append(punto)
                print(f"Il punto {punto.get_coordinate()} è stato aggiunto con successo.\n")
            else:
                print("Le coordinate devono essere numeri.")
    
    @control
    def stampa_piano(self):
        print(f"Stampo i punti del piano cartesiano, origine: {self.origine}")
        for punto in self.punti:
            x,y = punto.get_coordinate()
            print(f"(X: {x}, Y: {y})")
    
    @control 
    def distanza_punti(self):
        print("Ti mostro i punti del piano cartesiano")
        self.stampa_piano()
        p = int(input("Di quale punto vuoi la distanza (1,2): "))
        
        if p==1 or p==2:
            print(f"Distanza dall'origine: {self.punti[p-1].distanza_da_origine(self.origine)}\n")
            
        else:
            print("Il punto selezionato non esiste.")
    
    @control
    def muovi_punti(self):
        print("Ti mostro i punti del piano cartesiano")
        self.stampa_piano()
        p = int(input("Quale punto vuoi muovere? (1,2): "))
        if p==1 or p==2:
            dx = float(input("Sposta x di: "))
            dy = float(input("Sposta y di: "))
            self.punti[p-1].muovi_punto(dx,dy)
            print("Punto muovito con successo.\n")
            self.stampa_piano()
        else:
            print("Il punto selezionato non esiste.")
            

piano1 = PianoCartesiano(0,0)

piano1.stampa_piano()
piano1.start()
piano1.stampa_piano()
piano1.distanza_punti()
piano1.muovi_punti()