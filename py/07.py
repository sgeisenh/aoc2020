import fileinput
from collections import defaultdict

A = defaultdict(lambda: set())
B = defaultdict(lambda: set())

for line in fileinput.input():
    outer, right = line.strip().split(' bags contain ')
    if right == 'no other bags.':
        continue

    for comp in right.split(', '):
        count_str, rest = comp.split(' ', 1)
        count = int(count_str)
        inner = rest.split(' bag')[0]
        A[inner].add(outer)
        B[outer].add((inner, count))

def dfs(v, X):
    if v in X:
        return X
    X.add(v)
    for vn in A[v]:
        X = dfs(vn, X)
    return X

def countbags(v):
    total = 0
    for bag, count in B[v]:
        total += count * (1 + countbags(bag))
    return total

print('Part 1:', len(dfs('shiny gold', set())) - 1)
print('Part 2:', countbags('shiny gold'))
