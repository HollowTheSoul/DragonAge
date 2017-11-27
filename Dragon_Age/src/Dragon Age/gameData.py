import pygame
from database import setDragonData

#--------------------------window and screen--------------------------
WINDOW_SIZE = width, height = 800, 620
screen = pygame.display.set_mode(WINDOW_SIZE)


#--------------------------game mode----------------------------------
isIntro = True
isInGame = False
isGameOver = False
isPaused = False

#--------------------------game path data-----------------------------
checkPoints = [] #walking enemy
checkPoints2 = [] #flying enemy
boardBounds = 0, 700, 0, 520

#--------------------------game statistics----------------------------
wave = 1
life = 10

#--------------------------player data--------------------------------
playerHover = None
playerSelected = None
playerCoins = 1500
playerShowStatus = None

#--------------------------dragon data--------------------------------
dragonDatabase = setDragonData() #get data from database
dragonType = [] #3 types of dragons for other modules to refer to 
dragonParty = [] #the current party of dragons on board
dragonSize = 30


#--------------------------enemy data---------------------------------
#dragons to be appended to enemies
waveEnemies = [] #walking
waveEnemies2 = [] #flying
#enemy dragons for current wave
enemies = []
enemies2 = []
enemySpeed = 4
enemySpeed2 = 3
enemyCount = 30
enemyCount2 = 30
enemyMaxCount = 30
enemyMaxCount2 = 30
enemyNum = 7 #number of enemies per wave for walking enemy
enemyNum2 = 1 #number of enemies per wave for flying enemy
