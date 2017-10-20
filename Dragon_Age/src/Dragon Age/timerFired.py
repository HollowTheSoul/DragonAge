import pygame
from bullet import Bullet
from path import createPath, inPlay, onBoard, inMenuBounds, inParty
import gameData

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