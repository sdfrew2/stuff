
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

def fieldCandidatesSingle(value):
    return set(i for (i, rule) in enumerate(rules) if checkRule(rule, value))


def fieldCandidatesList(values):
    result = set(range(len(rules)))
    for v in values:
        result &= fieldCandidatesSingle(v)
    return result

def fieldCandidatesColumn(tickets, i):
    return fieldCandidatesList(ticket[i] for ticket in tickets)

def isValidTicket(ticket):
    for value in ticket:
        if not checkAnyRule(rules, value):
            return False
    return True

validTickets = []
for ticket in otherTickets:
    if isValidTicket(ticket):
        validTickets.append(ticket)
if isValidTicket(myTicket):
    validTickets.append(myTicket)

departureRules = [i for (i, rule) in enumerate(rules) if rule[0].startswith("departure")]
coll = []
for j in range(len(validTickets[0])):
    coll.append((j,fieldCandidatesColumn(validTickets, j)))
coll.sort(key=lambda z: len(z[1]))
print([len(z[1]) for z in coll])
print(departureRules)
coll = [(-1, set())] + coll
fieldRules = [(coll[j][0], coll[j][1] - coll[j-1][1]) for j in range(1, len(coll))]
result = 1
for (f, rs) in fieldRules:
    r = next(iter(rs))
    if r in departureRules:
        result *= myTicket[f]
print(result)











