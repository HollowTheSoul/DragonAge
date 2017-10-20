import gameData

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
