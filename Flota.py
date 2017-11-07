class Flota():
    def __init__(self,file):
        with open(file) as f_in:
            self.lines = filter(None, (line.rstrip() for line in f_in))
        self.statki = []
        self.ilosc = []
        self.skrot = []
        for c in self.lines[1:]:
           self.skrot.append(c.split(" ")[0])
           self.ilosc.append(c.split(" ")[1])
        print self.skrot, self.ilosc




    
        
    
    def usun_trafione(self):
        pass
    
    def losuj_cel(self):
        pass
    

F1=Flota("flota_1.txt")

