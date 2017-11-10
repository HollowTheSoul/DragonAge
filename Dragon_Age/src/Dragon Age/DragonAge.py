import sys, pygame
from path import inPlay, onBoard, inParty, evolveBound
from gameManager import gameInit, runGame
import gameData

#--------------------------Init--------------------------------------------
def init():
    pygame.init()
    pygame.display.set_caption("Dragon Age")
    gameInit()

#=-------------------------MousePress--------------------------------------
def mouse():
    x, y = pygame.mouse.get_pos()
    if gameData.isIntro:
        mousePress(x,y)

def mousePress(x,y):
    check = evolveBound(x,y)
    print check
    
    if inPlay(x,y):
        gameData.isPaused = False

    elif inParty(x,y):
        curDragon = inParty(x,y)#current dragon
        if curDragon.onBoard == False:#only in party not on board yet
            gameData.playerSelected = curDragon#pick up pokemon
            gameData.playerSelected.x,gameData.playerSelected.y = x,y
        #already on board, show status
        else: 
            gameData.playerShowStatus = curDragon
            print "hello"
            print gameData.playerShowStatus

    elif gameData.playerSelected!=None:
        #picked up to pokemon to put on board
        if onBoard(x,y):
            gameData.playerSelected.x,gameData.playerSelected.y = x,y
            gameData.playerSelected.bounds = x-10,y-10,x+10,y+10
            gameData.playerSelected.onBoard,gameData.playerSelected =True,None
    
    elif gameData.playerShowStatus!= None and evolveBound(x,y):
        print "evolve"
        (gameData.playerShowStatus).evolve()
    
    

def loadBackground():
    img = pygame.image.load("img/background.png")
    gameData.screen.blit(img, (0,0))

def game():
    init()
    while True:
        if gameData.isIntro == True and gameData.isGameOver == False:
            loadBackground()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: mouse()

        runGame()
        pygame.display.flip()
game()