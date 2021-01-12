import fileinput

qs1 = None
qs2 = None
total1 = 0
total2 = 0
for line in fileinput.input():
    line = line.strip()
    if not line:
        total1 += len(qs1)
        total2 += len(qs2)
        qs1 = None
        qs2 = None
        continue

    if qs1 == None:
        qs1 = set(line)
    else:
        qs1 = qs1 | set(line)
    if qs2 == None:
        qs2 = set(line)
    else:
        qs2 = qs2 & set(line)

total1 += len(qs1)
total2 += len(qs2)

print('Part 1:', total1)
print('Part 2:', total2)
