import sys
import collections
import itertools
import functools
import re

def parseAtom(a):
    if a.startswith('"'):
        return a[1]
    else:
        return int(a)

def parseClause(c):
    return tuple(parseAtom(a.strip()) for a in c.split())

def parseRule(line):
    line = line.strip()
    (lhs, rhs) = line.split(":")
    clauses = [parseClause(c.strip()) for c in rhs.split("|")]
    return (int(lhs), clauses)

@functools.lru_cache(maxsize=None)
def matchRule(ruleNum, word):
    clauses = ruleDict[ruleNum]
    for clause in clauses:
        if matchClause(clause, word):
            return True
    return False

@functools.lru_cache(maxsize=None)
def matchClause(clause, word):
    if len(word) == 0:
       return False
    if len(clause) == 1 and type(clause[0]) == str:
        return clause[0] == word
    elif len(clause) == 1 and type(clause[0]) == int:
        return matchRule(clause[0], word)
    elif len(clause) == 2:
        for i in range(1,len(word)): # assumption: no zero-length matches
            if matchRule(clause[0], word[:i]) and matchRule(clause[1], word[i:]):
                return True
    elif len(clause) == 3:
        for i in range(1, len(word)):
            for j in range(i+1, len(word)):
                if matchRule(clause[0], word[:i]) and matchRule(clause[2], word[j:]) and matchRule(clause[1], word[i:j]):
                    return True
    return False


rulesFinished = False
rules = []
words = []
with open(sys.argv[1]) as fh:
    for line in fh:
        line = line.strip()
        if line == "":
            rulesFinished = True
        if rulesFinished:
            words.append(line)
        else:
            rules.append(parseRule(line))

ruleDict = {}
for (k, cs) in rules:
    ruleDict[k] = cs
ruleDict[8] = [(42,), (42, 8)]
ruleDict[11] = [(42, 31), (42, 11, 31)]

def main():
    counter = 0
    for word in words:
        print(word)
        if matchRule(0, word):
            counter += 1
    print(counter)

main()
