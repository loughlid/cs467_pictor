#!/usr/bin/env python
"""#####################################
   
    Haunted Dungeon Game

    Team Pictor
    Andrew Bagwell
    Jerry Hayes
    Daniel Loughlin

    OSU CS 467 Winter 2017
#####################################"""

from DMT.GameData import DataManager


class HauntedDungeon():


    def newGame(self):
        """ From Jerry's example """
        self.dm = DataManager()
        self.dm.loadNewGame()
        self.dep = self.dm.getDependencies()
        for self.i in self.dep['commands']:
            print(self.i['tuple'])
        return


    def loadGame(self):
        return

    
    def showMenu(self):
        self.choice = "" 
        while (self.choice != "1") and (self.choice != "2") and (self.choice != "3"):
            print "HAUNTED DUNGEON!!"
            print
            print "1) Start A New Game"
            print "2) Load A New Game"
            print "3) Exit"
            print
            self.choice = str(raw_input("Enter your choice> "))
        if self.choice == "1":
       	    self.newGame()
        if self.choice == "2":
            self.loadGame()
        if self.choice == "3":
            exit() 
        return


    def runit(self):
	self.showMenu()



""" MAIN """
if __name__ == "__main__":
    hd = HauntedDungeon()
    hd.runit()
