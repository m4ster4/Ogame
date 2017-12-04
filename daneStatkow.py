# -*- coding: utf-8 -*-
class DaneStatkow:
    short=[]
    name=[]
    points=[]
    cover=[]
    attack=[]
    szybkie_dziala=[]
    
    def __init__(self):
        self.get_ship()
        # self.get_dziala()
        self.fast_guns()


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

    def fast_guns(self):
        with open("szybkie_dziala.txt", "r") as f_in:
            self.fast_lines = filter(None, (line.rstrip() for line in f_in))
            # print self.fast_lines
        for i in self.fast_lines[1:]:
            self.szybkie_dziala.append(i.split())
        # for el in self.szybkie_dziala:
        #     print el
        print self.szybkie_dziala

            
            
Ds=DaneStatkow()
Ds.addTab()
