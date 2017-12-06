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
towerCoord = [(0,0,0,0)] #tower locations
route = [(0,0,420,80), (145,80,250,182), (373,88,239,279), (300,249,420,280),
        (267,283,312,462), (312,413,430,464), (433,338,541,375),
        (500,377,546,462), (544,426,733,464), (490,0,705,144), (628,0,799,599) ]

#--------------------------game statistics----------------------------
wave = 1
life = 10

#--------------------------player data--------------------------------
playerHover = None
playerSelected = None
playerCoins = 1500
playerShowStatus = None
playerMessage = False

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
enemySpeed = 3
enemySpeed2 = 4
enemyCount = 30
enemyCount2 = 30
enemyMaxCount = 30
enemyMaxCount2 = 30
enemyNum = 7 #number of enemies per wave for walking enemy
enemyNum2 = 1 #number of enemies per wave for flying enemy
