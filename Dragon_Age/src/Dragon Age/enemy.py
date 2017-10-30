import pygame, random
from dragon import Dragon
import gameData

def setWave():
    enemyParty = [10,11,12,13]
    if gameData.wave%2 == 0:
        gameData.enemySpeed += 1
    if gameData.wave%4 == 0:
        gameData.enemyNum += 2

    gameData.waveEnemies = [Enemy(enemyParty[random.randint(0,len(enemyParty))-1],
                                  gameData.dragonDatabase) for i in range(gameData.enemyNum)]

class Enemy(Dragon):
    def __init__(self, dragon, dragonDatabase, x=-1, y=-1):
        Dragon.__init__(self, dragon, dragonDatabase)
        self.x = x
        self.y = y
        self.exit = False
        self.loc = 0 #index of data checkpoints
        self.img = pygame.transform.flip(self.img, True, False)
        self.setLevel()
        self.hp = self.setHP()
        self.maxHP = self.hp

    def setHP(self):
        growthHp = self.level*5
        return self.baseHp + growthHp

    def setLevel(self):
        avg = gameData.wave*3
        num = random.randint(-2,2)
        self.level = avg + num

    def moveEnemy(self): #move enemy along the path
        try:
            self.loc += gameData.enemySpeed
            self.x, self.y = gameData.checkPoints[self.loc]
            self.bounds = (self.x - self.size, self.y - self.size,
                           self.x + self.size, self.y + self.size)
        except: #reached end
            self.exit = True #disappears
            self.bounds = None

    def drawEnemy(self,canvas):
        gameData.screen.blit(self.img, (self.x - self.size, self.y - self.size))

