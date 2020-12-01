
lines = []
y = 0
trees = {}
with open("input.txt") as fh:
    for line in fh:
        line = line.strip()
        w = len(line)
        for (x, c) in enumerate(line):
            trees[(y, x)] = (c == '#')     
        y += 1
        lines.append(line)

h = len(lines)

def countTrees(dx, dy):
    x = 0
    y = 0
    t = 0
    while y < h:
        if trees[(y, x)]:
            t += 1
        y += dy
        x = (x + dx) % w
    return t
       
p = 1
for (dx, dy) in [(1,1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    c = countTrees(dx, dy)
    print("#", c)
    p *= c

print(p)
