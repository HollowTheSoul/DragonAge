import pygame
from bullet import Bullet
from path import inPlay, onBoard, inParty
import gameData

def moveAllBullets():#moves all bullets toward set direction
    for tower in gameData.dragonParty:
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
    for tower in gameData.dragonParty:
        if tower.onBoard and tower.bullets!=[]:
            temp = []
            for bullet in tower.bullets:
                if bullet.remove == False:
                    temp.append(bullet)
            tower.bullets = temp

def setTarget():
    #sets target for each tower 
    if gameData.enemies!= []:
        for tower in gameData.dragonParty:
            if tower.onBoard:
                enemyDragon = tower.target
                #set target, either when doesnt exist or changing targets
                if (tower.target==None or not tower.isInRange((enemyDragon.x,
                    enemyDragon.y,enemyDragon.x+10,enemyDragon.y+10))or
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

def setDamage(attack):
    return attack



def shootEnemies():#check whether each bullet has shot an enemy
    for tower in gameData.dragonParty:
        if tower.onBoard and tower.bullets!=[]:
            for bullet in tower.bullets:
                for enemy in gameData.enemies:
                    if enemy.exit == False:
                        if bullet.shotEnemy(enemy):
                            if bullet.element == "ice":
                                if enemy.isFrozen == False:
                                    enemy.speed = enemy.speed - 2
                                    enemy.isFrozen = True
                                    enemy.isFrozenCount = 0
                            
                            elif bullet.element == "poison":
                                if enemy.isPoison == False:
                                    enemy.speed = enemy.speed - 1
                                    enemy.isPoison = True
                                    enemy.isPoisonCount = 0
                                
                            enemy.hp-=tower.attack #damage the enemy
                            bullet.remove =True
                        
                        if enemy.hp<=0:#kills an enemy, gains exp and money
                            enemy.exit = True
                            gameData.playerCoins+=50

def setBullets():#set bullets for towers if tower has a target 
    if gameData.enemies!= []:
        for tower in gameData.dragonParty:
            if tower.onBoard and tower.target!= None:
                if tower.counter>= tower.maxCounter:
                    target = tower.target.x,tower.target.y
                    tower.bullets.append(Bullet(tower.x,tower.y,
                        target,tower.element,tower.upgrade))
                    tower.counter = 0 #counter for time between new bullet
                else:   tower.counter+=1

#check whether all bullets are removed from board
def allBulletsRemoved():
    for tower in gameData.dragonParty:
        if tower.onBoard and tower.bullets != []:
            for bullet in tower.bullets:
                if bullet.remove == False:
                    return False
    return True
