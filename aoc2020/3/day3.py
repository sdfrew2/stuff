
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
x = 0
y = 0
t = 0
while y < h:
    if trees[(y, x)]:
        t += 1
    y += 1
    x = (x + 3) % w
   
print(t)
