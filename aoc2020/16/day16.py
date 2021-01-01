
import sys

def readBlocks(fh):
    lines = []
    for line in fh:
        line = line.strip()
        if line == '':
            yield lines
            lines = []
        else:
            lines.append(line)
    if len(lines) > 0:
        yield lines

def parseTicket(line):
    return [int(s) for s in line.split(",")]

def parseRule(line):
    (lhs, rhs) = line.split(":")
    field = lhs
    rangeStrs = rhs.strip().split(" or ")
    ranges = []
    for rangeStr in rangeStrs:
        parts = rangeStr.split("-")
        smin = int(parts[0])
        smax = int(parts[1])
        ranges.append((smin, smax))
    return (field, ranges)

with open(sys.argv[1]) as fh:
    blocks = list(readBlocks(fh))
    
    
rules = [parseRule(line) for line in blocks[0]]
myTicket = parseTicket(blocks[1][1])
otherTickets = [parseTicket(line) for line in blocks[2][1:]]

def checkRule(rule, value):
    for (a, b) in rule[1]:
        if a <= value <= b:
            return True
    return False

def checkAnyRule(rules, value):
    return any(checkRule(r, value) for r in rules)


score = 0
for ticket in otherTickets:
    for value in ticket:
        if not checkAnyRule(rules, value):
            score += value

print(score)




