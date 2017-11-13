import pygame
import math
import gameData

class Bullet(object):
    def __init__(self,x,y,target,element,upgrade):
        self.targetX,self.targetY=target
        self.x = x
        self.y = y
        self.bounds = x-5,y-5,x+5,y+5
        self.remove = False #if hits something
        self.getDirection()
        self.speed = 20 #speed of bullet
        self.upgrade = upgrade
        self.setImage(element)
        self.element = element
        

    def setImage(self,element):#bullet img set based on element of tower
        image = pygame.image.load("img/%s.png" % element)
        if self.upgrade == 1:
            self.img = pygame.transform.scale(image, (15,15))
        elif self.upgrade == 2:
            self.img = pygame.transform.scale(image, (30,15))
        elif self.upgrade == 3:
            self.img = pygame.transform.scale(image, (45,30))

    def getDirection(self):
    #find direction of bullet in radians with given target
        dx = self.targetX-self.x
        dy = self.targetY-self.y
        rads = math.atan2(dy,dx)
        rads %= 2*math.pi
        self.dir = rads # in radians

    def shotEnemy(self,enemy):
        #whether the bullet intersects with an enemy bound
        (ax0, ay0, ax1, ay1) = self.bounds
        (bx0, by0, bx1, by1) = enemy.bounds
        return ((ax1 > bx0) and (bx1 > ax0) and (ay1 > by0) and (by1 > ay0))

    def moveBullet(self):
        #move bullet according to direction
        self.x += int(round(math.cos(self.dir)*self.speed))
        self.y += int(round(math.sin(self.dir)*self.speed))
        self.bounds = self.x-5,self.y-5,self.x+5,self.y+5

    def drawBullet(self,canvas):#draws bullet on canvas
        canvas.blit(self.img,(self.x,self.y))