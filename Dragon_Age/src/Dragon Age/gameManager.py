import pygame
from dragonTower import setDragons
from enemy import setWave
from path import createPath, inPlay, onBoard, inParty, evolveBound
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
    drawAll()
    timerFired()





   
