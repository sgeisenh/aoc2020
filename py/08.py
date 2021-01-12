import fileinput

A = []
for line in fileinput.input():
    left, right = line.strip().split()
    A.append((left, int(right)))

seen = set()
i = 0
acc = 0
while i not in seen:
    seen.add(i)
    op, arg = A[i]
    if op == 'acc':
        acc += arg
        i += 1
    elif op == 'jmp':
        i += arg
    elif op == 'nop':
        i += 1

def test(instrs):
    seen = set()
    i = 0
    acc = 0
    while i not in seen:
        if (i >= len(instrs)):
            return acc
        seen.add(i)
        op, arg = instrs[i]
        if op == 'acc':
            acc += arg
            i += 1
        elif op == 'jmp':
            i += arg
        elif op == 'nop':
            i += 1
    return None


B = []
result = None
for i, (op, arg) in enumerate(A):
    if op == 'jmp':
        result = test(A[:i] + [('nop', arg)] + A[i + 1:])
    elif op == 'nop':
        result = test(A[:i] + [('jmp', arg)] + A[i + 1:])
    if result:
        break

print('Part 1:', acc)
print('Part 2:', result)
