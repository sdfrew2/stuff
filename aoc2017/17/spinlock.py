SHIFT = 359
ITERATIONS = 2017
import sys

class Spinlock:
    def __init__(me, shift):
        me.buffer = [0]
        me.shift = shift
        me.pos = 0
        me.counter = 1

    def spin(me):
        shiftPos = (me.pos + me.shift) % len(me.buffer)
        if me.buffer[shiftPos] == 0:
            print(">>", me.counter)
        me.buffer[shiftPos+1:shiftPos+1] = [me.counter]
        me.counter += 1
        me.pos = shiftPos+1
        
    def __str__(me):
        parts = []
        for (i, x) in enumerate(me.buffer):
            if i == me.pos:
                parts.append("(" + str(x) + ")")
            else:
                parts.append(str(x))
        return " ".join(parts)


class AdvancedSpinlock:
    def __init__(me, shift, chunkSize):
        me.buffer = [[0]]
        me.shift = shift
        me.chunkSize = chunkSize
        me.chunkIndex = 0
        me.chunkPos = 0
        me.counter = 0
        me.insertedAfterZero = None
    def spin(me):
        me.counter += 1
        chunk = me.buffer[me.chunkIndex]
        remainingDistance = me.shift
        while me.chunkPos + remainingDistance >= len(chunk):
            stepsToNextChunk = len(chunk) - me.chunkPos
            remainingDistance -= stepsToNextChunk
            me.chunkIndex += 1
            me.chunkIndex %= len(me.buffer)
            me.chunkPos = 0
            chunk = me.buffer[me.chunkIndex]
        shiftPos = me.chunkPos + remainingDistance
        #print(chunk, me.chunkPos, shiftPos, remainingDistance)
        if chunk[shiftPos] == 0:
            me.insertedAtZero = me.counter
        chunk[shiftPos+1:shiftPos+1] = [me.counter]
        insertionPos = shiftPos + 1
        if len(chunk) > me.chunkSize:
            mid = me.chunkSize // 2
            rightHalf = chunk[mid:]
            leftHalf = chunk[:mid]
            del chunk[mid:]
            me.buffer[me.chunkIndex+1:me.chunkIndex+1] = [rightHalf]
            if insertionPos >= mid:
                me.chunkPos = insertionPos - mid
                me.chunkIndex += 1
            else:
                me.chunkPos = insertionPos
        else:
            me.chunkPos = insertionPos
        
    def __str__(me):
        parts = []
        for (i, x) in enumerate(me.buffer):
            if i == me.pos:
                parts.append("(" + str(x) + ")")
            else:
                parts.append(str(x))
        return " ".join(parts)


def main17():
    lock = Spinlock(SHIFT)
    for i in range(ITERATIONS):
        lock.spin()
    index = (lock.pos + 1) % len(lock.buffer)
    print(lock.buffer[index])
   

def main17b():
    lock = AdvancedSpinlock(SHIFT, 3000)
    for i in range(50):
        print("million", i)
        for j in range(1000000):
            lock.spin()
    print(lock.insertedAtZero) 
main17b()

