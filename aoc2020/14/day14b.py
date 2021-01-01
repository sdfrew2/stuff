import re
import sys
from collections import defaultdict
MEM = re.compile("^mem\[(.*?)] = (.*)$")
MASK = re.compile("^mask = (.*)$")

def handleMem(m):
    return ("mem", int(m.group(1)), int(m.group(2)))

def parseJokers(s):
    result = [(0, 0)]
    for (i, c) in enumerate(s):
        if s[i] == 'X':
            result2 = []
            for (a, b) in result:
                result2.append((a | (1 << (len(s) - 1- i)), b))
                result2.append((a, b | (1 << (len(s) - 1 -i))))
            result = result2
    return result


def handleMask(m):
    return ("mask", parseBin(m.group(1), "1"), parseJokers(m.group(1)))

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
        maskJokers = [(0, 0)]
        for (cmd, a, b) in me.program:
            if cmd == "mem":
                for joker in maskJokers:
                    address = (a | maskTrue | joker[0]) & ~joker[1] 
                    me.mem[address] = b
            elif cmd == "mask":
                maskTrue = a
                maskJokers = b
        s = 0
        for (k, v) in me.mem.items():
            s += v
        return s

proc = Processor(commands)
print(proc.run())

