import fileinput

A = [line.strip() for line in fileinput.input()]

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

res1 = 0
res2 = 1
for cc, rc in slopes:
    count = 0
    r = 0
    c = 0
    while r < len(A):
        if A[r][c % len(A[r])] == '#':
            count += 1
        r += rc
        c += cc
    res2 *= count
    if rc == 1 and cc == 3:
        res1 = count

print('Part 1:', res1)
print('Part 2:', res2)
