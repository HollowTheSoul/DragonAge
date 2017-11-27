import sys, pygame
from gameManager import gameInit, runGame, mousePress
import gameData
import random

##  @brief initial pygame and load backgound music
#   @return none
def init():
    pygame.init()
    pygame.display.set_caption("Dragon Age")
    gameInit()
    loadBGM()

##  @brief get position of the mouse and pass into mousePress(x,y)
#   @return none
def mouse():
    x, y = pygame.mouse.get_pos()
    if gameData.isIntro:
        mousePress(x,y)    

##  @brief load background(map) of the game
#   @return none
def loadBackground():
    img = pygame.image.load("img/background.png")
    gameData.screen.blit(img, (0,0))


def loadIntro():
    img = pygame.image.load("img/intro.jpg")
    img = pygame.transform.scale(img, (800,620))
    gameData.screen.blit(img, (0,0))
    startButtonImg = pygame.image.load("img/startButton.png")
    startButtonImg = pygame.transform.scale(startButtonImg, (50,50))
    gameData.screen.blit(startButtonImg,(610,370))
    playButton()

def playButton():
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    startButton2Img = pygame.image.load("img/startButton2.png")
    startButton2Img = pygame.transform.scale(startButton2Img, (50,50))
    if 660>cur[0]>610 and 420>cur[1]>370:
        gameData.screen.blit(startButton2Img,[610,370])
        if click[0] == 1:
            gameData.isIntro = False
            gameData.isInGame = True


##  @brief load game over message when game is over
#   @return none
def loadGameOverPage():
    img = pygame.image.load("img/gameOver.png")
    gameData.screen.blit(img, (0, 0))

##  @brief load background music of the game
#   play background music from a list of songs
#   @return none
def loadBGM():
    songs = ['Future - Mask Off.mp3', 'Rich Chigga -Glow like Dat.mp3']
    nextSong = random.choice(songs)
    pygame.mixer.music.load(nextSong)
    pygame.mixer.music.play()

##  @brief the game function
#   The function that load intro, background, gameover and runs the game
#   @return none
def game():
    #intro before init
    init()
    while True:
        if gameData.isIntro == True:
            loadIntro()
        elif gameData.isInGame == True and gameData.isGameOver == False:
            loadBackground()
        elif gameData.isGameOver == True:
            loadGameOverPage()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: mouse()
        runGame()
        pygame.display.flip()

game()
