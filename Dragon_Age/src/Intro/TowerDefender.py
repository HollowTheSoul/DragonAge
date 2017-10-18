import pygame
import time
pygame.init()

display_width = 700
display_height = 510

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHT_GREEN = (0,255,0)

# Load images
towerDefenderImg = pygame.image.load("towerDefender.png")
towerDefenderImg = pygame.transform.scale(towerDefenderImg, (600,200))
backgroundImg = pygame.image.load("background.png")
startButtonImg = pygame.image.load("startButton.png")
startButtonImg = pygame.transform.scale(startButtonImg, (50,50))
startButton2Img = pygame.image.load("startButton2.png")
startButton2Img = pygame.transform.scale(startButton2Img, (50,50))




gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Tower Defender")
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


block_size = 10
FPS = 30
font = pygame.font.SysFont(None,25)

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Define functions
def message_to_screen(msg,color,x,y):
    screen_text = font.render(msg,True,color)
    gameDisplay.blit(screen_text,[x,y])

def button(x,y,width,height):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width>cur[0]>x and y+height>cur[1]>y:
        gameDisplay.blit(startButton2Img,[610,350])
        if click[0] == 1:
            quit()  

# Set the interfaces
def introduction():
    gameDisplay.blit(towerDefenderImg,(40, 150))
    
def start():
    gameDisplay.blit(startButtonImg,(610,350))

    

# Define all botton bounds
  
    
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        
            done = True

        
        
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.

    gameDisplay.blit(backgroundImg,[0,0])
    introduction()
    start()
    message_to_screen("Press green button to start play!",RED,400,480)

    button(610,350,50,50)
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
quit()

