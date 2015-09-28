import gamesman as G

initialPosition = 16 *"0" + 2*"0"
initialGrid = 16 *"0" + 2*"0"
#2*2*2*2 grid + pointsA + pointsB
def primitive(position):
    flag = position[1] == "1" and position[2] == "1" and position[7] == "1" and position[11] == "1"
    print flag
    if flag and position[16] > position[16+1]:
        return G.WIN
    elif flag and position[16] < position[16+1]:
        return G.LOSE
    elif flag:
        return G.TIE
    else:
        return G.UNDECIDED

def generateMoves(position):
    ret = []
    for idx in xrange(4):
        if idx%2 != 1:
            if position[idx*4+idx+1]=="0":
                ret.append((idx, idx+1))
        if idx < 2 :
            if position[idx*4+idx+2]=="0":
                ret.append((idx, idx+2))
    print ret
    return ret

def doMove(position, move):
    position = position[0:move[0]*4+move[1]]+"1"+position[move[0]*4+move[1]+1:]
    if move[1] == move[0]+1:
        down1 = move[0] + 2
        down2 = move[1] + 2
        if position[move[0] * 4 + down1] =="1" and position[move[1] * 4 + down2] == "1" and position[down1 * 4 + down2] == "1":
            position = position[0:16]+chr(ord(position[16])+1)+position[17:]
        up1 = move[0] - 2
        up2 = move[1] - 2
        if position[up1 * 4 + move[0]] =="1" and position[up2 * 4 + move[1]] == "1" and position[up1 * 4 + up2] == "1":
            position = position[0:16]+chr(ord(position[16])+1)+position[17:]
                          
    elif move[1] == move[0]+2:
        right1 = move[0] + 1
        right2 = move[1] + 1
        if position[move[0] * 4 + right1] =="1" and position[move[1] * 4 + right2] == "1" and position[right1 * 4 + right2] == "1":
            position = position[0:16]+chr(ord(position[16])+1)+position[17:]
        left1 = move[0] - 1
        left2 = move[1] - 1
        if position[left1 * 4 + move[0]] =="1" and position[left2 * 4 + move[1]] == "1" and position[left1 * 4 + left2] == "1":
            position = position[0:16]+chr(ord(position[16])+1)+position[17:]
    else:
        var = position[16]
        position[16] = position[0:16]+position[16+1]+position[var]
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
                           
    
