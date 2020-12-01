from collections import defaultdict 
import sys
nums = []
with open("input1.txt") as f:
    for line in f:
        line = line.strip()
        num = int(line)
        nums.append(num)
numset = set(nums)
for (i, x) in enumerate(nums):
    for j in range(i+1, len(nums)):
        y = nums[j]
        if 2020 - y - x in numset:
            print(x*y*(2020-y-x))
            sys.exit(0)
    
