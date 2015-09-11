asdfimport gamesman as G

initialPosition = 0
initialGrid = 16 *"0"

def primitive(position):
    if position == 10:
        return G.LOSE
    else:
        return G.UNDECIDED

def generateMoves(position):
    ret = []
    for idx in xrange(4):
        if idx%2 != 1:
            if position[idx*4+idx+1]=="0":
                ret.append((idx, idx+1)
        if idx < 2:
            if position[idx*4+idx+2]=="0":
                ret.append((idx, idx+2))

def doMove(position, move):
    return position[move] = "1"

def solve(position=initiaGrid, numMoves = 0, pointsA = 0, pointsB = 0):
    if primitive(position) != G.UNDECIDED:
        return primitive(position, pointsA, pointsB)
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
