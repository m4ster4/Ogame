from daneStatkow import *
import random
class Statek:
    def __init__(self,param):
        idx = DaneStatkow.short.index(param)
        self.skrot=DaneStatkow.short[idx]
        self.nazwa=DaneStatkow.name[idx]
        self.p_s=DaneStatkow.points[idx]
        self.oslona=DaneStatkow.cover[idx]
        self.atak=DaneStatkow.attack[idx]

    
    def shoot(self,other_ship):
        ship = Statek(other_ship)
        if self.atak < 0.01 * ship.oslona:
            return ""
        else:
            return self.hit(other_ship)
        

    def hit(self,other_ship):
        other_ship.p_s-= self.atak-other_ship.oslona
        if (other_ship.oslona - self.atak)< 0:
            other_ship.oslona = 0
        else:
            other_ship.oslona = other_ship.oslona - self.atak
        indx = DaneStatkow.short.index(other_ship.skrot)
        if other_ship.p_s <0.7*int(DaneStatkow.points[indx]):
            wybuch = 1 - float((other_ship.p_s)/DaneStatkow.points[indx])
            losowanie = random.random()
            if losowanie < wybuch:
                other_ship.p_s = 0
    def szybkie_dziala(self,my_ship,other_ship):
        for i in xrange(len(DaneStatkow.szybkie_dziala)):
            pass

    def isDestroyed(self,statek):
        if statek.p_s > 0:
            return False
        else:
            return True

    def stats(self):
        return self.skrot,self.nazwa,self.p_s,self.oslona,self.atak

Stat=Statek('mt')
print Stat.stats()