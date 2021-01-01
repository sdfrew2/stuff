N = 16
def composePermutations(p, q):
    result = []
    for i in range(len(p)):
        result.append(q[p[i]])
    return tuple(result)

# dancer -> position



def cycle(dancerpos, k):
    return tuple((p + k) % N for p in dancerpos)

def swapDancers(dancerpos, i, j):
    result = list(dancerpos)
    result[i], result[j] = result[j], result[i]
    return tuple(result)


def swapPositions(dancerpos, i, j):
    swapPerm = list(range(N))
    swapPerm[j] = i
    swapPerm[i] = j
    return composePermutations(dancerpos, swapPerm)

def invert(p):
    result = [0] * len(p)
    for (i, x) in enumerate(p):
        result[x] = i
    return tuple(result)

base = (15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

INPUT = open("input.txt").read().strip().split(",")
def main16():
    dancerpos = tuple(range(N))
    for move in INPUT:
        m0 = move[0]
        if m0 == 's':
            dancerpos = cycle(dancerpos, int(move[1:]))
        elif m0 == 'p':
            first = ord(move[1]) - ord('a')
            second = ord(move[3]) - ord('a')
            dancerpos = swapDancers(dancerpos, first, second)
        elif m0 == 'x':
            parts = move[1:].split("/")
            first = int(parts[0])
            second = int(parts[1])
            dancerpos = swapPositions(dancerpos, first, second)
    result = [0] * N
    for dancer in range(N):
        result[dancerpos[dancer]] = chr(ord('a') + dancer)
    print("".join(result))


def permPower(p, n):
    x = tuple(range(len(p)))
    for i in range(n):
        x = composePermutations(x,p)
    return x

def period(p):
    identity = tuple(range(len(p)))
    currentPerm = identity
    j = 0
    while True:
        currentPerm = composePermutations(currentPerm, p)
        j += 1
        if currentPerm == identity:
            return j


def main16b():
    startPos = list(range(N))
    posPerm = list(range(N))
    for move in INPUT:
        m0 = move[0]
        if m0 == 's':
            posPerm = list(cycle(posPerm, int(move[1:])))
        elif m0 == 'p':
            first = ord(move[1]) - ord('a')
            second = ord(move[3]) - ord('a')
            startPos[first], startPos[second] = startPos[second], startPos[first]
        elif m0 == 'x':
            parts = move[1:].split("/")
            first = int(parts[0])
            second = int(parts[1])
            for i, x in enumerate(posPerm):
                if x == first:
                    posPerm[i] = second
                elif x == second:
                    posPerm[i] = first
    p1 = period(startPos)
    p2 = period(posPerm)
    startPosEx = permPower(startPos, 1000000000 % p1)
    posPermEx = permPower(posPerm,   1000000000 % p2)
    final = composePermutations(startPosEx, posPermEx)
    result = [0]*16
    for dancer in range(16):
        p0 = startPosEx[dancer]
        p1 = posPermEx[p0]
        result[p1] = chr(ord('a') + dancer)
    print("".join(result))




main16b()





