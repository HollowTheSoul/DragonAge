import pygame
import math
import gameData

##  @brief this is the class to create bullet object
#   @return none
class Bullet(object):
    
    ##  @brief the constructor of the class
    #   @param self the self
    #   @param x x-coord of bullet
    #   @param y y-coord of bullet
    #   @param target coord of target
    #   @param upgrade number of upgrade of dragon tower
    def __init__(self,x,y,target,element,upgrade):
        self.targetX,self.targetY=target
        self.x = x
        self.y = y
        self.bounds = x-5,y-5,x+5,y+5
        self.remove = False #if hits something
        self.getDirection()
        self.speed = 20
        self.upgrade = upgrade
        self.setImage(element)
        self.element = element
        
    ##  @brief set image of bullet
    #   @param self the self
    #   @param element the element of dragon tower
    #   bullet img set based on element of tower
    #   @return none
    def setImage(self,element):
        image = pygame.image.load("img/%s.png" % element)
        if self.upgrade == 1:
            self.img = pygame.transform.scale(image, (15,15))
        elif self.upgrade == 2:
            self.img = pygame.transform.scale(image, (30,15))
        elif self.upgrade == 3:
            self.img = pygame.transform.scale(image, (45,30))

    ##  @brief get direction of bullet
    #   @param self the self
    #   find direction of bullet in radians with given target
    def getDirection(self):
        dx = self.targetX-self.x
        dy = self.targetY-self.y
        rads = math.atan2(dy,dx)
        rads %= 2*math.pi
        self.dir = rads # in radians

    ##  @brief check if the bullet hit enemy
    #   @param self the self
    #   @param enemy the enemy object
    #   @return the boolean of whether the bullet intersects with an enemy bound
    def shotEnemy(self,enemy):
        (ax0, ay0, ax1, ay1) = self.bounds
        (bx0, by0, bx1, by1) = enemy.bounds
        return ((ax1 > bx0) and (bx1 > ax0) and (ay1 > by0) and (by1 > ay0))

    ##  @brief move the bullet
    #   @param self the self
    #   move the bullet according to the direction
    def moveBullet(self):
        self.x += int(round(math.cos(self.dir)*self.speed))
        self.y += int(round(math.sin(self.dir)*self.speed))
        self.bounds = self.x-5,self.y-5,self.x+5,self.y+5

    ##  @brief darw bullet
    #   @param self the self
    #   @param canvas the screen
    #   draw bullets on canvas
    def drawBullet(self,canvas):
        canvas.blit(self.img,(self.x,self.y))
