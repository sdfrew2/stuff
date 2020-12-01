
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

t = 0
for record in records:
    if len(record) == 8 or (len(record) == 7 and not ("cid" in record)):
        t += 1
     
print(t)

