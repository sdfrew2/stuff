import itertools
import sys

with open("input.txt") as fh:
    codes = [line.strip() for line in fh]

def parseBinary(s, one, zero):
    result = 0
    for c in s:
        if c == one:
            result = 2*result + 1
        elif c == zero:
            result = 2*result
    return result

def seatCoord(p):
    row = parseBinary(p, "B", "F")
    col = parseBinary(p, "R", "L")
    return (row, col)

def seatId(co):
    return 8*co[0] + co[1]

occupied = set(seatCoord(p) for p in codes)
for row in range(128):
    print(row, end="")
    for col in range(8):
        c = '.'
        if (row, col) in occupied:
            c = '#'
        print(c, sep="",end="")
    print()
