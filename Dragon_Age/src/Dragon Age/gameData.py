import pygame
from database import setDragonData

#--------------------------window and screen--------------------------
WINDOW_SIZE = width, height = 800, 620
screen = pygame.display.set_mode(WINDOW_SIZE)

#--------------------------game mode----------------------------------
isIntro = True  
isGameOver = False
isPaused = True

#--------------------------game path data-----------------------------
checkPoints = []

#--------------------------game statistics----------------------------
wave = 1
life = 10

#--------------------------dragon data--------------------------------
dragonDatabase = setDragonData() #get data from database
party = []
dragonSize = 30

#--------------------------enemy data---------------------------------
#dragons to be appended to enemies
waveEnemies = []

enemySpeed = 4
enemyCount = 30
enemyMaxCount = 30
enemyNum = 7 #number of enemies per wave