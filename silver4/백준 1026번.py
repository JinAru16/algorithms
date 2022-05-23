import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort()


total = 0

for i in range(N):
    multiple = A[i]*B[-1 - i]
    total += multiple

print(total)

