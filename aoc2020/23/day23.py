
class Game:
    def __init__(me, data):
        me.nodeMap = {}
        me.pos = data[0]
        for (i, x) in enumerate(data):
            me.nodeMap[x] = [data[(i-1) % len(data)], data[(i+1) % len(data)]]

    def connect(me, x, y):
        me.nodeMap[x][1] = y
        me.nodeMap[y][0] = x

    def _dec(me, x):
        result = x - 1
        if result == 0:
            result = len(me.nodeMap)
        return result

    def pred(me, x):
        return me.nodeMap[x][0]

    def succ(me, y):
        return me.nodeMap[y][1]
    
    def signature(me):
        current = 1
        result = []
        for i in range(len(me.nodeMap) - 1):
            current = me.succ(current)
            result.append(current)
        return "".join(str(i) for i in result)

    def step(me):
        p = me.pos
        nextThree = []
        current = p
        for i in range(3):
            current = me.succ(current)
            nextThree.append(current)
        afterThree = me.succ(current)
        
        target = me._dec(p)
        while target in nextThree:
            target = me._dec(target)
        afterTarget = me.succ(target)

        me.connect(target, nextThree[0])
        me.connect(nextThree[-1], afterTarget)
        me.connect(p, afterThree)
        me.pos = afterThree

    def __str__(me):
        return "Game" + str((me.pos, me.nodeMap))

    def productTwoAfter1(me):
        c = me.succ(1)
        d = me.succ(c)
        return c*d 


def main():
    data = "135468729"
    g = Game([int(c) for c in data])
    for i in range(100):
        g.step()
    print(g.signature())

def main2():
    data = [1,3,5,4,6,8,7,2,9]
    for i in range(10, 10**6 + 1):
        data.append(i)
    g = Game(data)
    for i in range(10**7):
        if i % 100000 == 0:
            print(i)
        g.step()
    print(g.productTwoAfter1())

main2()
