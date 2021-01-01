import re
import sys
import functools 

def tokenize(s):
    s = s.replace(" ", "")
    return [t for t in re.split("(\d+|[ +\-*/()])", s) if t != ""]

def parensToGroups(tokens):
    stack = [[]]
    for t in tokens:
        if t == "(":
            stack.append([])
        elif t == ")":
            stack[-2].append(stack.pop())
        else:
            stack[-1].append(t)
    return stack[0]



def expr_eval(expr):
    if type(expr) != list:
        return int(expr)
    i = 0
    sums = [0]
    while i < len(expr):
        part = expr[i]
        if part == "+":
            pass
        elif part == "*":
            sums.append(0)
        else:
            sums[-1] += expr_eval(part)
        i += 1
    return functools.reduce(lambda x, y: x*y, sums)            

def main():
    result = 0
    with open(sys.argv[1]) as fh:
        for line in fh:
            line = line.strip()
            result += expr_eval(parensToGroups(tokenize(line)))
    print(result)


main() 

