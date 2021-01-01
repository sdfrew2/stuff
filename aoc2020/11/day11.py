import sys
import collections
import copy


def parseState(fh):
    result = []
    for line in fh:
        line = line.strip()
        result.append(list(line))
    return result

def countNeighbors(state, i, j):
    result = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if (dx == 0) and (dy == 0):
                continue
            if not ( 0 <= i + dy < len(state)):
                continue
            if not (0 <= j + dx < len(state[0])):
                continue
            if state[i+dy][j+dx] == '#':
                result += 1
    return result

def evolve(srcState, target):
    for (i, row) in enumerate(srcState):
        for (j, v) in enumerate(row):
            if v == '.':
                continue
            if v == 'L':
                if countNeighbors(srcState, i, j) == 0:
                    target[i][j] = '#'
                else:
                    target[i][j] = 'L'
            if v == '#':
                if countNeighbors(srcState, i, j) >= 4:
                    target[i][j] = 'L'
                else:
                    target[i][j] = '#'



with open(sys.argv[1]) as fh:
    state = parseState(fh)

def countOccupied(state):
    return sum(row.count('#') for row in state)

def run(state):
    a = copy.deepcopy(state)
    b = copy.deepcopy(state)
    changed = True
    k = 0
    while changed:
        k += 1
        print(k)
        evolve(a, b)
        changed = (a != b)
        b, a = a, b
       
    return b



print(countOccupied(run(state)))

