from daneStatkow import *
import random
class Statek:
    """Klasa reprezentujaca pojedyczny statek , zawierajaca wszystkie informacje o nim"""
    def __init__(self,param):
        self.idx = DaneStatkow.short.index(param)
        self.skrot=DaneStatkow.short[self.idx]
        self.nazwa=DaneStatkow.name[self.idx]
        self.p_s=int(DaneStatkow.points[self.idx])
        self.oslona=int(DaneStatkow.cover[self.idx])
        self.atak=int(DaneStatkow.attack[self.idx])

    
    def shoot(self,other_ship):
        """Metoda do oddawania strzalu w statek przeciwnika, zwraca True jesli trafilismy"""
        if self.atak < 0.01 * other_ship.oslona:
            return False
        else:
            self.hit(other_ship)
            return True
        

    def hit(self,other_ship):
        """Metoda obslugujaca trafienie,zerowanie oslony, odejmowanie punktow  trafionego statku, sprawdzanie wybuchu   """
        other_ship.p_s -= self.atak - other_ship.oslona
        if (other_ship.oslona - self.atak) < 0:
            other_ship.oslona = 0
        else:
            other_ship.oslona = other_ship.oslona - self.atak
        indx = DaneStatkow.short.index(other_ship.skrot)
        if other_ship.p_s < 0.7 * int(DaneStatkow.points[indx]):
            explosion = 1 - (float(other_ship.p_s)/float(DaneStatkow.points[indx]))
            losowanie = random.random()
            if losowanie < explosion:
                other_ship.p_s = 0

    def szybkie_dzialaa(self,my_ship,other_ship):
        """Metoda szybkie dziala ktora okresla szanse na oddanie kolejnego strzalu"""
        for i in xrange(len(DaneStatkow.szybkie_dziala)):
            try:
                place_number = DaneStatkow.szybkie_dziala[i].index(my_ship)
                line_number = i
            except Exception:
                pass
            try:
                place_number_other = DaneStatkow.szybkie_dziala[i].index(other_ship)
                line_number_other = i
            except Exception:
                pass
        return int(DaneStatkow.szybkie_dziala[line_number][line_number_other+1])

    def isDestroyed(statek):
        """Metoda sprawdzajaca czy statek jest zniszczony"""
        if statek.p_s > 0:
            return False
        else:
            return True

    def stats(self):
        """Metoda pomocnicza do wyswietlania informacji o statku"""
        return self.skrot,self.nazwa,self.p_s,self.oslona,self.atak

# Stat=Statek('mt')
# print Stat.stats()