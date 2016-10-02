#CHARACTER CLASS
class Character(object):
    #constructor
    def __init__(self, name, vicPoints = 0, cheatMode = False):
        self.__name = name
        self.__vicPoints = vicPoints
        self.__cheatMode = cheatMode

    #Getters
    def getName(self):
       return self.__name

    def getVicPoints(self):
        x = self.__vicPoints
        return self.__vicPoints

    def addVicPoint(self):
        self.__vicPoints += 1

    def getCheatMode(self):
        return self.__cheatMode

    #setter
    def setCheatMode(self, cheatMode):
        if cheatMode == True:
            self.__cheatMode = True
        else:
            self.__cheadMode = False

    #toString
    def toString(self): 
        r = ""
        r+= "Name: " + str(self.__name)+ "\n"
        r+= "Victory Points: " + str(self.__vicPoints)+ "\n"
        return r


class Enemy(Character):
    temp = 0

