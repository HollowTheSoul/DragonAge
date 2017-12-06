import pygame
import gameData

##  @brief The class to create dragon object
class Dragon(object):
    ##  @brief the constructor for Dragon
    #   @param self the self
    #   @param dragon the dragon from the database
    #   @param dragonDatabase the database
    #   @return none
    def __init__(self, dragon, dragonDatabase):
        tup = dragonDatabase[dragon]
        self.dragon = tup[0]
        self.element = tup[1] 
        self.baseAttack = tup[2]
        self.baseHp = tup[3]
        self.upgrade = tup[4]
        self.maxCounter = tup[6] #attack speed, the lower the faster the attack
        self.attackGrowth = 10
        self.bounds = None
        self.button = None
        self.size = gameData.dragonSize
        self.index = dragon
        image = pygame.image.load("img/%s.png" % self.dragon)
        self.img = pygame.transform.scale(image, (40,40))

    ##  @brief set the size of dragon
    #   @param self the self
    #   @param size the size of dragon
    #   @return none
    def setSize(self, size):
        self.size = size

