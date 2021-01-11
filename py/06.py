import fileinput

qs1 = set()
qs2 = set()
fresh = True
total1 = 0
total2 = 0
for line in fileinput.input():
    if not line.strip():
        total1 += len(qs1)
        total2 += len(qs2)
        fresh = True
        qs1 = set()
        qs2 = set()
        continue

    newqs = set()
    for c in line.strip():
        newqs.add(c)
    if fresh:
        qs2 = set(newqs)
        fresh = False
    else:
        qs2 = qs2.intersection(newqs)
    qs1 = qs1.union(newqs)

total1 += len(qs1)
total2 += len(qs2)

print('Part 1:', total1)
print('Part 2:', total2)
