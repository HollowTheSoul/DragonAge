import pygame, random
from dragon import Dragon
import gameData

##  @brief Set enemy waves
#   @return none
#   set enemy waves with 4 types of enemies, set number of enemies per wave
#   and enemy moving speed depending on waves
def setWave():
    enemyParty = [10,11,12,13]  #walking enemy
    enemyParty2 = [14]  #flying enemy
    if gameData.wave%2 == 0:
        gameData.enemySpeed += 1
    if gameData.wave%4 == 0:
        gameData.enemyNum += 2
        gameData.enemyNum2 += 2
    #walking
    gameData.waveEnemies = [Enemy(enemyParty[random.randint(0,len(enemyParty))-1],
                    gameData.dragonDatabase) for i in range(gameData.enemyNum)]
    #flying
    gameData.waveEnemies2 = [Enemy(enemyParty2[random.randint(0,len(enemyParty2))-1],
                    gameData.dragonDatabase) for i in range(gameData.enemyNum2)]

##  @brief Enemy class
#   This is the enemy class that creates enemy objects in the game
class Enemy(Dragon):

    ##  @brief the constructor of Enemy class
    #   @param self this is the self
    #   @param dragon Dragon class
    #   @param dragonDatabase List of information about the dragon
    #   @param x the x coord in int
    #   @param y the y coord in int
    #   @return none
    def __init__(self, dragon, dragonDatabase, x=-1, y=-1):
        Dragon.__init__(self, dragon, dragonDatabase)
        self.x = x
        self.y = y
        self.speed = gameData.enemySpeed
        self.speed2 = gameData.enemySpeed2
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

    ##  @brief set HP
    #   @param self this is the self
    #   @return self.baseHp+grouthHP return the hp of enemy
    #   set the hp of enemy depending on baseHP and growthHP
    def setHP(self):
        growthHp = self.level*5
        return self.baseHp + growthHp

    ##  @brief set level
    #   @param self this is the self
    #   @return none
    #   set the level of enemy depending on the wave and a random integer
    def setLevel(self):
        avg = gameData.wave*3
        num = random.randint(-2,2)
        self.level = avg + num

    ##  @brief move walking enemy
    #   @param self this is the self
    #   @return none
    #   move the enemy along the path, remove enemy when it exit
    def moveEnemy(self):
        try:
            self.loc += self.speed
            self.x, self.y = gameData.checkPoints[self.loc]
            self.bounds = (self.x - self.size, self.y - self.size,
                           self.x + self.size, self.y + self.size)
                        
        except: #reached end
            self.exit = True #disappears
            self.bounds = None


    ##  @brief move flying enemy
    #   @param self this is the self
    #   @return none
    #   move the enemy along the path2, remove enemy when it exit
    def moveEnemy2(self):
        try:
            self.loc += self.speed2
            self.x, self.y = gameData.checkPoints2[self.loc]
            self.bounds = (self.x - self.size, self.y - self.size,
                           self.x + self.size, self.y + self.size)
                        
        except: #reached end
            self.exit = True #disappears
            self.bounds = None

    ##  @brief draw enemy on map
    #   @param self this is the self
    #   @param canvas The game screen
    #   @return none
    def drawEnemy(self,canvas):
        if self.isFrozen and self.isPoison:
            gameData.screen.blit(self.frozenPoisonImg, (self.x - self.size, self.y - self.size))
        elif self.isPoison:
            gameData.screen.blit(self.poisonImg, (self.x - self.size, self.y - self.size))
        elif self.isFrozen:
            gameData.screen.blit(self.frozenImg, (self.x - self.size, self.y - self.size))
        else:
            gameData.screen.blit(self.img, (self.x - self.size, self.y - self.size))



