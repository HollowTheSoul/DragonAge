import pygame
import gameData

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

#check whether the round is over
def roundOver():
    for enemy in gameData.enemies:
        if enemy.exit == False:
            return False
    return True