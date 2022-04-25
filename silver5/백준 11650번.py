import sys
N = int(sys.stdin.readline())
a = [[] for _ in range(N)]

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    a[i].append(x)
    a[i].append(y)

a.sort()


for i in range(N):
    print('{} {}'.format(a[i][0], a[i][1]))
