import sys
from collections import defaultdict

def readBlocks(fh):
    block = []
    for line in fh:
        line = line.strip()
        if len(line) == 0:
            yield block
            block = []
        else:
            block.append(line)
    if len(block) > 0:
        yield block

def blockValue(block):
    checked = set()
    for line in block:
        for c in line:
            checked.add(c)
    return len(checked)


s = 0
with open(sys.argv[1]) as fh:
    for block in readBlocks(fh):
        v = blockValue(block)
        print("BV", v)
        s += v

print("TOTAL", s)
