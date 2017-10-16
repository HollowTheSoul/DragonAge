from __future__ import print_function, division
import sys, pygame, random, string, math
from database import setDragonData

class Struct(object):pass
data = Struct()

#--------------------------Init--------------------------------------------
def init(data):
    pygame.init()
    pygame.display.set_caption("Dragon Age")
    data.size = width, height = 800, 620
    data.screen = pygame.display.set_mode(data.size)
    #set all mode
    listInit(data)
    databaseInit(data)
    modeInit(data)
    playerInit(data)
    enemyInit(data)

def databaseInit(data):
    data.database = setDragonData()
    data.dragonSize = 25
    createPath(data)
    data.boardBounds = 0, 700, 0, 520
    
    
def modeInit(data):
    data.intro = True
    data.gameOver = False
    data.paused = True

def playerInit(data):
    data.lives = 10
    data.wave = 1
    data.coins = 100

def enemyInit(data):
    data.speed = 4
    #counter for frames before placing a new enemy
    data.count = 30
    data.maxCount = 30
    #number of enemies per wave
    data.num = 7
    setWave(data)

def listInit(data):
    data.waveEnemies = []
    data.enemies = []

def createPath(data):
    corners = [(50,50),(100,50),(100,520)]
    data.checkPoints = []
    #adds all x, y positions into new list
    for i in range(1, len(corners)):
        x0,y0 = corners[i-1]
        x1,y1 = corners[i]
        #check if horizontal or veritcal
        if x1 - x0 == 0:
            verticalPath(data,x0,y0,x1,y1)
        else:
            horizontalPath(data,x0,y0,x1,y1)

def verticalPath(data,x0,y0,x1,y1):
    #distance between 2 corners
    dis = y1 - y0
    for i in range(abs(dis)):
        if dis < 0:
            data.checkPoints.append((x0,y0-i))
        else:
            data.checkPoints.append((x0,y0+i))

def horizontalPath(data,x0,y0,x1,y1):
    #distance between 2 corners
    dis = x1 - x0
    for i in range(abs(dis)):
        if dis < 0:
            data.checkPoints.append((x0-i,y0))
        else:
            data.checkPoints.append((x0+i,y0))

#------------------------Classes-------------------------------------------

class Dragon(object):
    def __init__(self, dragon, data):
        tup = data.database[dragon]
        self.id = dragon
        self.dragon = tup[0]
        self.element = tup[1]
        self.baseAttack = tup[2]
        self.baseHp = tup[3]
        self.bounds = None
        self.button = None
        self.setSize()
        image = pygame.image.load("%s.png" % self.dragon)
        self.img = pygame.transform.scale(image, (30,30))

    def setSize(self):
        self.size = data.dragonSize

class Enemy(Dragon):
    def __init__(self, dragon, data, x=-1, y=-1):
        Dragon.__init__(self, dragon, data)
        self.x = x
        self.y = y
        self.exit = False
        self.loc = 0 #index of data checkpoints
        self.img = pygame.transform.flip(self.img, True, False)
        self.setLevel(data)
        self.hp = self.setHP()
        self.maxHP = self.hp

    def setHP(self):
        growthHp = self.level*5
        return self.baseHp + growthHp

    def setLevel(self,data):
        avg = data.wave*3
        num = random.randint(-2,2)
        self.level = avg + num

    def moveEnemy(self): #move enemy along the path
        try:
            self.loc += data.speed
            self.x, self.y = data.checkPoints[self.loc]
            self.bounds = (self.x - self.size, self.y - self.size,
                           self.x + self.size, self.y + self.size)
        except: #reached end
            self.exit = True #disappears
            self.bounds = None

    def drawEnemy(self,canvas):
        data.screen.blit(self.img, (self.x - self.size, self.y - self.size))

#-------------------------TimerFired functions----------------------------

def setWave(data):
    if data.wave%2 == 0:
        data.speed += 1
    if data.wave%4 == 0:
        data.num += 2

    data.waveEnemies = [Enemy(4,data) for i in range(data.num)]

def moveAllEnemies(data):
    if data.waveEnemies != []:
        if data.count == data.maxCount:
            newEnemy = data.waveEnemies.pop(0)
            data.enemies.append(newEnemy)
            data.count = 0
        else:
            data.count += 1 #counter for time between adding each enemy on board
    for enemy in data.enemies:
        if enemy.exit == False:
            enemy.moveEnemy()
            if enemy.exit:
                data.lives -= 1
                if data.lives == 0:
                    data.gameOver = True


def timerFired(data):
    if data.gameOver:
        gameoverHover(data)
    elif data.intro == True:
        moveAllEnemies(data)
        
#--------------------------Draw-------------------------------------------
def drawIntro():
    img = pygame.image.load("Intro.png")
    data.screen.fill((255,255,255))
    img = pygame.transform.scale(img, (500,250))
    data.screen.blit(img, (0,0))

def loadBackground():
    img = pygame.image.load("background.png")
    data.screen.blit(img, (0,0))

def drawEnemies(data):
    for enemy in data.enemies:
        if enemy.exit == False:
            enemy.drawEnemy(data.screen)

def drawPlay(data):
    x0,y0 = 50, 400
    width, height = 70, 70
    img = pygame.image.load("play.png")
    img = pygame.transform.scale(img, (50,50))
    data.screen.blit(img, (x0, y0))

def drawAll(data):
    drawEnemies(data)
    drawPlay(data)

#=-------------------------Button bounds--------------------------------------

def inPlay(x,y):
    x0,y0,x1,y1 = 45,395,105,455
    return x < x1 and x > x0 and y > y0 and y < y1

#=-------------------------MousePress--------------------------------------

def mousePress(x,y,data):
    if inPlay(x,y):
        data.paused = False

def mouse(data):
    x, y = pygame.mouse.get_pos()
    if data.intro:
        mousePress(x,y,data)

def game():
    init(data)
    while True:
        if data.intro == True and data.gameOver == False:
            loadBackground()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: mouse(data)

        drawAll(data)
        timerFired(data)
        pygame.display.flip()
game()
