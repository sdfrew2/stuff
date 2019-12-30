




def knothash(s):
    buffer = list(range(256))
    skip = 0
    pos = 0
    bytes = [ord(c) for c in s]
    bytes += [17, 31, 73, 47, 23]
    for round in range(64):
        for l in bytes:
            hl = l // 2
            for i in range(hl):
                left = (pos + i) % 256
                right = (pos + l - 1 - i) % 256
                buffer[left], buffer[right] = buffer[right], buffer[left]
            pos += l + skip
            skip += 1
    hexparts = []
    for i in range(16):
        xsum = 0
        for j in range(16):
            xsum ^= buffer[16 * i + j]
        hexpart = hex(xsum)[2:].rjust(2, "0")
        hexparts.append(hexpart)
    return "".join(hexparts)

INPUT =open("input.txt", "r").read().strip()
h = knothash(INPUT)
print(h)
