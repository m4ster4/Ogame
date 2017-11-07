# -*- coding: utf-8 -*-
class DaneStatkow:
    short=[]
    name=[]
    points=[]
    cover=[]
    attack=[]
    
    def __init__(self):
        with open("dane_statkow.txt", "r") as f_in:
            self.lines = filter(None, (line.rstrip() for line in f_in))
    
    
    def printuj(self):
        for c in self.lines:
            print c.split(" ")
#         L= self.lines[0].split(" ")
#         print L
            
    def addTab(self):
        for c in self.lines:
            self.short.append(c.split(" ")[0])
            self.name.append(c.split(" ")[1])
            self.points.append(c.split(" ")[2])
            self.cover.append(c.split(" ")[3])
            self.attack.append(c.split(" ")[4])
        print self.short
        print self.name
        print self.points
        print self.cover
        print self.attack
        
        
            
            
Ds=DaneStatkow()
Ds.addTab()