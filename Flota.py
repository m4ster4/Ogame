class Flota():
    def __init__(self,otworz_flote):
        with open(otworz_flote) as f_in:
            self.lines = filter(None, (line.rstrip() for line in f_in))
        self.statki = []
        self.ilosc = []
        self.skrot = []
        for c in self.lines:
            print c
            

    
        
    
    def usun_trafione(self):
        pass
    
    def losuj_cel(self):
        pass
    

F1=Flota("flota_1.txt")

