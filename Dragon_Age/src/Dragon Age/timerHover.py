import pygame
import gameData
from path import inPlay, onBoard, inParty

#HOVER
def hover():#general hover fucntion wrap
    x,y = pygame.mouse.get_pos()
    if gameData.playerSelected!= None:#put tower on board
        buildTowerHover(x,y) 

def buildTowerHover(x,y):
#draw rect of size of dragon when building if legal
    gameData.playerSelected.x, gameData.playerSelected.y= x,y
    if onBoard(x,y):
        pygame.draw.rect(gameData.screen,(255,255,255),(x-gameData.playerSelected.size,
            y-gameData.playerSelected.size,gameData.playerSelected.size*2,gameData.playerSelected.size*2),
            3)
