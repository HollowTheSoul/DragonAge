import gameData

   
#=-------------------------Button bounds--------------------------------------
def inPlay(x,y):
    x0,y0,x1,y1 = 45,395,105,455
    return x < x1 and x > x0 and y > y0 and y < y1

def onBoard(x,y):
    ax0,ay0,ax1,ay1 = (x-gameData.dragonSize,y-gameData.dragonSize,
        x+gameData.dragonSize,y+gameData.dragonSize)
    bx0,bx1,by0,by1 = gameData.boardBounds
    return ((ax1 > bx0) and (bx1 > ax0) and (ay1 > by0) and (by1 > ay0))

def upgradeBound(x,y):#if clicks in upgrade button
    x0,y0,x1,y1 = 500,400,800,620
    return x<x1 and x>x0 and y>y0 and y<y1

def inTowerBounds(bounds): #make sure tower is not on top of another tower, also know when tower is selected
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

def canBuild(x,y):
    ax0,ay0,ax1,ay1 = (x-50,y-50,x+50,y+50)
    
    if inTowerBounds((ax0,ay0,ax1,ay1)) == False:
        return True
    return False

def inParty(x,y):
    for dragonTower in gameData.dragonType:
        selectedDragon = dragonTower
        x0,y0,width,height = dragonTower.button
        x1,y1 = x0+width, y0+height
        if x>x0 and x<x1 and y>y0 and y<y1:
            return selectedDragon
    return False


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

def verticalPath(checkPoints,x0,y0,x1,y1):
    #distance between 2 corners
    dis = y1 - y0
    for i in range(abs(dis)):
        if dis < 0:
            checkPoints.append((x0,y0-i))
        else:
            checkPoints.append((x0,y0+i))

def horizontalPath(checkPoints,x0,y0,x1,y1):
    #distance between 2 corners
    dis = x1 - x0
    for i in range(abs(dis)):
        if dis < 0:
            checkPoints.append((x0-i,y0))
        else:
            checkPoints.append((x0+i,y0))
