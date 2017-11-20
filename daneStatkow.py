# -*- coding: utf-8 -*-
class DaneStatkow:
    short=[]
    name=[]
    points=[]
    cover=[]
    attack=[]
    
    def __init__(self):
        self.get_ship()
        # self.get_dziala()


    def get_ship(self):
        with open("dane_statkow.txt", "r") as f_in:
            self.lines = filter(None, (line.rstrip() for line in f_in))
        self.addTab()


    def addTab(self):
        for c in self.lines:
            self.short.append(c.split(" ")[0])
            self.name.append(c.split(" ")[1])
            self.points.append(c.split(" ")[2])
            self.cover.append(c.split(" ")[3])
            self.attack.append(c.split(" ")[4])


            
            
Ds=DaneStatkow()
Ds.addTab()
