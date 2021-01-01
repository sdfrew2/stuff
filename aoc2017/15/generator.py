MA = 16807
SA = 699
SB = 124
MB = 48271
MOD = 2**31 - 1

def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

def rng(seed, multiplier):
    x = seed
    m = 2**31 - 1
    while True:
        x *= multiplier
        x %= m
        yield x
h = (1 << 16) - 1 
result = 0
for (i, x, y) in zip(range(40000000), rng(SA, MA), rng(SB, MB)):
    if x & h == y & h:
        result += 1

print(result)
