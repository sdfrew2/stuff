import sys

def parseLine(line):
    line = line.strip()
    tokens = line.split(":")
    rule = parseRule(tokens[0])
    pw = tokens[1].strip()
    return (rule, pw)

def parseRule(s):
    s = s.strip()
    parts = s.split(" ")
    r = parseRange(parts[0])
    letter = parts[1]
    return (r, letter)

def parseRange(s):
    s = s.strip()
    parts = s.split("-")
    return (int(parts[0]), int(parts[1]))

def pwc(s, i):
    if i < 1 or i > len(s):
        return None
    return s[i-1]

def checkRule(rule, s):
    ((i,j), letter) = rule
    positions = [i,j]
    match = 0
    matches = []
    for p in positions:
        matches.append(pwc(s,p))        
        if letter == pwc(s, p):
            match += 1
    print(matches)
    return match == 1

good = 0
bad = 0
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        (rule, pw) = parseLine(line)
        if checkRule(rule, pw):
            good += 1
        else:
            bad += 1

print("good = " , good, " bad = " , bad)

            
