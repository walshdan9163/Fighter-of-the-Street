

import random

response = True

usedSpaces = []
pTwoUsedSpaces = []

eventPlaces = [(0, 1),(2, 2),(5, 3),(4, 8),(9, 0),(4, 3),(1, 5),(0,6),(0,4),(0,12),(2,8),(3,6),(3,1),(1,0),(5,11),(11,6),(14,14),(15,12),(7,5),(3,14),(1,15),(14,1),(15,13),(9,8),(8,1),(8,6),(15,2)]

def event(cheatMode):
    import random
    x = random.randint(1,3)
    #ROCK PAPER SCISSORS
    if x == 1:
        choices = ["Rock", "Paper", "Scissors", "rock", "paper", "scissors"]
        print("You've been challenged to a game of 'Rock, Paper, Scissors!'")
        eChoice = choices[random.randint(0,2)]
        if cheatMode:
            print("The computer chose: " + eChoice)
        choice = "NONE"
        while choice not in choices:
            choice = input("Which do you choose?(rock, paper, or scissors)")
        
        if choice == "Rock" or choice == "rock" and eChoice == "Paper":
            print("You lose! I picked paper!")
            return False
        elif choice == "Paper" or choice == "paper" and eChoice == "Scissors":
            print("You lose! I picked Scissors!")
            return False
        elif choice == "Scissors" or choice == "scissors" and eChoice == "Rock":
            print("Haha! You lose, because I picked Rock!")
            return False
        elif choice == "Rock" or choice == "rock" and eChoice == "Scissors":
            print("You win! I picked Scissors! :(")
            return True
        elif choice == "Paper" or choice == "paper" and eChoice == "Rock":
            print("You win! I picked Rock! :(")
            return True
        elif choice == "Scissors" or choice == "scissors" and eChoice == "Paper":
            print("You win! I picked Paper! :(")
            return True
        elif choice == "Rock" or choice == "rock" and eChoice == "Rock":
            print("It's a tie! You got lucky, and your life is spared!")
            return False
        elif choice == "Paper" or choice == "paper" and eChoice == "Paper":
            print("It's a tie! You got lucky, and your life is spared!")
            return False
        elif choice == "Scissors" or choice == "scissors" and eChoice == "Scissors":
            print("It's a tie! You got lucky, and your life is spared!")
            return False
        else:
            print("not a valid response")
            
    #GUESSING NUMBER GAME
    elif x == 2:
        import random
        possibleGuesses = []
        for g in range(20):
            possibleGuesses.append(g+1)
        guesses = 0
        cNumber = random.randint(1, 20)
        print('I have chosen between 1 and 20.\nYou have six tries to guess my number.')
        #Gives answer if in cheatmode
        if cheatMode:
            print("The number is between "+str(cNumber-1)+" and " +str(cNumber+1))
        #Let player guess 6 times
        while guesses < 6:
            pGuess = "NONE"
            while pGuess not in possibleGuesses:
                try:
                    pGuess = int(input('Try to guess it!: '))
                except ValueError:
                    print("That is not a valid response.")
                    pGuess = "NONE"

            guesses = guesses + 1
            if pGuess < cNumber:
                print('My number is higher than that!') 

            if pGuess > cNumber:
                print('My number is lower than that!')

            if pGuess == cNumber:
                break

        if pGuess == cNumber:
            guessesTaken = str(guesses)
            print('Good job! You guessed my number in ' + guessesTaken + ' guesses!\n')
            return True

        if pGuess != cNumber:
            number = str(cNumber)
            print('Nope. The number I was thinking of was ' + number + "\n")
            return False
    #Dice
    elif x == 3:
        import random
        print("I challenge you to a game of Dice!")
        print("We will each roll 3 dice and we will compare our totals. The one with the highest total wins!")
        #Roll dice 3 times
        pTotal = 0
        eTotal = 0
        for i in range(3):
            pDice = random.randint(1,6)
            eDice = random.randint(1,6)
            roll = input("Press enter to roll.")
            print("\nYou rolled a " + str(pDice))
            print("I rolled a " + str(eDice))
            pTotal += pDice#Add to total
            eTotal += eDice

        #Compare totals
        if eTotal > pTotal:
            print("Haha! You lose! I rolled a "+str(eTotal)+" and you only rolled a " +str(pTotal)+"!")
            return False
        elif pTotal > eTotal:
            print("Ahh.. It seems that you have beaten me this time. You won't be so lucky the next.")
            return True
        else:
            print("We tied! This means that we must play again!")
            pTotal = 0
            eTotal = 0
            for i in range(3):
                pDice = random.randint(1,6)
                eDice = random.randint(1,6)
                roll = input("Press enter to roll.")
                print("\nYou rolled a " + str(pDice))
                print("I rolled a " + str(eDice))
                pTotal += pDice
                eTotal += eDice

        #Compare totals
            if eTotal > pTotal:
                print("Haha! You lose! I rolled a "+str(eTotal)+" and you only rolled a " +str(pTotal)+"!")
                return False
            elif pTotal > eTotal:
                print("Ahh.. It seems that you have beaten me this time. You won't be so lucky the next.")
                return True
            else:
                print("Well, we tied again! The odds of this are so slim that I'll just give you the win.")
            
            

#Check for events
def eventCheck(x, y, eventPlaces, cheatMode):
    eventSpots = eventPlaces
    if (x,y) not in eventSpots:
        print("There is nothing here!")
    else:
        result = event(cheatMode)
        return result

