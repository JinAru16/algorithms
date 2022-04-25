import sys

N = int(sys.stdin.readline())

a = [0] * 10001

for i in range(N):
    any_number = int(sys.stdin.readline().strip())
    a[any_number] += 1

for p in range(10001):
    if a[p] != 0:
        for q in range(a[p]):
            print(p)
