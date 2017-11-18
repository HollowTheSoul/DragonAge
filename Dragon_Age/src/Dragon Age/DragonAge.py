import sys, pygame
from gameManager import gameInit, runGame, mousePress
import gameData
import random

#--------------------------Init--------------------------------------------
def init():
    pygame.init()
    pygame.display.set_caption("Dragon Age")
    gameInit()
    loadBGM()

#=-------------------------MousePress--------------------------------------
def mouse():
    x, y = pygame.mouse.get_pos()
    if gameData.isIntro:
        mousePress(x,y)    

def loadBackground():
    img = pygame.image.load("img/background.png")
    gameData.screen.blit(img, (0,0))

def loadGameOverPage():
    img = pygame.image.load("img/gameOver.png")
    gameData.screen.blit(img, (170, 150))

def loadBGM():
    songs = ['Future - Mask Off.mp3', 'Rich Chigga -Glow like Dat.mp3']
    nextSong = random.choice(songs)
    pygame.mixer.music.load(nextSong)
    pygame.mixer.music.play()

def game():
    init()
    while True:
        if gameData.isIntro == True and gameData.isGameOver == False:
            loadBackground()
        elif gameData.isGameOver == True:
            loadGameOverPage()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: mouse()
            
        runGame()
        pygame.display.flip()
game()
