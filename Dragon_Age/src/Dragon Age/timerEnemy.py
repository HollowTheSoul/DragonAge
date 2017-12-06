import pygame
import gameData

##  @brief move all walking enemies
#   @return none
def moveAllEnemies():
    if gameData.waveEnemies != []:
        if gameData.enemyCount == gameData.enemyMaxCount:
            newEnemy = gameData.waveEnemies.pop(0)
            #newEnemy2 = gameData.waveEnemies2.pop(0)
            gameData.enemies.append(newEnemy)
            #gameData.enemies.append(newEnemy2)
            gameData.enemyCount = 0
        else:
            #counter for time between adding each enemy on board
            gameData.enemyCount += 1
            
    for enemy in gameData.enemies:
        if enemy.exit == False:
            enemy.moveEnemy()
            if enemy.isFrozen:
                enemy.isFrozenCount += 5
                if enemy.isFrozenCount > 30:
                    enemy.speed = gameData.enemySpeed
                    enemy.isFrozen = False
                    enemy.isFrozenCount = 0
            if enemy.isPoison:
                enemy.isPoisonCount += 5
                if enemy.isPoisonCount > 50:
                    enemy.speed = gameData.enemySpeed
                    enemy.isPoison = False
                    enemy.isPoisonCount = 0
            if enemy.exit:
                gameData.life -= 1
                print(gameData.life)
                if gameData.life == 0:
                    gameData.isGameOver = True

##  @brief move all flying enemies
#   @return none
def moveAllEnemies2():
    if gameData.waveEnemies2 != []:
        if gameData.enemyCount2 == gameData.enemyMaxCount2:
            newEnemy = gameData.waveEnemies2.pop(0)
            gameData.enemies2.append(newEnemy)
            gameData.enemyCount2 = 0
        else:
            #counter for time between adding each enemy on board
            gameData.enemyCount2 += 1
    for enemy in gameData.enemies2:
        if enemy.exit == False:
            enemy.moveEnemy2()
            if enemy.isFrozen:
                enemy.isFrozenCount += 5
                if enemy.isFrozenCount > 30:
                    enemy.speed = gameData.enemySpeed
                    enemy.isFrozen = False
                    enemy.isFrozenCount = 0
            if enemy.isPoison:
                enemy.isPoisonCount += 5
                if enemy.isPoisonCount > 50:
                    enemy.speed = gameData.enemySpeed
                    enemy.isPoison = False
                    enemy.isPoisonCount = 0
            if enemy.exit:
                gameData.life -= 1
                print(gameData.life)
                if gameData.life == 0:
                    gameData.isGameOver = True

##  @brief remove all enemies from enemy list
#   @return none
def removeAllEnemies():
    if gameData.life == 0:
        gameData.waveEnemies = []
        gameData.waveEnemies2 = []
        
##  @brief check whether the round is over
#   @return a boolean of whether the round is over
def roundOver():
    for enemy in gameData.enemies:
        if enemy.exit == False:
            return False
    for enemy in gameData.enemies2:
        if enemy.exit == False:
            return False
    return True
