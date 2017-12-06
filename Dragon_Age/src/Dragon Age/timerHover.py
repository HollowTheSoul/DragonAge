import pygame
import gameData
from path import inPlay, onBoard, inParty
from timerEnemy import removeAllEnemies

##  @brief general hover function wrap
#   @return none
def hover():
    x,y = pygame.mouse.get_pos()
    if gameData.playerSelected!= None:#put tower on board
        buildTowerHover(x,y) 

##  @brief draw rect of size of dragon when building if legal
#   @return none
def buildTowerHover(x,y):
    gameData.playerSelected.x, gameData.playerSelected.y= x,y
    if onBoard(x,y):
        pygame.draw.rect(gameData.screen,(255,255,255),(x-gameData.playerSelected.size,
            y-gameData.playerSelected.size,gameData.playerSelected.size*2,gameData.playerSelected.size*2),
            3)

##  @brief remove all enemies when life is 0
#   @return none
def gameoverHover():
    if gameData.life == 0:
        removeAllEnemies()
        
