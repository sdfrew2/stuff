
import sys

class Ship:
    def __init__(me, position, direction):
        me.pos = position
        me.dir = direction

    def run(me, cmd, val):
        if cmd == 'F':
            me.pos += me.dir * val
        elif cmd == 'L':
            me.dir *= (1j)**(val // 90)
        elif cmd == 'R':
            me.dir *= (-1j)**(val // 90)
        elif cmd == 'N':
            me.pos += 1j * val
        elif cmd == 'E':
            me. pos += val
        elif cmd == 'W':
            me.pos -= val
        elif cmd == 'S':
            me.pos -= 1j * val

    
instructions = []
with open(sys.argv[1]) as fh:
    for line in fh:
        line = line.strip()
        cmd = line[0]
        val = int(line[1:])
        instructions.append((cmd, val))

ship = Ship(0, 1)
for (cmd, val) in instructions:
    ship.run(cmd, val)
print(abs(ship.pos.real) + abs(ship.pos.imag))


     
        
