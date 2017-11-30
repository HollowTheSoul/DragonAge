import pygame
from dragonTower import setDragons
from enemy import setWave
from path import createPath, createPath2, inPlay, onBoard, inParty, upgradeBound, inTowerBounds, canBuild
from draw import drawAll
from timerFired import timerFired
import gameData
import copy

def gameInit():
    #Create path
    createPath()
    createPath2()

    #Initialise the dragons
    setDragons()

    #Initialise the enemies
    setWave() 

def runGame():
    #draw the game
    if gameData.isIntro != True:
        drawAll()

    #Start time-based modules
    timerFired()


def mousePress(x,y):
    check = upgradeBound(x,y)

    if inPlay(x,y):
        gameData.isPaused = False

    elif gameData.playerShowStatus!= None and upgradeBound(x,y):
        print("Inside show status")
        (gameData.playerShowStatus).upgradeTower()

    #Click on party selection,
    elif inParty(x,y):
        curDragon = inParty(x,y)#current dragon

        #build new tower if the tower is already on board
        if (gameData.playerCoins >= 150): #only if the player have sufficient money
            selectedDragon = copy.copy(curDragon) #create a copy to be appended later to the party
            gameData.playerSelected = selectedDragon#pick up pokemon
            gameData.playerSelected.x,gameData.playerSelected.y = x,y
        
        #No money
        else:
            font = pygame.font.Font("pokemon_pixel_font.ttf",15)
            text = font.render("Insufficient gold.",True,(255,255,255))
            #draw money
            gameData.screen.blit(text,(700,60))

    #Click on Tower on board:
    elif gameData.playerSelected==None and inTowerBounds((x,y,x,y)):
        onBoardDragon = inTowerBounds((x,y,x,y))
        gameData.playerShowStatus = onBoardDragon

    elif gameData.playerSelected!=None and gameData.playerSelected.onBoard==False:
        #picked up to pokemon to put on board
        if onBoard(x,y) and canBuild(x,y):
            gameData.dragonParty.append(gameData.playerSelected)
            gameData.playerCoins -= 150 #deduct money
            gameData.playerSelected.x,gameData.playerSelected.y = x,y
            gameData.playerSelected.bounds = x-10,y-10,x+10,y+10
            gameData.playerSelected.onBoard,gameData.playerSelected =True,None
    
    else:
        gameData.playerSelected = None
        gameData.playerShowStatus = None

    




   
