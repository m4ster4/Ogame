from Statek import Statek
import random
class Flota():
    opponents = []
    def __init__(self, file):
        with open(file) as f_in:
            self.lines = filter(None, (line.rstrip() for line in f_in))
        self.statki = []
        self.ilosc = []
        self.skrot = []

        for c in self.lines[1:]:
            temp = int(c.split()[1])
            if temp >= 1:
                while temp >= 1:
                    S1 = Statek(c.split()[0])
                    self.statki.append(S1)
                    self.skrot.append(c.split()[0])
                    self.ilosc.append(1)
                    temp-=1
            else:
                S1 = Statek(c.split()[0])
                self.statki.append(S1)
                self.skrot.append(c.split()[0])
                self.ilosc.append(temp)


        # print len(self.statki)



    def delete_hit(self):
        _ships = self.statki[:]
        for k in xrange(len(_ships)):
            if Statek.isDestroyed(_ships[k]) is True:
                self.ilosc[k] = 0

    def check_opponent(self, flota):
        if len(flota.statki) > 0:
            opponent = random.randint(0, (len(flota.statki)-1))
            # if opponent in flota.opponents:
            #     return False
            flota.opponents.append(opponent)

            if int(flota.ilosc[opponent]) != 0:
            # print flota.statki[opponent]
                return flota.statki[opponent]
            else:
                return self.check_opponent(flota)
        else:
            return False

    def random_target(self, flota, opponent =0, x=0 ):
        while x < len(self.statki)-1:
            if self.ilosc[x] != 0:
                opponent = self.check_opponent(flota)
                if opponent == False:
                    return self.random_target(flota,opponent,x+1)
                shot = self.statki[x].shoot(opponent)
                if shot is True:

                    temp = self.statki[0].szybkie_dzialaa(self.skrot[x],flota.skrot[flota.statki.index(opponent)])
                    temp = 1 - (1/temp)
                    los = random.random()
                    if los < temp:
                        opponent = self.check_opponent(flota)
                        x+=1
                        self.random_target(flota,opponent,x)
            x+=1

    def status(self):
        counter = 0
        for i in xrange(len(self.statki)):
            if self.ilosc[i] != 0:
                counter += 1
        return counter
    

# F1=Flota("flota_1.txt")
# F2=Flota("flota_2.txt")
# F1.random_target(F2)

# F2.random_target("flota_1.txt")

