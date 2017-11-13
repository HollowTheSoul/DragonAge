import pygame
from dragonTower import setDragons
from enemy import setWave
from path import createPath, inPlay, onBoard, inParty, upgradeBound
from draw import drawAll
from timerFired import timerFired
import gameData

def gameInit():
    #Create path
    createPath()

    #Initialise the dragons
    setDragons()

    #Initialise the enemies
    setWave() 

def runGame():
    #draw the game
    drawAll()

    #Start time-based modules
    timerFired()


def mousePress(x,y):
    check = upgradeBound(x,y)

    if inPlay(x,y):
        gameData.isPaused = False

    elif inParty(x,y):
        curDragon = inParty(x,y)#current dragon
        if curDragon.onBoard == False:#only in party not on board yet
            gameData.playerSelected = curDragon#pick up pokemon
            gameData.playerSelected.x,gameData.playerSelected.y = x,y
        #already on board, show status
        else: 
            gameData.playerShowStatus = curDragon
            print gameData.playerShowStatus

    elif gameData.playerSelected!=None:
        #picked up to pokemon to put on board
        if onBoard(x,y):
            gameData.playerSelected.x,gameData.playerSelected.y = x,y
            gameData.playerSelected.bounds = x-10,y-10,x+10,y+10
            gameData.playerSelected.onBoard,gameData.playerSelected =True,None
    
    elif gameData.playerShowStatus!= None and upgradeBound(x,y):
        (gameData.playerShowStatus).upgradeTower()
    




   
