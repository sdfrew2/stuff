import sys

cardkey = 6270530
doorkey = 14540258
modulus = 20201227


# 7**X = c    7**Y = d

def keyiter():
    i = 0
    x = 1
    while True:
        x *= 7
        x %= modulus
        i += 1
        yield (i, x)

def main1():
    cardloop = None
    doorloop = None

    for (i, x) in keyiter():
        if x == doorkey:
            doorloop = i
        if x == cardkey:
            cardloop = i
        if cardloop != None and doorloop != None:
            break

C = 397860
D = 16774995
x = 1

def modpow(x, n, m):
    result = 1
    for i in range(n):
        result *= x
        result %= m
    return result

q = modpow(7, C, modulus)
r = modpow(q, D,modulus)
print(r)

