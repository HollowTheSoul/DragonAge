import sys, pygame, random, string, math
from database import setDragonData
from hover import *

class Struct(object):pass
data = Struct()

#--------------------------Init--------------------------------------------
def init(data):
    pygame.init()
    pygame.display.set_caption("Dragon Age")
    data.size = width, height = 800, 620
    data.screen = pygame.display.set_mode(data.size)
    #set all initial data
    listInit(data)
    databaseInit(data)
    modeInit(data)
    playerInit(data)
    enemyInit(data)
    

#set dragon data from database.py
def databaseInit(data):
    data.database = setDragonData()
    data.dragonSize = 30
    createPath(data)
    setDragons(data)
    data.boardBounds = 0, 700, 0, 520
    
def modeInit(data):
    data.intro = True
    data.gameOver = False
    data.paused = True

def playerInit(data):
    data.lives = 10
    data.wave = 1
    data.hover = None
    data.selected = None
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
    #3 types of dragons for my party when starting the game
    data.party = []
    #dragons to be appended to enemies
    data.waveEnemies = []
    #enemy dragons for current wave
    data.enemies = []

def setDragons(data):
    fireDragon =myParty(1,data)
    waterDragon = myParty(2,data)
    iceDragon = myParty(3,data)
    data.party.append(fireDragon)
    data.party.append(waterDragon)
    data.party.append(iceDragon)
    print(data.party)

def createPath(data):
    corners = [(0,80),(185,80),(185,165),(293,165),(293,80),(420,80),
               (420,265),(300,265),(300,450),(420,450),(420,365),
               (535,365),(535,450),(700,450)]
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
        self.upgrade = tup[4]
        self.attackGrowth = 10
        self.bounds = None
        self.button = None
        self.setSize()
        image = pygame.image.load("%s.png" % self.dragon)
        self.img = pygame.transform.scale(image, (30,30))

    def setSize(self):
        self.size = data.dragonSize

class myParty(Dragon):
    def __init__(self,dragon,data,level=1,x=None,y=None):
        #super
        Dragon.__init__(self,dragon,data)
        self.x = x
        self.y = y
        self.setRange()
        #when to shoot next bullet
        self.maxCounter = 8
        self.counter = self.maxCounter
        self.target = None
        self.bullets = []
        self.onBoard = False
        self.radius = False
        self.level = level
        self.numOfUpgrade = 0
        self.attack = self.baseAttack

    def setRange(self):
        if self.upgrade == 0:
            self.range = 50
        if self.upgrade == 1:
            self.range = 80
        if self.upgrade == 2:
            self.range = 120

    #using the right triangle theory to calculate if the enemy is in range
    def isInRangeEquation(self,x,y):
        return (x-self.x)**2 + (y-self.y)**2 < self.range**2

    def isInRange(self,bounds):
        x0,x1,y0,y1 = bounds
        if (self.isInRangeEquation(x0,y0) or self.isInRangeEquation(x0,y1) or
            self.isInRangeEquation(x1,y0) or self.isInRangeEquation(x1,y1)):
            return True
        else:
            return False    
    
    def drawTower(self,canvas):#draw dragon once set on board
        data.screen.blit(self.img,(self.x-self.size,self.y-self.size))

    def drawRadius(self,canvas):#draws radius sof pokemon
        pygame.draw.circle(canvas,(255,255,255),(self.x,self.y),self.range,3)

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


class Bullet(object):
    def __init__(self,x,y,target,element):
        self.targetX,self.targetY=target
        self.x = x
        self.y = y
        self.bounds = x-5,y-5,x+5,y+5
        self.remove = False#if hits something
        self.getDirection()
        self.speed = 5#speed of bullet
        self.setImage(element)

    def setImage(self,element):#bullet img set based on element of pokemon
        self.img = pygame.image.load("%s.png" % element)

    def getDirection(self):
    #find direction of bullet in radians with given target
        dx = self.targetX-self.x
        dy = self.targetY-self.y
        rads = math.atan2(dy,dx)
        rads %= 2*math.pi
        self.dir = rads# in radians

    def shotEnemy(self,enemy):
        #whether the bullet intersects with an enemy bound
        (ax0, ay0, ax1, ay1) = self.bounds
        (bx0, by0, bx1, by1) = enemy.bounds
        return ((ax1 > bx0) and (bx1 > ax0) and (ay1 > by0) and (by1 > ay0))

    def moveBullet(self):
        #move bullet according to direction
        self.x += int(round(math.cos(self.dir)*self.speed))
        self.y += int(round(math.sin(self.dir)*self.speed))
        self.bounds = self.x-5,self.y-5,self.x+5,self.y+5

    def drawBullet(self,canvas):#draws bullet on canvas
        canvas.blit(self.img,(self.x,self.y))
#-------------------------TimerFired functions----------------------------

def moveAllBullets(data):#moves all bullets toward set direction
    for tower in data.party:
        for bullet in tower.bullets:
            bullet.moveBullet()
            width,height = data.size
            #if goes out of bounds, remove bullets
            x0,x1,y0,y1 =data.boardBounds
            if (bullet.x>x1 or bullet.x<0 or bullet.y>y1 
                or bullet.y<0):
                bullet.remove = True
            
def removeBullets(data):
    #check whether bullets are removed for every frame and replace bullet list
    for tower in data.party:
        if tower.onBoard and tower.bullets!=[]:
            temp = []
            for bullet in tower.bullets:
                if bullet.remove == False:
                    temp.append(bullet)
            tower.bullets = temp

