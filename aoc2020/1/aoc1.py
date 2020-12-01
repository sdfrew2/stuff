from collections import defaultdict 
nums = {}
with open("input1.txt") as f:
    for line in f:
        line = line.strip()
        num = int(line)
        if 2020 - num in nums:
            print(num * (2020 - num))
            break
        nums[num] = 1
