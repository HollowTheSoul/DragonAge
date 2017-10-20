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
        self.attackGrowth = 10
        self.bounds = None
        self.button = None
        self.setSize()
        image = pygame.image.load("%s.png" % self.dragon)
        self.img = pygame.transform.scale(image, (30,30))

    def setSize(self):
        self.size = gameData.dragonSize