
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

print(max(seatId(seatCoord(p)) for p in codes))


