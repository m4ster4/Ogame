from Flota import Flota


def Symulacja():
    F1 = Flota("flota_1.txt")
    F2 = Flota("flota_2.txt")

    for i in xrange(6):
        if F2.ilosc.count(0) == len(F2.ilosc) or F1.ilosc.count(0) == len(F1.ilosc):
            break

        F2.random_target(F1)  # 2 na 1
        F1.random_target(F2)  # 1 na 2

        F1.delete_hit()
        F2.delete_hit()

        print "stan F1: "
        print F1.status()

        print "stan F2: "
        print F2.status()
    if F1.status()==F2.status():
        return 'Remis'
    elif F1.status() > F2.status():
        return 'F1'
    else:
        return 'F2'


# Symulacja()

