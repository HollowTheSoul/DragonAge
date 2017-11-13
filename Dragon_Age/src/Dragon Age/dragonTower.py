import pygame
import gameData
from dragon import Dragon

## @brief setDragon
    #  @return none
    #  Initiliase the dragons for the game
def setDragons():
    fireDragon =DragonTower(1,gameData.dragonDatabase)
    iceDragon = DragonTower(4,gameData.dragonDatabase)
    poisonDragon = DragonTower(7,gameData.dragonDatabase)
    gameData.dragonParty.append(fireDragon)
    gameData.dragonParty.append(iceDragon)
    gameData.dragonParty.append(poisonDragon)

## @brief Dragon Tower Class
# This class represents the tower that the users will be building. 
# It attackes enemies within range and can be upgraded.
class DragonTower(Dragon):

    ## @brief Dragon Tower __init__ the DragonTower class constructor
    #  @param self
    #  @param dragon Dragon class 
    #  @param dragonDatabase List of information about the dragon
    #  @param level The initial level of the unit
    #  @param x The x coord in int
    #  @param y The y coord in int
    #  @return none
    def __init__(self,dragon,dragonDatabase,level=1,x=None,y=None):
        Dragon.__init__(self,dragon,dragonDatabase)
        self.x = x
        self.y = y
        self.range = dragonDatabase[dragon][5]
        self.counter = self.maxCounter
        self.target = None
        self.bullets = []
        self.onBoard = False
        self.radius = False
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

    ## @brief isInRange calculates whether or not enemy is in range
    #  @param self This is the self
    #  @param bounds the x, y bound of the Tower
    #  @return True if the enemy is in range, False if the enemy is not
    def isInRange(self,bounds):
        x0,x1,y0,y1 = bounds
        if (self.isInRangeEquation(x0,y0) or self.isInRangeEquation(x0,y1) or
            self.isInRangeEquation(x1,y0) or self.isInRangeEquation(x1,y1)):
            return True
        else:
            return False    
    
    ## @brief drawTower draws the tower on the screen
    #  @param self This is the self
    #  @param canvas The game screen
    #  @return none
    def drawTower(self,canvas):#draw dragon once set on board
        gameData.screen.blit(self.img,(self.x-self.size,self.y-self.size))

    ## @brief drawRadius draws the range radius of the tower
    #  @param self This is the self
    #  @param canvas The game screen
    #  @return none
    def drawRadius(self,canvas):#draws radius sof pokemon
        pygame.draw.circle(canvas,(255,255,255),(self.x,self.y),self.range,2)

    ## @brief canUpgrade determines whether the tower can be upgraded
    #  @param self This is the self
    #  @return True if the tower can be upgraded
    def canUpgrade(self):#whether tower can be upgraded
        if self.upgrade < 3:
            if self.upgrade == 1: #upgrade to level 2 requires 50 money
                if gameData.playerCoins>=150:
                    gameData.playerCoins -= 150;
                    return True
                    
            if self.upgrade == 2: #upgrade to level 3 requires 100 money
                if gameData.playerCoins>=300:
                    gameData.playerCoins -= 300;
                    return True

    ## @brief upgrade Upgrade the tower to the next level
    #  @param self This is the self
    #  @return none    
    def upgradeTower(self):#set data for evolution
        if self.canUpgrade():
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
            if self.upgrade == 2:
                self.img = pygame.transform.scale(image, (60,60))
            elif self.upgrade == 3:
                self.img = pygame.transform.scale(image, (90,90))
            
            self.onBoard = True

