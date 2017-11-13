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
    store = pygame.image.load("img/store.png")
    store = pygame.transform.scale(store, (35,35))
    gameData.screen.blit(store, (680,20))
    money = font.render(str(gameData.playerCoins),True,(255,255,255))
    text = "Money:"
    moneySymbol = font.render(text,True,(255,255,255))
    gameData.screen.blit(money,(760,35))
    gameData.screen.blit(moneySymbol,(720,35))
    level = font.render(("Level: %d" %gameData.wave),True,(255,255,255))
    gameData.screen.blit(level,(20,20))
    life = font.render(("Remaining Life: %d" %gameData.life),True,(255,255,255))
    gameData.screen.blit(life,(560,470))
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