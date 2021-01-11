import fileinput

A = [int(line) for line in fileinput.input()]
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] + A[j] == 2020:
            print('Part 1:', A[i] * A[j])
        for k in range(j + 1, len(A)):
            if A[i] + A[j] + A[k] == 2020:
                print('Part 2:', A[i] * A[j] * A[k])
