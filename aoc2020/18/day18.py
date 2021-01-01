import re
import sys

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
    if type(expr) == str:
        return int(expr)
    result = expr_eval(expr[0])
    i = 1
    while i < len(expr):
        op = expr[i]
        nextval = expr_eval(expr[i+1])
        if op == '+':
            result += nextval
        else:
            result *= nextval
        i += 2
    return result

result = 0
with open(sys.argv[1]) as fh:
    for line in fh:
        line = line.strip()
        result += expr_eval(parensToGroups(tokenize(line)))
print(result)





s = "(5*3 + (8)) + 7"
print(eval(parensToGroups(tokenize(s))))
    
    

