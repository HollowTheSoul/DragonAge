import pygame
from timerBullet import moveAllBullets, removeBullets, setTarget, shootEnemies, setDamage, setBullets, allBulletsRemoved
from timerHover import hover, buildTowerHover, gameoverHover
from timerEnemy import moveAllEnemies, moveAllEnemies2, roundOver
from enemy import setWave
import gameData

#-------------------------TimerFired functions----------------------------
#initiate all the timer fired functions
def timerFired():
    if gameData.isGameOver:
        gameoverHover()
    elif gameData.isIntro == True:
        hover()
        moveAllEnemies()
        moveAllEnemies2()
        setTarget()
        setBullets()
        moveAllBullets()
        shootEnemies()
        removeBullets()
        #after a wave is cleared, check conditions and add the next wave
        if (gameData.enemies != []  and
            roundOver() and allBulletsRemoved()):
            gameData.enemies = []
            gameData.enemies2 = []
            gameData.wave += 1
            setWave()
