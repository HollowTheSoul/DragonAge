import pygame
import gameData


#--------------------------Draw-------------------------------------------
def drawEnemies():
    for enemy in gameData.enemies:
        if enemy.exit == False:
            enemy.drawEnemy(gameData.screen)
    for enemy in gameData.enemies2:
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


def drawStatus(): #draw the status of the tower selected
    color = 255,255,255
    font = pygame.font.Font("pokemon_pixel_font.ttf",20)
    pygame.draw.rect(gameData.screen,color,(690,720,400,500),2)
    if gameData.playerShowStatus!= None:
        dragon = gameData.playerShowStatus
        dragon.drawRadius(gameData.screen)

        name = font.render(dragon.dragon,True,color)
        gameData.screen.blit(name,(690,350))
        level = font.render(("Level: %d" %dragon.upgrade),True,color)
        gameData.screen.blit(level,(690,380))
        attack = font.render(("Attack: %d"%dragon.baseAttack),True,color)
        gameData.screen.blit(attack,(690,410))


def drawGameStats(): #draw the money collected so far
    font = pygame.font.Font("pokemon_pixel_font.ttf",20)
    store = pygame.image.load("img/money.png")
    store = pygame.transform.scale(store, (35,35))
    gameData.screen.blit(store, (680,10))
    money = font.render(str(gameData.playerCoins),True,(255,255,255))
    

    #draw money
    gameData.screen.blit(money,(720,20))

    #draw level
    level = font.render(("Level: %d" %gameData.wave),True,(255,255,255))
    gameData.screen.blit(level,(20,20))

    #draw life
    life = font.render(("Remaining Life: %d" %gameData.life),True,(255,255,255))
    gameData.screen.blit(life,(550,20))

def drawParty():
    startY = 120
    startX = 690
    width = 100
    height = 25
    for i in range(len(gameData.dragonType)):
        dragon = gameData.dragonType[i]#display name of each pokemon
        name = dragon.dragon

        dragonImage = pygame.image.load("img/%sIcon.png" % name)
        dragonImage = pygame.transform.scale(dragonImage, (60,60))
        gameData.screen.blit(dragonImage, (startX+10,startY-30))

        dragon.button = startX,startY,width,height
        if gameData.playerHover == dragon or gameData.playerSelected == dragon:
            pygame.draw.rect(gameData.screen,(255,0,0),(dragon.button),1)
        startY+=80


def drawAllBullets():#draws all bullets on board
    for tower in gameData.dragonParty:
        if tower.onBoard and tower.bullets!=[]:
            for bullet in tower.bullets:
                bullet.drawBullet(gameData.screen)

def drawAll():
    drawTowers()
    drawParty()
    drawAllBullets()
    drawGameStats()
    drawStatus()
    drawEnemies()
