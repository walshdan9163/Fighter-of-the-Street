
#Save
def save(player, usedPlaces, gamePoint):
    import pickle
    fileName = input("What do you want to name the file?")
    fileName = open(fileName + ".bin", "wb")
    pickle.dump(player,fileName)
    pickle.dump(usedPlaces, fileName)
    pickle.dump(gamePoint,fileName)
    fileName.close()

def saveMultiplayer(playerOne, playerTwo, usedPlaces, gamePoint):
    import pickle
    fileName = input("What do you want to name the file?")
    fileName = open(fileName + ".bin", "wb")
    pickle.dump(playerOne,fileName)
    pickle.dump(playerTwo, fileName)
    pickle.dump(usedPlaces, fileName)
    pickle.dump(gamePoint, fileName)
    fileName.close()


    
def main():
    size = 16

    #Imports
    import pickle
    import random
    import Character
    import Map

    #Reading intro
    intro = open("intro.txt", "r")
    print(intro.read())
    intro.close()

    playerOnePrompt = open("playerOnePrompt.txt","r")
    line = playerOnePrompt.read()
    playerOnePrompt.close()

    playerTwoPrompt = open("playerTwoPrompt.txt","r")
    display = playerTwoPrompt.read()
    playerOnePrompt.close()

    #used
    usedPlaces = []


    vicPoints = 0
    #Load Game


   
    #Character creation
    ans = input("Multiplayer or Singleplayer?(m/s): ")
    if ans == "m":
        ansTwo = input("Do you have a saved game?(y/n): ")
        if ansTwo == "y":
            eventPlaces = [(0, 1),(2, 2),(5, 3),(4, 8),(9, 0),(4, 3),(1, 5),(0,6),(0,4),(0,12),(2,8),(3,6),(3,1),(1,0),(5,11),(11,6),(14,14),(15,12),(7,5),(3,14),(1,15),(14,1),(15,13),(9,8),(8,1),(8,6),(15,2)]
            loadName = input("What is the name of your saved file?: ")
            f = open(loadName + ".bin","rb")
            playerOne = pickle.load(f)
            playerTwo = pickle.load(f)
            pMap = pickle.load(f)
            gamePoint = pickle.load(f)
            f.close()
            print("\nWelcome back, "+playerOne.getName())
            print("You have " + str(playerOne.getVicPoints()) + " victory points")
            print("\nHello, "+playerTwo.getName())
            print("You have " + str(playerTwo.getVicPoints()) + " victory points")

        else:
            #Ask for length of game
            gamePoint = ""
            recommended = []
            for i in range(10):
                recommended.append(i+1)
            while gamePoint not in recommended:
                try:
                    gamePoint = int(input("What do you want to play until? (1-10 recommended): "))
                except ValueError:
                    print("Not a recognized input")

            #Character Names
            pOneInput = input("What is player one's name?: ")
            playerOne = Character.Character(pOneInput)
            if pOneInput == "jon" or pOneInput == "Jon":
                playerOne.setCheatMode(True)
                print("CheatMode is on")
            else:
                playerOne.setCheatMode(False)
                print("cheatmode is being set to false")

            pTwoInput = input("What is player Two's name?:")    
            playerTwo = Character.Enemy(pTwoInput)
            if pTwoInput == "jon" or pTwoInput == "Jon":
                playerTwo.setCheatMode(True)
                print("CheatMode is on")
            else:
                playerTwo.setCheatMode(False)
                print("cheatmode is being set to false")


            pMap = Map.Map(size)
            pTwoSpot = pMap.getSize()
            pMap.setPlayerTwo(0,pTwoSpot-1)
            pMap.setPlayer(0,0)
            eventPlaces = [(0, 1),(2, 2),(5, 3),(4, 8),(9, 0),(4, 3),(1, 5),(0,6),(0,4),(0,12),(2,8),(3,6),(3,1),(1,0),(5,11),(11,6),(14,14),(15,12),(7,5),(3,14),(1,15),(14,1),(15,13),(9,8),(8,1),(8,6),(15,2)]
            i = 0
            while i < 45 and i not in eventPlaces:
                g = random.randint(1,size-1)
                h = random.randint(1,size-1)
                pMap.addTerrain(g,h)
                i += 1

        #Displaying map
        print("Here is the map: ")
        pMap.display()

        #Playing the game
        #Player One's turn
        while playerOne.getVicPoints() < gamePoint and playerTwo.getVicPoints() < gamePoint:
            print(line)
            print("You have " + str(playerOne.getVicPoints()) + " victory point(s).")
            response = ""
            options = ["w", "a", "s", "d", "2", "4", "6", "8", "k","event"]
            while response not in options:
                response = input("\nWhere do you want to move?: ")#Asks where player wants to move
                #If player chooses to save
                if response == "k":
                    saveMultiplayer(playerOne, playerTwo, pMap, gamePoint)#Save function
                    break
                #Shows events on the map
                if response == "event":
                    if playerOne.getCheatMode():
                        pMap.showEvents()
                    else:
                        print("You don't have access to this intel.")
                else:
                    coordinates = pMap.moveDir(response)#Moves the player, and returns the coordinates as a list
                    newPlace = (coordinates)
                    usedPlaces.append(newPlace)
                    result = Map.eventCheck(coordinates[0],coordinates[1], eventPlaces, playerOne.getCheatMode())#checks for event at those coordinates
                    if result == True:
                        playerOne.addVicPoint()
                        if playerOne.getVicPoints() > gamePoint:
                            break
                    else:
                        temp = 100

                #Player Two's turn
                print(display)
                print("You have " + str(playerTwo.getVicPoints()) + " victory point(s).")
                response = ""
                options = ["w", "a", "s", "d", "2", "4", "6", "8", "k", "event"]
                while response not in options:
                    response = input("\nWhere do you want to move?: ")#Asks where player wants to move
                    #If player chooses to save
                    if response == "k":
                        saveMultiplayer(playerOne, playerTwo, pMap, gamePoint)#Save function
                        break
                    #Shows events on the map
                    if response == "event":
                        if playerTwo.getCheatMode():
                            pMap.showEvents()
                        else:
                            print("You don't have access to this intel!")
                    else:
                        coordinates = pMap.playerTwoMoveDir(response)#Moves the player, and returns the coordinates as a list
                        newPlace = (coordinates)
                        usedPlaces.append(newPlace)
                        result = Map.eventCheck(coordinates[0],coordinates[1], eventPlaces, playerTwo.getCheatMode())#checks for event at those coordinates
                        if result == True:
                            playerTwo.addVicPoint()
                            if playerOne.getVicPoints() > gamePoint:
                                break
                        else:
                            temp = 100

        #End of Game
        if playerOne.getVicPoints() < gamePoint and playerTwo.getVicPoints() < gamePoint:
            print("Come back soon!!")
            end = input("\nPress enter to close the game.")

        elif playerTwo.getVicPoints() > gamePoint:
            print(playerTwo.getName() + " wins!")
            end = input("\nPress enter to close the game.")

        elif playerOne.getVicPoints() > gamePoint:
            print(playerOne.getName() + " wins!")
            end = input("\nPress enter to close the game.")

        else:
            print("Error!")
            end = input("\nPress enter to close the game.")



    #Single player gameplay
    else:
        savedGame = input("Do you want to load a game?(y/n): ")
        if savedGame == "y" or savedGame == "Y":
            eventPlaces = [(0, 1),(2, 2),(5, 3),(4, 8),(9, 0),(4, 3),(1, 5),(0,6),(0,4),(0,12),(2,8),(3,6),(3,1),(1,0),(5,11),(11,6),(14,14),(15,12),(7,5),(3,14),(1,15),(14,1),(15,13),(9,8),(8,1),(8,6),(15,2)]
            loadName = input("What is the name of your saved file?: ")
            f = open(loadName + ".bin","rb")
            player = pickle.load(f)
            pMap = pickle.load(f)
            gamePoint = pickle.load(f)
            f.close()
            print("Welcome back, "+player.getName())
            print("You have " + str(player.getVicPoints()) + " victory points")
        else:
            gamePoint = int(input("What do you want to play until? (1-10 recommended): "))
            name = input("\n\nWhat is your name?: ")
            print("Welcome,",name+". \nGood luck!\n")
            player = Character.Character(name)
            if player.getName() == "jon" or player.getName() == "Jon":
                player.setCheatMode(True)
            else:
                player.setCheatMode(False)

            #instructions
            print("To save your game, press 'k' when asked for your move")
            
            #map creation
            pMap = Map.Map(16)
            pMap.setPlayer(0,15)
            pMap.setPlayer(0,0)
            eventPlaces = [(0, 1),(2, 2),(5, 3),(4, 8),(9, 0),(4, 3),(1, 5),(0,6),(0,4),(0,12),(2,8),(3,6),(3,1),(1,0),(5,11),(11,6),(14,14),(15,12),(7,5),(3,14),(1,15),(14,1),(15,13),(9,8),(8,1),(8,6),(15,2)]
            i = 0
            while i < 45 and i not in eventPlaces:
                g = random.randint(1,14)
                h = random.randint(1,14)
                pMap.addTerrain(g,h)
                i += 1

    #Displaying map
        print("Here is the map: ")
        pMap.display()

        #Playing the game
        while player.getVicPoints() < gamePoint:
            print("You have " + str(player.getVicPoints()) + " victory point(s).")
            response = ""
            options = ["w", "a", "s", "d", "2", "4", "6", "8", "k","event"]
            while response not in options:
                response = input("\nWhere do you want to move?: ")#Asks where player wants to move
            #If player chooses to save
            if response == "k":
                save(player, pMap, gamePoint)#Save function
                break
            #Shows events on the map
            elif response == "event":
                if player.getCheatMode:
                    pMap.showEvents()
                else:
                    print("You don't have access to this intel!")
            else:
                coordinates = pMap.moveDir(response)#Moves the player, and returns the coordinates as a list
                newPlace = (coordinates[0],coordinates[1])
                usedPlaces.append(newPlace)
                result = Map.eventCheck(coordinates[0],coordinates[1], eventPlaces, player.getCheatMode())#checks for event at those coordinates
                if result == True:
                    player.addVicPoint()
                    if player.getVicPoints() > gamePoint:
                        break
                    else:
                        temp = 100

        if player.getVicPoints() < gamePoint:
            print("Come back soon!")
            end = input("\nPress enter to close the game.")
            
        else:
            print("Congrats. You win the game!")
            end = input("\nPress enter to close the game.")



main()
