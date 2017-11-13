import pygame
import gameData
from dragon import Dragon

def setDragons():
    fireDragon =DragonTower(1,gameData.dragonDatabase)
    waterDragon = DragonTower(4,gameData.dragonDatabase)
    iceDragon = DragonTower(7,gameData.dragonDatabase)
    gameData.dragonParty.append(fireDragon)
    gameData.dragonParty.append(waterDragon)
    gameData.dragonParty.append(iceDragon)

## @brief Dragon Tower Class
# This class represents the tower that the users will be building. 
# It attackes enemies within range and can be upgraded.
class DragonTower(Dragon):

     ## The constructor
    def __init__(self,dragon,dragonDatabase,level=1,x=None,y=None):
        #super
        Dragon.__init__(self,dragon,dragonDatabase)
        self.x = x
        self.y = y
        self.range = dragonDatabase[dragon][5]
        self.counter = self.maxCounter
        self.target = None
        self.bullets = []
        self.onBoard = False
        self.radius = False
        self.level = level
        self.attack = self.baseAttack

    ## @brief isInRangeEquation calculates whether or not enemy is in range
    #  @param self This is the self
    #  @param x The x coord in int
    #  @param y The y coord in int
    #  using the right triangle theory to calculate if the enemy is in range
    #  @return inRange (True if the enemy is in range and false otherwise)
    def isInRangeEquation(self,x,y):
        inRange = ((x-self.x)**2 + (y-self.y)**2 < self.range**2)
        return inRange

    def isInRange(self,bounds):
        x0,x1,y0,y1 = bounds
        if (self.isInRangeEquation(x0,y0) or self.isInRangeEquation(x0,y1) or
            self.isInRangeEquation(x1,y0) or self.isInRangeEquation(x1,y1)):
            return True

        else:
            return False    
    
    def drawTower(self,canvas):#draw dragon once set on board
        gameData.screen.blit(self.img,(self.x-self.size,self.y-self.size))

    def drawRadius(self,canvas):#draws radius sof pokemon
        pygame.draw.circle(canvas,(255,255,255),(self.x,self.y),self.range,2)

    
    def canEvolve(self):#whether pokemon has met conditions to evolve
        if self.upgrade < 3:
            if self.upgrade == 1: #upgrade to level 2 requires 50 money
                if gameData.playerCoins>=50:
                    return True
                    gameData.playerCoins -= 50;
            if self.upgrade == 2: #upgrade to level 3 requires 100 money
                if gameData.playerCoins>=100:
                    return True
                    gameData.playerCoins -= 100;

        
    def evolve(self):#set data for evolution
        if self.canEvolve():
            nextUpgrade = gameData.dragonDatabase[self.index+1]
            self.dragon = nextUpgrade[0]
            self.element = nextUpgrade[1]
            self.baseAttack = nextUpgrade[2]
            self.baseHp = nextUpgrade[3]
            self.upgrade = nextUpgrade[4]
            self.attackGrowth = 10
            self.bounds = None
            self.button = None
            self.index += 1
            self.setSize()
            image = pygame.image.load("img/%s.png" % self.dragon)
            self.img = pygame.transform.scale(image, (30,30))
            self.onBoard = True

