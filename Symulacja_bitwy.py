from Flota import Flota

class Symulacja():
    def __init__(self):
        for i in range(6):
            F1 = Flota("flota_1.txt")
            F2 = Flota("flota_2.txt")
            F1.random_target(F2)
            F2.random_target(F1)
            print F1.status()
            print F2.status()
            # F1.delete_hit(F2)
            # F2.delete_hit(F1)



S=Symulacja()

