import sys
import collections
import math

with open(sys.argv[1]) as fh:
    lines = fh.readlines()

START = int(lines[0])
BUSES = [int(busId) for busId in lines[1].split(",") if busId.isnumeric()]

def waitTime(start, busId):
    return busId - start % busId 

(minWaitTime, minWaitBus) = min((waitTime(START, busId), busId)  for busId in BUSES)
print(minWaitTime *  minWaitBus)
