import sys, pygame, random, string, math
from path import createPath, inPlay, onBoard, inMenuBounds, inParty
from enemy import Enemy, setWave
from dragon import Dragon
from myParty import MyParty, setDragons
from bullet import Bullet
import gameData

#--------------------------Init--------------------------------------------
def init():
    pygame.init()
    pygame.display.set_caption("Dragon Age")
    #set all initial data
    databaseInit()
    enemyInit()

#set dragon data from database.py
def databaseInit():
    createPath()
    setDragons()

def enemyInit():
    setWave()

#-------------------------TimerFired functions----------------------------
def moveAllBullets():#moves all bullets toward set direction
    for tower in gameData.party:
        for bullet in tower.bullets:
            bullet.moveBullet()
            width,height = gameData.WINDOW_SIZE
            #if goes out of bounds, remove bullets
            x0,x1,y0,y1 =gameData.boardBounds
            if (bullet.x>x1 or bullet.x<0 or bullet.y>y1 
                or bullet.y<0):
                bullet.remove = True
            
def removeBullets():
    #check whether bullets are removed for every frame and replace bullet list
    for tower in gameData.party:
        if tower.onBoard and tower.bullets!=[]:
            temp = []
            for bullet in tower.bullets:
                if bullet.remove == False:
                    temp.append(bullet)
            tower.bullets = temp

def setTarget():
    #sets target for each tower 
    if gameData.enemies!= []:
        for tower in gameData.party:
            if tower.onBoard:
                enemyPoke = tower.target
                #set target, either when doesnt exist or changing targets
                if (tower.target==None or not tower.isInRange((enemyPoke.x,
                    enemyPoke.y,enemyPoke.x+10,enemyPoke.y+10))or
                    tower.target.exit):
                    for enemy in gameData.enemies:#loops through all enemeis
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

def shootEnemies():#check whether each bullet has shot an enemy
    for tower in gameData.party:
        if tower.onBoard and tower.bullets!=[]:
            for bullet in tower.bullets:
                for enemy in gameData.enemies:
                    if enemy.exit == False:
                        if bullet.shotEnemy(enemy):
                            enemy.hp-=setDamage(tower.attack)
                            bullet.remove =True
                        if enemy.hp<=0:#kills an enemy, gains exp and money
                            enemy.exit = True
                            gameData.playerCoins+=555

#set damage of bullet according to stats of pokemon as well as type of bullet
def setDamage(attack):
    return attack

def setBullets():#set bullets for towers if tower has a target 
    if gameData.enemies!= []:
        for tower in gameData.party:
            if tower.onBoard and tower.target!= None:
                if tower.counter>= tower.maxCounter:
                    target = tower.target.x,tower.target.y
                    tower.bullets.append(Bullet(tower.x,tower.y,
                        target,tower.element))
                    tower.counter =0#counter for time between new bullet
                else:   tower.counter+=1

def moveAllEnemies():
    if gameData.waveEnemies != []:
        if gameData.enemyCount == gameData.enemyMaxCount:
            newEnemy = gameData.waveEnemies.pop(0)
            gameData.enemies.append(newEnemy)
            gameData.enemyCount = 0
        else:
            gameData.enemyCount += 1 #counter for time between adding each enemy on board
    for enemy in gameData.enemies:
        if enemy.exit == False:
            enemy.moveEnemy()
            if enemy.exit:
                gameData.life -= 1
                print(gameData.life)
                if gameData.life == 0:
                    gameData.isGameOver = True


#HOVER
def hover():#general hover fucntion wrap
    x,y = pygame.mouse.get_pos()
    if gameData.playerSelected!= None:#put tower on board
        buildTowerHover(x,y)

def buildTowerHover(x,y):
#draw rect of size of pokemon when building if legal
    gameData.playerSelected.x, gameData.playerSelected.y= x,y
    if onBoard(x,y):
        pygame.draw.rect(gameData.screen,(255,255,255),(x-gameData.playerSelected.size,
            y-gameData.playerSelected.size,gameData.playerSelected.size*2,gameData.playerSelected.size*2),
            3)

def timerFired():
    if gameData.isGameOver:
        gameoverHover()
    elif gameData.isIntro == True:
        hover()
        moveAllEnemies()
        setTarget()
        setBullets()
        moveAllBullets()
        shootEnemies()
        removeBullets()
        
#--------------------------Draw-------------------------------------------
def drawIntro():
    img = pygame.image.load("img/Intro.png")
    gameData.screen.fill((255,255,255))
    img = pygame.transform.scale(img, (500,250))
    gameData.screen.blit(img, (0,0))

def loadBackground():
    img = pygame.image.load("img/background.png")
    gameData.screen.blit(img, (0,0))

def drawEnemies():
    for enemy in gameData.enemies:
        if enemy.exit == False:
            enemy.drawEnemy(gameData.screen)

def drawPlay():
    x0,y0 = 50, 400
    width, height = 70, 70
    img = pygame.image.load("img/play.png")
    img = pygame.transform.scale(img, (50,50))
    gameData.screen.blit(img, (x0, y0))

def drawTowers():#draw all towers on board
    for dragon in gameData.party:
        if dragon.onBoard == True:
            dragon.drawTower(gameData.screen)

def drawParty():
    startY =60
    startX = 690
    width = 100
    height = 25
    font = pygame.font.Font("pokemon_pixel_font.ttf",20)
    for i in range(len(gameData.party)):
        dragon = gameData.party[i]#display name of each pokemon
        name = dragon.dragon
        dragon.button = startX,startY,width,height
        if gameData.playerHover == dragon or gameData.playerSelected == dragon:
            pygame.draw.rect(gameData.screen,(255,0,0),(dragon.button),1)
        name = font.render(name,True,(255,255,255))
        gameData.screen.blit(name,(startX+5,startY+5))
        startY+=25

def drawAllBullets():#draws all bullets on board
    for tower in gameData.party:
        if tower.onBoard and tower.bullets!=[]:
            for bullet in tower.bullets:
                bullet.drawBullet(gameData.screen)


def drawAll():
    drawEnemies()
    drawPlay()
    drawTowers()
    drawParty()
    drawAllBullets()
 
#=-------------------------MousePress--------------------------------------

def mousePress(x,y):
    if inPlay(x,y):
        gameData.isPaused = False
    if inParty(x,y):
        curDragon = inParty(x,y)#current dragon
        if curDragon.onBoard == False:#only in party not on board yet
            gameData.playerSelected = curDragon#pick up pokemon
            gameData.playerSelected.x,gameData.playerSelected.y = x,y
        #already on board, show status
        else: 
            data.status = curDragon
    elif gameData.playerSelected!=None:
        #picked up to pokemon to put on board
        if onBoard(x,y):
            gameData.playerSelected.x,gameData.playerSelected.y = x,y
            gameData.playerSelected.bounds = x-10,y-10,x+10,y+10
            gameData.playerSelected.onBoard,gameData.playerSelected =True,None

def mouse():
    x, y = pygame.mouse.get_pos()
    if gameData.isIntro:
        mousePress(x,y)


def game():
    init()
    while True:
        if gameData.isIntro == True and gameData.isGameOver == False:
            loadBackground()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: mouse()

        drawAll()
        timerFired()
        pygame.display.flip()
game()