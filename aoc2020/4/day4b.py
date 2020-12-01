import re

def parseDb(fh):
    record = {}
    result = [record]
    for line in fh:
        line = line.strip()
        if len(line) == 0:
            record = {}
            result.append(record)
            continue
        tokens = line.split(" ")
        for token in tokens:
            (k, v) = token.split(":")
            record[k] = v
    return result

with open("input.txt") as fh:
    records = parseDb(fh)

rules = {}
rules["byr"] = [( "([0-9]+)$", 1920, 2002 )]
rules["iyr"] = [( "([0-9]+)$", 2010, 2020 )]
rules["eyr"] = [( "([0-9]+)$", 2020, 2030 )]
rules["hgt"] = [( "([0-9]+)cm$", 150, 193), ("([0-9]+)in$", 59, 76)]
rules["hcl"] = [( "#[0-9a-f]{6}$", None, None)]
rules["ecl"] = [("blu|amb|brn|gry|grn|hzl|oth$", None, None)]
rules["pid"] = [("[0-9]{9}$", None, None)]

def validateSingleRule(r, v):
    regex = r[0]
    thematch = re.match(regex, v)
    if not thematch:
        return False
    if r[1] != None:
        if r[1] > int(thematch.group(1)):
            return False
    if r[2] != None and int(thematch.group(1)) > r[2]:
        return False
    return True

def validate(record):
    for (k, rs) in rules.items():
        if not (k in record):
            return False
        anyMatch = any(validateSingleRule(r, record[k]) for r in rs)
        if not anyMatch:
            return False
    return True



t = 0
for record in records:
    if validate(record):
        t += 1
     
print(t)

