import sys
import copy
from functools import lru_cache
import itertools
def chunks(fh):
    chunk = []
    for line in fh:
        line = line.strip()
        if line == "":
            yield chunk
            chunk = []
        else:
            chunk.append(line)
    if len(chunk) > 0:
        yield chunk

def pixelRotate(pic):
    m = len(pic) - 1
    result = copy.deepcopy(pic)
    for y in range(len(pic)):
        for x in range(len(pic)):
            result[y][m-x] = pic[x][y]
    return result

def pixelFlip(pic):
    m = len(pic) - 1
    result = copy.deepcopy(pic)
    for y in range(len(pic)):
        for x in range(len(pic)):
            result[m-x][y] = pic[x][y]
    return result

def matchHorizontal(pic1, pic2):
    for y in range(len(pic1)):
        if pic1[-1][y] != pic2[0][y]:
            return False
    return True

def matchVertical(pic1, pic2):
    for x in range(len(pic1)):
        if pic1[x][-1] != pic2[x][0]:
            return False
    return True

def orientations(picture):
    for i in range(4):
        yield picture
        picture = pixelRotate(picture)
    picture = pixelFlip(picture)
    for i in range(4):
        yield picture
        picture = pixelRotate(picture)

PICS = {}

with open(sys.argv[1]) as fh:
    for chunk in chunks(fh):
        key = int(chunk[0].split(" ")[-1][:-1])
        size = len(chunk) - 1
        picture = [[None] * size for y in range(size)]
        for (y, line) in enumerate(chunk[1:]):
            for (x, c) in enumerate(line):
                picture[x][y] = c
        PICS[key] = picture

ORI_PICS = {}
for (k, pic) in PICS.items():
    ORI_PICS[k] = list(orientations(pic))

def checkPiece(board, x, y, piece, orientation):
    if x > 0 and not matchHorizontalIx(board[x-1][y], (piece, orientation)):
        return False
    if y > 0 and not matchVerticalIx(board[x][y-1], (piece, orientation)):
        return False
    return True

@lru_cache(maxsize=None)
def matchHorizontalIx(po1, po2):
    (p1, o1) = po1
    (p2, o2) = po2
    return matchHorizontal(ORI_PICS[p1][o1], ORI_PICS[p2][o2])

@lru_cache(maxsize=None)
def matchVerticalIx(po1, po2):
    (p1, o1) = po1
    (p2, o2) = po2
    return matchVertical(ORI_PICS[p1][o1], ORI_PICS[p2][o2])


def search(board, positions, piecesLeft):
    if len(positions) == 0:
        yield board
    (x, y) = positions.pop()
    for piece in piecesLeft:
        for orientation in range(8):
            if checkPiece(board, x, y, piece, orientation):
                piecesLeft.remove(piece)
                board[x][y] = (piece, orientation)
                for solution in search(board, positions, piecesLeft):
                    yield solution
                board[x][y] = None
                piecesLeft.add(piece)
    positions.append((x, y))
        
def diagonalPositions(n):
    result = list(itertools.product(range(n), range(n)))
    result.sort(key=lambda p: (p[0] + p[1], p[0]))
    result.reverse()
    return result



def main():
    board = [[None] * 12 for y in range(12)]
    for sol in search(board, diagonalPositions(12), set(PICS.keys())):
        a = sol[0][0][0]
        b = sol[0][-1][0]
        c = sol[-1][0][0]
        d = sol[-1][-1][0]
        print(a*b*c*d)