#Map Class
class Map(object):
    #Constructor
    def __init__(self, size, charSymbol = "[-U-]", startPos = (0,0), pTwoStartPos = (0,15)):
        self.charSymbol = charSymbol
        self.curX = startPos[0]
        self.curY = startPos[1]
        self.pTwoCurX = pTwoStartPos[0]
        self.pTwoCurY = pTwoStartPos[1]
        self.size = size
        self.curPos = startPos
        self.charTwoSymbol = "[-2-]"
        
        self.grid = [] 
        for x in range(self.size):
            self.grid.append([])

        for col in self.grid: 
            for x in range(self.size):
                col.append("[---]")

    #Get Player Position
    def getPos(self):
        return (self.curX, self.curY)

    def getSize(self):
        return self.size

    
    #Set Player
    def setPlayer(self, x = 0, y = 0):
        if self.isValid(x,y):
            curPos = self.grid[x][y]#change current position to (0,0)
            self.grid[x][y] = self.charSymbol#change (0,0) on the grid to the character symbol
        else:
            print("Invalid starting position")

    def setPlayerTwo(self, x = 0, y = 14):
        if self.isValid(x,y):
            self.grid[x][y] = self.charTwoSymbol
        else:
            print("Invalid starting position for player Two")

    #Display Map
    def display(self):
        print("\n")
        for x in range(self.size):
            for y in range(self.size):
                end = ''
                print(self.grid[x][y], end = "")
            print()
        print("\n")

    #Is Valid?
    def isValid(self, x, y):
        if x < 0 or y < 0 or x >= self.size and y >= self.size:
            return False
        elif self.grid[x][y] != "[---]":
            return False
        else:
            return True

    #Add Terrain        
    def addTerrain(self, x, y):
        if self.isValid(x,y) and (x,y) != self.curPos:
            self.grid[x][y] = ""
            self.grid[x][y] += "[-x-]"

    #Move To
    def moveTo(self, x, y):
        if self.isValid(x, y):
            self.grid[x][y] = self.charSymbol
            self.grid[self.curX][self.curY] = "[-/-]"
            usedSpaces.append((self.curX, self.curY))
            self.curX = x
            self.curY = y
            self.display()
        else:
            print("error in moveTo")
        
    def movePlayerTwo(self, x, y):
        if self.isValid(x, y):
            self.grid[x][y] = self.charTwoSymbol
            self.grid[self.pTwoCurX][self.pTwoCurY] = "[-/-]"
            pTwoUsedSpaces.append((self.pTwoCurX, self.pTwoCurY))
            self.pTwoCurX = x
            self.pTwoCurY = y
            self.display()

    #Move Direction
    def moveDir(self, direction):
        if direction in ["w", "a", "s", "d", "2", "4", "6", "8", "k", "event"]:
            if direction == "a" or direction == "4":
                x = self.curX
                y = self.curY - 1
                if(self.isValid(x, y)):
                    self.moveTo(x, y)
                    return [x,y]
                else:
                    print("invalid move")
                    return [0,0]
            elif direction == "s" or direction == "2":
                x = self.curX + 1
                y = self.curY
                if(self.isValid(x, y)):
                    self.moveTo(x, y)
                    return [x,y]
                else:
                    print("invalid move")
                    return [0,0]
            elif direction == "d" or direction == "6":
                x = self.curX
                y = self.curY + 1
                if(self.isValid(x, y)):
                    self.moveTo(x, y)
                    return [x,y]
                else:
                    print("invalid move")
                    return [0,0]
            elif direction == "w" or direction == "8":
                x = self.curX - 1
                y = self.curY 
                if(self.isValid(x, y)):
                    self.moveTo(x, y)
                    return [x,y]
                else:
                    print("invalid move")
                    return [0,0]
            elif direction == "k" or direction == "K":
                return [self.curX,self.curY]
            else:
                print("error")
        else:
            print("Not in list of possible moves")


    def playerTwoMoveDir(self, direction):
        if direction in ["w", "a", "s", "d", "2", "4", "6", "8", "k", "event"]:
            if direction == "a" or direction == "4":
                x = self.pTwoCurX
                y = self.pTwoCurY - 1
                if(self.isValid(x, y)):
                    self.movePlayerTwo(x, y)
                    return [x,y]
                else:
                    print("invalid move")
                    return [0,0]
            elif direction == "s" or direction == "2":
                x = self.pTwoCurX + 1
                y = self.pTwoCurY
                if(self.isValid(x, y)):
                    self.movePlayerTwo(x, y)
                    return [x,y]
                else:
                    print("invalid move")
                    return [0,0]
            elif direction == "d" or direction == "6":
                x = self.pTwoCurX
                y = self.pTwoCurY + 1
                if(self.isValid(x, y)):
                    self.movePlayerTwo(x, y)
                    return [x,y]
                else:
                    print("invalid move")
                    return [0,0]
            elif direction == "w" or direction == "8":
                x = self.pTwoCurX - 1
                y = self.pTwoCurY 
                if(self.isValid(x, y)):
                    self.movePlayerTwo(x, y)
                    return [x,y]
                else:
                    print("invalid move")
                    return [0,0]
            elif direction == "k" or direction == "K":
                return [self.pTwoCurX,self.pTwoCurY]
            else:
                print("error")
        else:
            print("Not in list of possible moves")


    #Shows the spaces with events on the map
    def showEvents(self):
        for i in eventPlaces:
            x = i[0]
            y = i[1]
            self.grid[x][y] = "[-E-]"
        self.display()
        for i in eventPlaces:
            x = i[0]
            y = i[1]
            self.grid[x][y] = "[---]"