def setTarget(data):
    #sets target for each tower 
    if data.enemies!= []:
        for tower in data.party:
            if tower.onBoard:
                enemyPoke = tower.target
                #set target, either when doesnt exist or changing targets
                if (tower.target==None or not tower.isInRange((enemyPoke.x,
                    enemyPoke.y,enemyPoke.x+10,enemyPoke.y+10))or
                    tower.target.exit):
                    for enemy in data.enemies:#loops through all enemeis
                        if enemy.exit == False:#make sure enemy hasn't died yet
                            bounds = enemy.x,enemy.y,enemy.x+10,enemy.y+10
                            if tower.isInRange(bounds):
                                #sets first enemy found as target and breaks
                                tower.target = enemy
                                break
                #sets target as None if target goes out of range or target dies
                if tower.target != None and (tower.target.exit or not 
                    tower.isInRange((tower.target.x,tower.target.y,
                    tower.target.x+10,tower.target.y+10))):
                    tower.target = None

def shootEnemies(data):#check whether each bullet has shot an enemy
    for tower in data.party:
        if tower.onBoard and tower.bullets!=[]:
            for bullet in tower.bullets:
                for enemy in data.enemies:
                    if enemy.exit == False:
                        if bullet.shotEnemy(enemy):
                            enemy.hp-=setDamage(data,tower.attack,
                                tower.element,enemy.element)
                            bullet.remove =True
                        if enemy.hp<=0:#kills an enemy, gains exp and money
                            enemy.exit = True
                            data.coins+=555

#set damage of bullet according to stats of pokemon as well as type of bullet
def setDamage(data,attack,attackType,enemyType):
    return attack

def setBullets(data):#set bullets for towers if tower has a target 
    if data.enemies!= []:
        for tower in data.party:
            if tower.onBoard and tower.target!= None:
                if tower.counter>= tower.maxCounter:
                    target = tower.target.x,tower.target.y
                    tower.bullets.append(Bullet(tower.x,tower.y,
                        target,tower.element))
                    tower.counter =0#counter for time between new bullet
                else:   tower.counter+=1


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
        hover(data)
        moveAllEnemies(data)
        setTarget(data)
        setBullets(data)
        moveAllBullets(data)
        shootEnemies(data)
        removeBullets(data)
        
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

def drawTowers(data):#draw all towers on board
    for dragon in data.party:
        if dragon.onBoard == True:
            dragon.drawTower(data.screen)

def drawParty():
    startY =60
    startX = 690
    width = 100
    height = 25
    font = pygame.font.Font("pokemon_pixel_font.ttf",20)
    for i in range(len(data.party)):
        dragon = data.party[i]#display name of each pokemon
        name = dragon.dragon
        dragon.button = startX,startY,width,height
        if data.hover == dragon or data.selected == dragon:
            pygame.draw.rect(data.screen,(255,0,0),(dragon.button),1)
        name = font.render(name,True,(255,255,255))
        data.screen.blit(name,(startX+5,startY+5))
        startY+=25

def drawAllBullets(data):#draws all bullets on board
    for tower in data.party:
        if tower.onBoard and tower.bullets!=[]:
            for bullet in tower.bullets:
                bullet.drawBullet(data.screen)


def drawAll(data):
    drawEnemies(data)
    drawPlay(data)
    drawTowers(data)
    drawParty()
    drawAllBullets(data)


    
#=-------------------------Button bounds--------------------------------------

def inPlay(x,y):
    x0,y0,x1,y1 = 45,395,105,455
    return x < x1 and x > x0 and y > y0 and y < y1

def onBoard(data,x,y):
    ax0,ay0,ax1,ay1 = (x-data.dragonSize,y-data.dragonSize,
        x+data.dragonSize,y+data.dragonSize)
    bx0,bx1,by0,by1 = data.boardBounds
    return ((ax1 > bx0) and (bx1 > ax0) and (ay1 > by0) and (by1 > ay0))

def inMenuBounds(x,y):#if clicks in menu button
    x0,x1,y0,y1 =700,800,520,620
    return x<x1 and x>x0 and y>y0 and y<y1


def inParty(x,y):
    for dragon in data.party:
        x0,y0,width,height = dragon.button
        x1,y1 = x0+width, y0+height
        if x>x0 and x<x1 and y>y0 and y<y1:
            return dragon
    return False

#=-------------------------MousePress--------------------------------------

def mousePress(x,y,data):
    if inPlay(x,y):
        data.paused = False
    if inParty(x,y):
        curDragon = inParty(x,y)#current dragon
        if curDragon.onBoard == False:#only in party not on board yet
            data.selected = curDragon#pick up pokemon
            data.selected.x,data.selected.y = x,y
        #already on board, show status
        else: 
            data.status = curDragon
    elif data.selected!=None:
        #picked up to pokemon to put on board
        if onBoard(data,x,y):
            data.selected.x,data.selected.y = x,y
            data.selected.bounds = x-10,y-10,x+10,y+10
            data.selected.onBoard,data.selected =True,None

def mouse(data):
    x, y = pygame.mouse.get_pos()
    if data.intro:
        mousePress(x,y,data)

# =--------------------------Hover-----------------------------
def hover(data):#general hover fucntion wrap
    x,y = pygame.mouse.get_pos()
    if data.selected!= None:#put tower on board
        buildTowerHover(x,y,data)

def buildTowerHover(x,y,data):
#draw rect of size of pokemon when building if legal
    data.selected.x, data.selected.y= x,y
    if onBoard(data,x,y):
        pygame.draw.rect(data.screen,(255,255,255),(x-data.selected.size,
            y-data.selected.size,data.selected.size*2,data.selected.size*2),
            3)

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
