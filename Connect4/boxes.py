import gamesman as G

line = int(raw_input("Number of lines:\n"))
column = int(raw_input("Number of columns:\n"))
gameSize = line * column
gridSize = gameSize ** 2

pont1Pos = gridSize
pont2Pos = gridSize+1
turnBit = gridSize+2
initialPosition = gridSize *"0" + 2*"0" + "0" 
#initialPosition =initialPosition[0:7] + "1" + initialPosition[8:]

def pos(i, j):
    return i*column + j

def edge(pos1, pos2):
    return pos1*gameSize + pos2

def hasEdge(pos1, pos2, p):
    return p[edge(pos1, pos2)] == "1"

def printInitialBoard():
    for i in xrange(line):
        ret = ""
        if i > 0:
            for j in xrange(column):
                if j > 0:
                    ret += "  " 
                if hasEdge(pos(i-1, j), pos(i, j), initialPosition):
                    ret += "| "
                else:
                    ret += "  "
        print ret


        ret = ""
        for j in xrange(column):
            idx = pos(i, j)
            if j == 0:
                if idx < 10:
                    ret += "0"
                ret += str(pos(i, j))
            else:
                if hasEdge(pos(i, j-1), pos(i, j), initialPosition):
                    ret += "--" 
                    if idx < 10:
                        ret += "0"
                    ret += str(pos(i, j))
                else:
                    ret += "  "
                    if idx < 10:
                        ret += "0"
                    ret += str(pos(i, j))
        print ret
    print


print("Your board will look like this one:")
printInitialBoard()

while(True):
    s = raw_input("Type two numbers to add an edge between the two corresponding numbers to the initial board or q(uit) to solve):")
    if s == "q" or s == "quit":
        break
    numbers = s.split()
    initialPosition = initialPosition[:edge(int(numbers[0]), int(numbers[1]))] + "1" + initialPosition[edge(int(numbers[0]), int(numbers[1]))+1:]
    print("Your board looks like this:")
    printInitialBoard()



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
        position = position[0:gridSize]+position[pont2Pos]+position[var:]
        if position[turnBit] == "0":
            position = position[:turnBit] + "1"
        else:
            position = position[:turnBit] + "0"
    return position

def solve(position=initialPosition):
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
