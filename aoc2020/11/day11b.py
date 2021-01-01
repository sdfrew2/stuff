import sys
import collections
import copy


def parseState(fh):
    result = []
    for line in fh:
        line = line.strip()
        result.append(list(line))
    return result


        

def findSeat(state, y, x, dy, dx):
    for i in range(1, 1000):
        sx = x + i * dx
        sy = y + i * dy
        if not (0 <= sy < len(state)):
            break
        if not (0 <= sx  < len(state[0])):
            break
        if state[sy][sx] != '.':
            return (sy, sx)
    return None

def findSeats(state, y, x):
    result = []
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dx == dy == 0:
                continue
            s = findSeat(state, y, x, dy, dx)
            if s != None:
                result.append(s)
    return result

def makeNeighborTable(state):
    result = {}
    for i in range(len(state)):
        for j in range(len(state[0])):
            ns = findSeats(state, i, j)
            result[(i, j)] = ns
    return result 

def countNeighbors(state, nt, i, j):
    result = 0
    for (y, x) in nt[(i, j)]:
        if state[y][x] == '#':
            result += 1
    return result

def evolve(nt, srcState, target):
    for (i, row) in enumerate(srcState):
        for (j, v) in enumerate(row):
            if v == '.':
                continue
            if v == 'L':
                if countNeighbors(srcState, nt, i, j) == 0:
                    target[i][j] = '#'
                else:
                    target[i][j] = 'L'
            if v == '#':
                if countNeighbors(srcState, nt, i, j) >= 5:
                    target[i][j] = 'L'
                else:
                    target[i][j] = '#'



with open(sys.argv[1]) as fh:
    state = parseState(fh)

def countOccupied(state):
    return sum(row.count('#') for row in state)

def run(state):
    nt = makeNeighborTable(state)
    a = copy.deepcopy(state)
    b = copy.deepcopy(state)
    changed = True
    k = 0
    while changed:
        k += 1
        print(k)
        evolve(nt, a, b)
        changed = (a != b)
        b, a = a, b
       
    return b



print(countOccupied(run(state)))

