from collections import deque
INPUT = "hxtvlmkl"

def knothash(s):
    buffer = list(range(256))
    skip = 0
    pos = 0
    bytes = [ord(c) for c in s]
    bytes += [17, 31, 73, 47, 23]
    for round in range(64):
        for l in bytes:
            hl = l // 2
            for i in range(hl):
                left = (pos + i) % 256
                right = (pos + l - 1 - i) % 256
                buffer[left], buffer[right] = buffer[right], buffer[left]
            pos += l + skip
            skip += 1
    hexparts = []
    for i in range(16):
        xsum = 0
        for j in range(16):
            xsum ^= buffer[16 * i + j]
        hexpart = hex(xsum)[2:].rjust(2, "0")
        hexparts.append(hexpart)
    return "".join(hexparts)

def bitcount(x):
    if x == 0:
        return 0
    if x % 2 == 0:
        return bitcount(x // 2)
    else:
        return bitcount(x // 2) + 1

def bits(x):
    result = []
    for i in range(4):
        result.append(x % 2)
        x //= 2
    result.reverse()
    return result
   
def neighbors(p):
    (x, y) = p
    return [(x-1, y), (x+1, y), (x,y-1), (x,y+1) ] 

def main14():
    hexval = {}
    for (i, c) in enumerate("0123456789abcdef"):
        hexval[c] = i
    numbits = 0
    ones = set()
    for row in range(128):
        valueToHash = INPUT + "-" + str(row)
        h = knothash(valueToHash)
        column = 0
        for d in h:
            value = hexval[d]
            for b in bits(value):
                if b == 1:
                    ones.add((row, column))
                column += 1
    regions = {}
    regionNum = 0
    for row in range(128):
        for column in range(128):
            p = (row, column)
            if p in ones:
                if p in regions:
                    continue
                regionNum += 1
                ffq = deque()
                ffq.append(p)
                while len(ffq) > 0:
                    elem = ffq.popleft()
                    if elem in regions or not (elem in ones):
                        continue
                    regions[elem] = regionNum
                    for q in neighbors(elem):
                        (row2, col2) = q
                        if 0 <= row2 < 128 and 0 <= col2 < 128:
                            ffq.append((row2, col2))
    print(len(set(regions.values())))
                    
                

main14()
