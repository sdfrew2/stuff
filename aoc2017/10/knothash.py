




def knothash(bytes):
    buffer = list(range(256))
    skip = 0
    pos = 0
    for l in bytes:
        hl = l // 2
        for i in range(hl):
            left = (pos + i) % 256
            right = (pos + l - 1 - i) % 256
            buffer[left], buffer[right] = buffer[right], buffer[left]
        pos += l + skip
        skip += 1
    return buffer

INPUT = [int(s) for s in open("input.txt", "r").read().strip().split(",")]
h = knothash(INPUT)
print(h[0] * h[1])
