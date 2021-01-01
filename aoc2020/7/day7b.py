from collections import defaultdict
import sys

def parseRule(line):
    line = line.replace(".", "")
    line = line.replace("bags", "")
    line = line.replace("bag", "")
    tokens = line.split("contain")
    lhs = tokens[0].strip()
    rightPart = tokens[1].strip()
    tokens = rightPart.split(",")
    rhs = []
    if "no " in rightPart:
        return (lhs, rhs)
    for token in tokens:
        components = token.split()
        count = int(components[0])
        bagtype = components[1] + " " + components[2]
        rhs.append((count, bagtype))
    return (lhs, rhs)



rules = {}
with open(sys.argv[1]) as fh:
    for line in fh:
        line = line.strip()
        rule = parseRule(line)
        rules[rule[0]] = rule[1]

costCache = {}
def cost(color):
    if color in costCache:
        return costCache[color]
    rule = rules[color]
    result = 1
    for (n, othercol) in rule:
        result += n*cost(othercol)
    costCache[color] = result
    return result




l = cost("shiny gold") - 1
print(l)
