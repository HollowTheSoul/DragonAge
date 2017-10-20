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
boardBounds = 0, 700, 0, 520
#--------------------------game statistics----------------------------
wave = 1
life = 10

#--------------------------player data--------------------------------
playerHover = None
playerSelected = None
playerCoins = 500
playerShowStatus = None

#--------------------------dragon data--------------------------------
dragonDatabase = setDragonData() #get data from database
dragonParty = []
dragonSize = 30

#--------------------------enemy data---------------------------------
#dragons to be appended to enemies
waveEnemies = []
#enemy dragons for current wave
enemies = []

enemySpeed = 4
enemyCount = 30
enemyMaxCount = 30
enemyNum = 7 #number of enemies per wave