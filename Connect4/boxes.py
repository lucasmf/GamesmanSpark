import gamesman as G


line = 3
column = 3
gameSize = line * column
gridSize = gameSize ** 2

pont1Pos = gridSize
pont2Pos = gridSize+1

initialPosition = gridSize *"0" + 2*"0"
initialGrid = gridSize *"0" + 2*"0"

def pos(i, j): 
    return i*column + j

def edge(pos1, pos2):
    return pos1*gameSize + pos2

def primitive(position):
    flag = True
    for idx in xrange(gameSize):
        if idx%column != column-1:
            if position[edge(idx, idx+1)] == "0":
                flag = False
        if idx < (line-1)*column:
            if position[edge(idx, idx+column)] == "0":
                flag = False
    #if(flag):
        #print position           
    if flag and (position[pont1Pos] > position[pont2Pos]):
        #print position
        return G.WIN
    elif flag and (position[pont1Pos] < position[pont2Pos]):
        #print position
        return G.LOSE
    elif flag:
        return G.TIE
    else: 
        return G.UNDECIDED

def generateMoves(position):
    ret = []
    for idx in xrange(gameSize):
        if idx%column != column-1:
            if position[edge(idx,idx+1)]=="0":
                ret.append((idx, idx+1))
        if idx < (line-1)*column:
            if position[edge(idx, idx+column)]=="0":
                ret.append((idx, idx+column))
    return ret

def doMove(position, move):
    position = position[0:edge(move[0], move[1])]+"1"+position[edge(move[0], move[1])+1:]
    if move[1] == move[0]+1:
        down1 = move[0] + column
        down2 = move[1] + column
        if position[edge(move[0],down1)] =="1" and position[edge(move[1],down2)] == "1" and position[edge(down1,down2)] == "1":
            position = position[0:gridSize]+chr(ord(position[pont1Pos])+1)+position[pont2Pos:]
        up1 = move[0] - column
        up2 = move[1] - column
        if position[edge(up1,move[0])] =="1" and position[edge(up2,move[1])] == "1" and position[edge(up1,up2)] == "1":
            position = position[0:gridSize]+chr(ord(position[pont1Pos])+1)+position[pont2Pos:]
                          
    elif move[1] == move[0] + column:
        right1 = move[0] + 1
        right2 = move[1] + 1
        if position[edge(move[0],right1)] =="1" and position[edge(move[1],right2)] == "1" and position[edge(right1,right2)] == "1":
            position = position[0:gridSize]+chr(ord(position[pont1Pos])+1)+position[pont2Pos:]
        left1 = move[0] - 1
        left2 = move[1] - 1
        if position[edge(left1,move[0])] =="1" and position[edge(left2,move[1])] == "1" and position[edge(left1,left2)] == "1":
            position = position[0:gridSize]+chr(ord(position[pont1Pos])+1)+position[pont2Pos:]
    else:
        var = position[pont1Pos]
        position[pont1Pos] = position[0:gridSize]+position[pont2Pos]+position[var]
    return position

def solve(position=initialGrid):
    if primitive(position) != G.UNDECIDED:
        return primitive(position)
    else:
        moves = generateMoves(position)

        positions = [doMove(position, move) for move in moves]
        
        values = [solve(pos) for pos in positions]
        
        if G.LOSE in values:
            return G.WIN
        elif G.TIE in values:
            return G.TIE
        else:
            return G.LOSE
                           
    
