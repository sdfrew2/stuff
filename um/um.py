import sys

REG = 7
REG_C = REG
REG_B = REG << 3
REG_A = REG << 6
OP = 15 << 28
LD_A = REG << 25 
LD_VAL = (1 << 25) - 1
WORD = (1 << 32) - 1
def decode_regs(word):
    return ((word & REG_A) >> 6, (word & REG_B) >> 3, (word & REG_C))

def read_program(filename):
    data = []
    result = []
    with open(filename, "rb") as fh:
        data = fh.read()
    for i in range(len(data) // 4):
        b = 4*i 
        w = 0
        w = data[b]
        w = w << 8
        w |= data[b+1]
        w = w << 8
        w |= data[b+2]
        w = w << 8
        w |= data[b+3]
        result.append(w)
    return result

class UM:
    def __init__(me, program):
        me.banks = {0: program[:]}
        me.ax = 1
        me.regs = [0] * 8
        me.steps =0 
        me.ip = 0
        me.ops = [None] * 14
        me.stopped = False
        me.ops[0] = me.cmov
        me.ops[1] = me.aget
        me.ops[2] = me.aset
        me.ops[3] = me.add
        me.ops[4] = me.mul
        me.ops[5] = me.div
        me.ops[6] = me.nand
        me.ops[7] = me.halt
        me.ops[8] = me.aloc
        me.ops[9] = me.free
        me.ops[10] = me.out
        me.ops[11] = me.read
        me.ops[12] = me.load
        me.ops[13] = me.val

    def step(me):
        word = me.banks[0][me.ip]
        op = (word & OP) >> 28
        me.ip += 1
        me.ops[op](word)
        me.steps += 1 
    def cmov(me, word):
        (a, b, c) = decode_regs(word)
        r = me.regs
        if r[c] != 0:
            r[a] = r[b]

    def aget(me, word):
        (a, b, c) = decode_regs(word)
        r = me.regs
        r[a] = me.banks[r[b]][r[c]]
    
    def aset(me, word):
        (a, b, c) = decode_regs(word)
        r = me.regs
        me.banks[r[a]][r[b]] = r[c] 

    def add(me, word):
        (a, b, c) = decode_regs(word)
        r = me.regs
        r[a] = (r[b] + r[c]) & WORD

    def mul(me, word):
        (a, b, c) = decode_regs(word)
        r = me.regs
        r[a] = (r[b] * r[c]) & WORD

    def div(me, word):
        (a, b, c) = decode_regs(word)
        r = me.regs
        r[a] = (r[b] // r[c])

    def nand(me, word):
        (a, b, c) = decode_regs(word)
        r = me.regs
        r[a] = ~(r[b] & r[c]) & WORD

    def halt(me, word):
        me.stopped = True

    def aloc(me, word):
        (a, b, c) = decode_regs(word)
        r = me.regs
        j = me.ax
        while j in me.banks:
            j += 1
            j = j & WORD
        me.banks[j] = [0] * r[c]
        r[b] = j
        me.ax = j + 1

    def free(me, word):
        (a, b, c) = decode_regs(word)
        r = me.regs
        del me.banks[r[c]]

    def out(me, word):
        (a, b, c) = decode_regs(word)
        r = me.regs
        sys.stdout.buffer.write((r[c]).to_bytes(1, byteorder='big'))

    def read(me, word):
        (a, b, c) = decode_regs(word) 
        r = me.regs
        char = sys.stdin.read(1)
        if len(char) == 0:
            r[c] = WORD
        else:
            r[c] = ord(char)
    
    def load(me, word):
        (a, b, c) = decode_regs(word)
        r = me.regs
        if r[b] != 0:
            me.banks[0] = me.banks[r[b]][:]
        me.ip = r[c]

    def val(me, word):
        a = ((7 << 25) & word) >> 25
        r = me.regs
        v = ((1 << 25)-1) & word
        r[a] = v

def main():
    program = read_program(sys.argv[1])
    um = UM(program)
    while not um.stopped:
        um.step()
main()
