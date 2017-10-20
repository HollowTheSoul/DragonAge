import pygame
import gameData

#--------------------------Draw-------------------------------------------
def drawIntro():
    img = pygame.image.load("img/Intro.png")
    gameData.screen.fill((255,255,255))
    img = pygame.transform.scale(img, (500,250))
    gameData.screen.blit(img, (0,0))

def drawEnemies():
    for enemy in gameData.enemies:
        if enemy.exit == False:
            enemy.drawEnemy(gameData.screen)

def drawPlay():
    x0,y0 = 50, 400
    width, height = 70, 70
    img = pygame.image.load("img/play.png")
    img = pygame.transform.scale(img, (50,50))
    gameData.screen.blit(img, (x0, y0))

def drawTowers():#draw all towers on board
    for dragon in gameData.dragonParty:
        if dragon.onBoard == True:
            dragon.drawTower(gameData.screen)

def drawParty():
    startY =60
    startX = 690
    width = 100
    height = 25
    font = pygame.font.Font("pokemon_pixel_font.ttf",20)
    for i in range(len(gameData.dragonParty)):
        dragon = gameData.dragonParty[i]#display name of each pokemon
        name = dragon.dragon
        dragon.button = startX,startY,width,height
        if gameData.playerHover == dragon or gameData.playerSelected == dragon:
            # pygame.draw.rect(gameData.screen,(255,0,0),(dragon.button),1)
            dragon.drawRadius(gameData.screen)
        name = font.render(name,True,(255,255,255))
        gameData.screen.blit(name,(startX+5,startY+5))
        startY+=25

def drawAllBullets():#draws all bullets on board
    for tower in gameData.dragonParty:
        if tower.onBoard and tower.bullets!=[]:
            for bullet in tower.bullets:
                bullet.drawBullet(gameData.screen)

def drawAll():
    drawEnemies()
    drawPlay()
    drawTowers()
    drawParty()
    drawAllBullets()