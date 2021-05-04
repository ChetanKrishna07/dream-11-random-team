# -*- coding: utf-8 -*-
"""
Created on Tue May  4 16:12:30 2021

@author: cheta
"""
import random
class Player:
    name = ''
    points = 0
    typ = 0
    
    def __init__(self, N, p, t):
        self.name = N
        self.points = p
        self.typ = t
        
    def __str__(self):
        return self.name + " " + self.getType() + " " + str(self.points)
    
    def getName(self):
        return self.name
    
    def getPoints(self):
        return self.points
    
    def getType(self):
        
        if self.typ == 1:
            return "wk"
        if self.typ == 2:
            return "bat"
        if self.typ == 3:
            return "ar"
        if self.typ == 4:
            return "bowl"
        else:
            return "err"
        
class Team:
    
    players = []
    wk = 0
    bat = 0
    ar = 0
    bowl = 0
    mwk = 0
    mbat = 0
    mar = 0
    mbowl = 0
    
    def inTeam(self, p) :
        return p in self.players
    
    def generateTeam(self, players):
        
        players_list = [i for i in players]
        
        tot = 11
        i = 0
        
        
        while(i < tot):
            
            index = random.randint(0, len(players_list) - 1)
            
            # print(index)
            # print(players_list[index])
            # print()
            # self.showTeam()
            
            if not self.inTeam(players_list[index]):
                
                if players_list[index].getType() == "wk" :
                    if self.wk > 4:
                        continue
                    elif (11 - (i + self.mbat + self.mar + self.mbowl) < self.mwk) :
                        continue
                    else:
                        if self.mwk > 0:
                            self.mwk -= 1
                        self.players.append(players_list[index])
                        players_list.pop(index)
                        i += 1
                        self.wk += 1
                        
                elif players_list[index].getType() == "bat" :
                    if self.bat > 4:
                        continue
                    elif (11 - (i + self.mwk + self.mar + self.mbowl) < self.mbat) :
                        continue
                    else:
                        if self.mbat > 0:
                            self.mbat -= 1
                        self.players.append(players_list[index])
                        players_list.pop(index)
                        i += 1
                        self.bat += 1
                
                elif players_list[index].getType() == "ar" :
                    if self.ar > 4:
                        continue
                    elif (11 - (i + self.mbat + self.mwk + self.mbowl) < self.mar) :
                        continue
                    else:
                        if self.mar > 0:
                            self.mar -= 1
                        self.players.append(players_list[index])
                        players_list.pop(index)
                        i += 1
                        self.ar += 1
                        
                elif players_list[index].getType() == "bowl" :
                    if self.bowl > 4:
                        continue
                    elif (11 - (i + self.mbat + self.mar + self.mwk) < self.mbowl) :
                        continue
                    else:
                        if self.mbowl > 0:
                            self.mbowl -= 1
                        self.players.append(players_list[index])
                        players_list.pop(index)
                        i += 1
                        self.bowl += 1
            else:
                continue
            

    def __init__(self, player_list):
        
        self.mwk = 1
        self.mbat = 3
        self.mar = 1
        self.mbowl = 3
        self.wk = 0
        self.bat = 0
        self.ar = 0
        self.bowl = 0
        players = []
        
        self.generateTeam(player_list)
    
    def showTeam(self):
        
        l = len(self.players)
        
        
        print("Wicket-Keepers: ")

        for i in range(l) :
            if self.players[i].getType() == "wk":
                print(self.players[i].getName())
        
        print("Batsmen: ")
        for i in range(l) :
            if self.players[i].getType() == "bat":
                print(self.players[i].getName())
        
        print("All-Rounders: ")
        for i in range(l) :
            if self.players[i].getType() == "ar":
                print(self.players[i].getName())
                
        print("Bowlers: ")
        for i in range(l):
            if self.players[i].getType() == "bowl":
                print(self.players[i].getName())
        

#Data        
players = [Player("Naitram", 10, 1), Player("J Peter", 9, 1), Player("G Prospere", 8, 1), Player("Thomas", 9, 2), Player("Auguste", 8, 2), Player("T Gabriel", 8, 2), Player("Pamphile", 9, 2), Player("Sookwa", 9, 3), Player("Price", 10, 3), Player("A Prospere", 9, 3), Player("Edward", 9, 3), Player("Mann", 8, 3), Player("John", 9, 4), Player("Hippolyte", 9, 4), Player("Arnold", 8, 4), Player("Williams", 8, 4), Player("Joseph", 8, 4), Player("Hayle", 8, 4)]

for i in range(5):
    team = Team(players)
    print("Team ", i, ":", sep='')
    team.showTeam()
    
            
            
            
            
            
