import itertools
import collections
import sys

deltas = [c for c in itertools.product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1]) if c != (0, 0, 0, 0)]

def countNeighbors(state):
    result = collections.defaultdict(lambda: 0)
    for (x, y, z, w) in state:
        for (dx, dy, dz, dw) in deltas:
            result[(x+dx, y+dy, z+dz, w+dw)] += 1
    return result

def evolve(state):
    nb = countNeighbors(state)
    result = set()
    for (p, count) in nb.items():
        if count == 3 or (count == 2 and p in state):
            result.add(p)
    return result 

def parseState(fh):
    result = set()
    for (y, line) in enumerate(fh):
        for (x, c) in enumerate(line.strip()):
            if c == '#':
                result.add((x,y,0, 0))
    return result

with open(sys.argv[1]) as fh:
    state = parseState(fh)
    for i in range(6):
        state = evolve(state)
    print(len(state))
