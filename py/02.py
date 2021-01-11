import fileinput

res1 = 0
res2 = 0
for line in fileinput.input():
    splits = line.split()
    lo, hi = [int(x) for x in splits[0].split('-')]
    c = splits[1][0]
    p = splits[2]
    if lo <= p.count(c) <= hi:
        res1 += 1
    if (p[lo - 1] == c) != (p[hi - 1] == c):
        res2 += 1

print('Part 1:', res1)
print('Part 2:', res2)
