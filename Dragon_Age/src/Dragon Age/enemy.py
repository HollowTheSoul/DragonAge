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
        self.speed = gameData.enemySpeed
        self.exit = False
        self.loc = 0 #index of data checkpoints
        self.img = pygame.transform.flip(self.img, True, False)
        
        self.setLevel()
        self.hp = self.setHP()
        self.maxHP = self.hp
        self.isFrozen = False
        self.isFrozenCount = 0
        
        frozenImage = pygame.image.load("img/f%s.png" % self.dragon)
        self.frozenImg = pygame.transform.scale(frozenImage, (40,40))
        self.frozenImg = pygame.transform.flip(self.frozenImg, True, False)
        
        
        self.isPoison = False
        self.isPoisonCount = 0
        
        poisonImage = pygame.image.load("img/p%s.png" % self.dragon)
        self.poisonImg = pygame.transform.scale(poisonImage, (40,40))
        self.poisonImg = pygame.transform.flip(self.poisonImg, True, False)
        
        frozenPoisonImage = pygame.image.load("img/fp%s.png" % self.dragon)
        self.frozenPoisonImg = pygame.transform.scale(frozenPoisonImage, (40,40))
        self.frozenPoisonImg = pygame.transform.flip(self.frozenPoisonImg, True, False)
    
    
    def setHP(self):
        growthHp = self.level*5
        return self.baseHp + growthHp
    
    def setLevel(self):
        avg = gameData.wave*3
        num = random.randint(-2,2)
        self.level = avg + num
    
    def moveEnemy(self): #move enemy along the path
        try:
            self.loc += self.speed
            self.x, self.y = gameData.checkPoints[self.loc]
            self.bounds = (self.x - self.size, self.y - self.size,
                           self.x + self.size, self.y + self.size)
        
        except: #reached end
            self.exit = True #disappears
            self.bounds = None

def drawEnemy(self,canvas):
    if self.isFrozen and self.isPoison:
        gameData.screen.blit(self.frozenPoisonImg, (self.x - self.size, self.y - self.size))
        elif self.isPoison:
            gameData.screen.blit(self.poisonImg, (self.x - self.size, self.y - self.size))
    elif self.isFrozen:
        gameData.screen.blit(self.frozenImg, (self.x - self.size, self.y - self.size))
        else:
            gameData.screen.blit(self.img, (self.x - self.size, self.y - self.size))



