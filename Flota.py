from Statek import Statek
import random
class Flota():
    def __init__(self, file):
        with open(file) as f_in:
            self.lines = filter(None, (line.rstrip() for line in f_in))
        self.statki = []
        self.ilosc = []
        self.skrot = []
        for c in self.lines[1:]:
           self.statki.append(Statek(c.split()[0]))
           # print c.split(" ")[0]
           self.ilosc.append(int(c.split()[1]))
        print self.statki, self.ilosc




    
        
    
    def delete_hit(self):
        pass

    def check_opponent(self, flota):
        opponent = random.randint(0, (len(flota.statki)-1))
        print opponent, flota.statki[opponent]

        if int(flota.ilosc[opponent]) != 0:
            return flota.statki[opponent]
        else:
            return self.check_opponent(flota)

    def random_target(self, flota, przeciwnik =0):
        flota = Flota(flota)

        opponent = self.check_opponent(flota)

        for x in xrange(0, len(self.statki)-1):
            if self.ilosc[x] !=0:
                self.ilosc[x] -=1
                opponent = self.check_opponent(flota)
                shot = self.statki[x].shot(opponent)
                if shot is True:
                    opponent = self.random_target(flota)


    def status(self):
        return self.statki
    

F1=Flota("flota_1.txt")
F1.random_target("flota_2.txt")

