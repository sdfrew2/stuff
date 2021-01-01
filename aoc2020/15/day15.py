
class State:
    def __init__(me, start):
        me.lastSeen = {}
        for (i, x) in enumerate(start):
            if i == len(start) - 1:
                me.last = x
            else:
                me.lastSeen[x] = i
        me.time = i+1

    def __str__(me):
        return "state("+str(me.time)+" " + str(me.last) + " " + str(me.lastSeen)+")"
        
    def step(me):
        l = me.last
        if l in me.lastSeen:
            result = me.time - 1 - me.lastSeen[l]
        else:
            result = 0
        me.lastSeen[l] = me.time - 1
        me.time += 1
        me.last = result
        return result


start = [15,12,0,14,3,1]
s = State(start)
for i in range(2020 - len(start)):
    s.step()
print(s.last)


