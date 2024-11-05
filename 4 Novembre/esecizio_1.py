class Punto():
    origine = 0,0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def muovi_punto(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def distanza_da_origine(self):
        ox, oy = self.origine
        print(f"Distanza da origine in x,y: {self.x-ox}, {self.y-oy}")
        

punto1 = Punto(1,1)

punto1.muovi_punto(3,-4)

punto1.distanza_da_origine()




