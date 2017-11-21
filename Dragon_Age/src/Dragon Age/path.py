import gameData

##  @brief The inPlay function
#   checks if the mouse is in 'play' button bound
#   @return a boolean of whether the mouse is in play bound
def inPlay(x,y):
    x0,y0,x1,y1 = 45,395,105,455
    return x < x1 and x > x0 and y > y0 and y < y1

##  @brief The onBoard function
#   checks if the dragon tower is on board
#   @return a boolean of whether the dragon tower is on board
def onBoard(x,y):
    ax0,ay0,ax1,ay1 = (x-gameData.dragonSize,y-gameData.dragonSize,
        x+gameData.dragonSize,y+gameData.dragonSize)
    bx0,bx1,by0,by1 = gameData.boardBounds
    return ((ax1 > bx0) and (bx1 > ax0) and (ay1 > by0) and (by1 > ay0))

##  @brief The upgradeBound function
#   specify the upgrade button bound on board and checks if
#   the mouse is in button bound
#   @return a boolean of whether the mouse is in button bound
def upgradeBound(x,y):
    x0,y0,x1,y1 = 500,400,800,620
    return x<x1 and x>x0 and y>y0 and y<y1

##  @brief the inTowerBounds
#   make sure tower is not on top of another tower,
#   also know when tower is selected
#   @return the tower or false
def inTowerBounds(bounds):
    bx0,by0,bx1,by1 = bounds
    counter = 1
    for tower in gameData.dragonParty:
        print(counter)
        counter += 1
        ax0,ay0,ax1,ay1 = tower.bounds
        if ((bx0 > ax0) and (bx1 < ax1) and (by0 > ay0) and (by1 < ay1)):
            print ("inside a dragon")
            return tower
    return False

##  @brief the canBuild function
#   checks if tower can build in correct tower bound
#   @return a boolean whether the tower can build in correct tower bound
def canBuild(x,y):
    ax0,ay0,ax1,ay1 = (x-50,y-50,x+50,y+50)
    
    if inTowerBounds((ax0,ay0,ax1,ay1)) == False:
        return True
    return False

##  @brief the inParty function
#   @return return a selected dragon in dragonTower party or return false
def inParty(x,y):
    for dragonTower in gameData.dragonType:
        selectedDragon = dragonTower
        x0,y0,width,height = dragonTower.button
        x1,y1 = x0+width, y0+height
        if x>x0 and x<x1 and y>y0 and y<y1:
            return selectedDragon
    return False

##  @brief the create path function
#   create a path for waking enemy based on a list of corner points of path
#   corresponding to the map and create checkpoints for either horizontal
#   or vertical path
#   @return none
def createPath():
    corners = [(0,80),(185,80),(185,165),(293,165),(293,80),(420,80),
               (420,265),(300,265),(300,450),(420,450),(420,365),
               (535,365),(535,450),(700,450)]
    #adds all x, y positions into new list
    for i in range(1, len(corners)):
        x0,y0 = corners[i-1]
        x1,y1 = corners[i]
        #check if horizontal or veritcal
        if x1 - x0 == 0:
            verticalPath(gameData.checkPoints,x0,y0,x1,y1)
        else:
            horizontalPath(gameData.checkPoints,x0,y0,x1,y1)

##  @brief the create path2 function
#   create a path for flying enemy based on a list of corner points of path
#   corresponding to the map and create checkpoints for either horizontal
#   or vertical path
#   @return none
def createPath2(): #path for flying dragon enemy
    corners = [(0,170),(100,170),(100,300),(170,300),(170,480),
               (700,480)]
    for i in range(1, len(corners)):
        x0,y0 = corners[i-1]
        x1,y1 = corners[i]
        #check if horizontal or veritcal
        if x1 - x0 == 0:
            verticalPath(gameData.checkPoints2,x0,y0,x1,y1)
        else:
            horizontalPath(gameData.checkPoints2,x0,y0,x1,y1)

##  @brief the vertical path function
#   check if two cordinates make a vertical path and append the cordinates
#   every 1 pixel on the path into checkPoints
#   @return none
def verticalPath(checkPoints,x0,y0,x1,y1):
    #distance between 2 corners
    dis = y1 - y0
    for i in range(abs(dis)):
        if dis < 0:
            checkPoints.append((x0,y0-i))
        else:
            checkPoints.append((x0,y0+i))

##  @brief the horizontal path function
#   check if two cordinates make a horizontal path and append the cordinates
#   every 1 pixel on the path into checkPoints
#   @return none
def horizontalPath(checkPoints,x0,y0,x1,y1):
    #distance between 2 corners
    dis = x1 - x0
    for i in range(abs(dis)):
        if dis < 0:
            checkPoints.append((x0-i,y0))
        else:
            checkPoints.append((x0+i,y0))
