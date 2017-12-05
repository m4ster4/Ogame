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
            temp = int(c.split()[1])
            print temp
            while temp >= 1:
                print "IN", temp
                self.statki.append(Statek(c.split()[0]))
                self.ilosc.append(int(c.split()[1]))
                temp-=1
            self.statki.append(Statek(c.split()[0]))
            self.ilosc.append(int(c.split()[1]))
        print len(self.statki)



    def delete_hit(self,flota):
        for k in range(len(flota.statki)):
            if Statek.isDestroyed(flota.statki(k)) is True:
                flota.ilosc[k]=0

    def check_opponent(self, flota):
        # print len(flota.statki),"statki kurde"
        opponent = random.randint(0, (len(flota.statki)-1))
        if int(flota.ilosc[opponent]) != 0:
            # print flota.statki[opponent]
            return flota.statki[opponent]
        else:
            return self.check_opponent(flota)

    def random_target(self, flota, opponent =0, x=0 ):
        while x < len(self.statki)-1:
            ilosc_statki_moje = self.ilosc[x]
            if ilosc_statki_moje !=0:
                while ilosc_statki_moje > 0:
                    ilosc_statki_moje -=1

                    opponent = self.check_opponent(flota)
                    shot = self.statki[x].shoot(opponent)
                    if shot is True:
                        temp = self.statki[0].fast_guns(self.skrot[x],flota.skrot[flota.statki.index(opponent)])
                        temp = 1 - (1/temp)
                        los = random.random()
                        if los < temp:
                            opponent = self.check_opponent(flota)
                            x+=1
                            self.random_target(flota,opponent,x)
            x+=1

    def status(self):
        return self.statki
    

F1=Flota("flota_1.txt")
F2=Flota("flota_2.txt")
F1.random_target(F2)

# F2.random_target("flota_1.txt")

