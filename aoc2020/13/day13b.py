import sys
import collections
import random
import math

with open(sys.argv[1]) as fh:
    lines = fh.readlines()

START = int(lines[0])
BUSES = [(int(busId), i) for (i, busId) in enumerate(lines[1].strip().split(",")) if busId.isnumeric()]

def mergeModEqn(e1, e2):
    (a1, m1) = e1
    (a2, m2) = e2
    if m1 < m2:
        a1, m1, a2, m2 = a2, m2, a1, m1
    z = a1
    while z % m2 != a2:
        z += m1
    return (z % (m1 * m2), m1 * m2)
equations = []
for (busId, i) in BUSES:
    equations.append(((busId - i) % busId, busId))
#random.shuffle(equations)
e = (0, 1)
u = 0
for eq in equations:
    print(u)
    u+=1
    e = mergeModEqn(eq, e)

print(e)


