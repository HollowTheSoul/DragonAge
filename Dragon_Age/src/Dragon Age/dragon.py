import pygame
import gameData

class Dragon(object):
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
        self.setSize()
        self.index = dragon
        image = pygame.image.load("img/%s.png" % self.dragon)
        self.img = pygame.transform.scale(image, (40,40))

    def setSize(self):
        self.size = gameData.dragonSize

