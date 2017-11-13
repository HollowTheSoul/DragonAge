import pygame
from timerBullet import moveAllBullets, removeBullets, setTarget, shootEnemies, setDamage, setBullets, allBulletsRemoved
from timerHover import hover, buildTowerHover
from timerEnemy import moveAllEnemies, roundOver
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
        setTarget()
        setBullets()
        moveAllBullets()
        shootEnemies()
        removeBullets()
        #after a wave is cleared, check conditions and add the next wave
        if (gameData.enemies != [] and roundOver() and allBulletsRemoved()):
            gameData.enemies = []
            gameData.wave += 1
            setWave()
