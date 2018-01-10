from appJar import gui
from Symulacja_bitwy import *

skroty = ["mt", "dt", "lm", "cm", "kr", "ow", "sk", "re", "ss", "b", "n", "gs", "p"]

def press(button):
    if button == "EXIT":
        app.stop()
    if button == "RUN":
        temp = Symulacja()
        app.setLabel("wynik","WINNER:" +str(temp))

    else:
        z = app.getAllEntries()
        flota_1 = open("flota_1.txt", "w")
        flota_2 = open("flota_2.txt", "w")
        flota_2.write('skrot ilosc')
        flota_2.write("\n")
        flota_1.write('skrot ilosc')
        flota_1.write("\n")
        temp1 , temp2 = 0,0

        for x in xrange(1,len(z)+1):
            if x%2==0:
                flota_2.write(skroty[temp1])
                flota_2.write(" ")
                a = int(z["" + str(x) + ""])
                flota_2.write(str(a))
                flota_2.write("\n")
                temp1 += 1
            else:
                flota_1.write(skroty[temp2])
                flota_1.write(" ")
                a = int(z["" + str(x) + ""])
                flota_1.write(str(a))
                flota_1.write("\n")
                temp2 += 1
        flota_1.close()
        flota_2.close()
        print "zapisano"


app = gui("OGAME SIMULATOR", "450x400")
app.setBg("#CCCCCC")
app.setFont(10)
app.addLabel("title_1", "FLOTA 1: ", 0,1)
app.addLabel("title_2", "FLOTA 2: ", 0, 3)
app.setLabelBg("title_1", "#777777")
app.setLabelBg("title_2", "#777777")

for i in xrange(len(skroty)):
    """generate label"""
    app.addLabel(skroty[i]+'_0',skroty[i],i+1)
    app.addLabel(skroty[i]+'_1', skroty[i], i + 1,2)

my_list1 = [i for i in range(1,28,2)]
my_list2 = [j for j in range(2,28,2)]

for i in xrange(len(skroty)):
    """generate entry"""
    app.addNumericEntry(str(my_list1[i]), i+1, 1)
    app.addNumericEntry(str(my_list2[i]), i+1, 3, 0)

app.addButtons(["SAVE"], press, 14,0)
app.addButtons(["RUN"],press,14,1)
app.addLabel("wynik", "WINNER... ",14,2)

app.addButtons(["EXIT"], press, 14, 3)
app.go()
