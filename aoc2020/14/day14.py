import re
import sys
from collections import defaultdict
MEM = re.compile("^mem\[(.*?)] = (.*)$")
MASK = re.compile("^mask = (.*)$")

def handleMem(m):
    return ("mem", int(m.group(1)), int(m.group(2)))

def handleMask(m):
    return ("mask", parseBin(m.group(1), "1"), parseBin(m.group(1), "0"))

def parseBin(s, one):
    result = 0
    for c in s:
        if c == one:
            result *= 2
            result += 1
        else:
            result *= 2
    return result



commands = []
with open(sys.argv[1]) as fh:
    for line in fh:
        line = line.strip()
        for (pattern, handler) in [(MEM, handleMem), (MASK, handleMask)]:
            m = pattern.fullmatch(line)
            if m:
                commands.append(handler(m))
                break
           
class Processor:
    def __init__(me, program):
        me.program = program[:]
        me.mem = defaultdict(lambda: 0)

    def run(me):
        maskTrue = 0
        maskFalse = 0
        for (cmd, a, b) in me.program:
            if cmd == "mem":
                me.mem[a] = (b | maskTrue) & ~maskFalse
            elif cmd == "mask":
                maskTrue = a
                maskFalse = b
        s = 0
        for (k, v) in me.mem.items():
            s += v
        return s


proc = Processor(commands)
v = proc.run()
print(v)
