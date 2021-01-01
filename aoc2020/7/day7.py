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

containedIn = defaultdict(lambda: set())
for (lhs, rhs) in rules.items():
    for (n, col) in rhs:
        containedIn[col].add(lhs)

def reachable(graph, start):
    visited = set()
    frontier = [start]
    while len(frontier) > 0:
        node = frontier.pop()
        if node in visited:
            continue
        visited.add(node)
        for col in graph[node]:
            frontier.append(col)
    return visited





l = reachable(containedIn, "shiny gold")
print(len(l) - 1)
