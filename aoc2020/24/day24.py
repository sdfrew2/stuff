import re
import collections
import sys
import copy

DIRECTIONS = re.compile("([ns]?[ew])")

def splitDirections(dirStr):
    return [d for d in re.split(DIRECTIONS, dirStr) if d != '']


# coordinate system: x east, y northeast

coordTable = {
    "e": 1,
    "w": -1,
    "ne": 1+1j,
    "se": -1j,
    "sw": -1-1j,
    "nw": 1j
}

coordTable = {
    "e": 1+0j,
    "w": -1+0j,
    "ne": 1j,
    "sw": -1j,
    "se": 1-1j,
    "nw": -1+1j
}

def neighbors(coord):
    return [v+coord for (k,v) in coordTable.items() ]

def evolveState(state):
    newState = copy.deepcopy(state)
    neighborTable = collections.defaultdict(lambda: 0)
    for (k, v) in state.items():
        if v == 1:
            for neighbor in neighbors(k):
                neighborTable[neighbor] += 1
    for k in set(neighborTable.keys()) | set(state.keys()):
        v = state[k]
        nc = neighborTable[k]
        if v == 0 and nc == 2:
            newState[k] = 1
        if v == 1 and (nc == 0 or nc > 2):
            newState[k] = 0
    return newState



def followDirections(dirs):
    return sum(coordTable[d] for d in dirs)

print(splitDirections("sesenwnenenewseeswwswswwnenewsewsw"))

def main():
    floor = collections.defaultdict(lambda: 0)
    with open(sys.argv[1]) as fh:
        for line in fh:
            line = line.strip()
            target = followDirections(splitDirections(line))
            floor[target] = 1 - floor[target]
    counter = 0 
    for (k, v) in floor.items():
        if v == 1:
            counter += 1
    print(counter)

def main2():
    floor = collections.defaultdict(lambda: 0)
    with open(sys.argv[1]) as fh:
        for line in fh:
            line = line.strip()
            target = followDirections(splitDirections(line))
            floor[target] = 1 - floor[target]
    state = floor
    for i in range(100):
        state = evolveState(state)
        print(sum(v for (k, v) in state.items()))
    print(len(state), len(set(state.keys())))
main2()
