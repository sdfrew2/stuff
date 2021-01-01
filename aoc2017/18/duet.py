

import collections

class ConstAccessor:
    def __init__(me, n):
        me.n = n

    def get(me):
        return me.n

    def set(me):
        pass

class VarAccessor:
    def __init__(me, var, registers):
        me.var = var
        me.registers = registers

    def get(me):
        return me.registers[me.var]

    def set(me, x):
        me.registers[me.var] = x

def makeAccessor(expr, cpu):
    try:
        n = int(expr)
        return ConstAccessor(n)
    except:
        return VarAccessor(expr, cpu.registers)



class Processor:
    def __init__(me, program):
        me.registers = collections.defaultdict(lambda: 0)
        me.program = []
        for line in program:
            tokens = line.strip().split()
            opcode = tokens[0]
            args = [makeAccessor(arg, me) for arg in tokens[1:]]
            me.program.append((opcode, args))
        me.pos = 0

    def step(me):
        try:
            instruction = me.program[me.pos]
        except IndexError:
            return False
        offset = getattr(me, instruction[0])(*instruction[1])
        if offset is None:
            offset = 1
        me.pos += offset
        return True
       
    def add(me, tgt, src):
        tgt.set(tgt.get() + src.get())

    def mul(me, tgt, src):
        tgt.set(tgt.get() * src.get())

    def mod(me, tgt, src):
        tgt.set(tgt.get() % src.get())

    def jgz(me, check, offset):
        if check.get() > 0:
            return offset.get()
        return 1

    def set(me, tgt, src):
        tgt.set(src.get())

    def snd(me, x):
        me.sndval = x.get()

    def rcv(me, x):
        if x.get() != 0:
            print(me.sndval)
            x.set(me.sndval)


def main18():
    program = [line for line in open("input.txt", "r") if len(line) > 2]
    cpu = Processor(program)
    counter = 0
    while cpu.step():
        #print(counter)
        counter += 1
    print(counter)

main18()

