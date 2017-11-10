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