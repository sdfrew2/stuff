import sys

def parseLine(line):
    line = line.strip()
    tokens = line.split(":")
    rule = parseRule(tokens[0])
    pw = tokens[1]
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

def checkRule(rule, s):
    ((omin, omax), letter) = rule
    return omin <= s.count(letter) <= omax

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

            
