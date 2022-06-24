import sys


N, M = map(int, sys.stdin.readline().split())

never_heard = {}


for _ in range(N):
    h_name = sys.stdin.readline().strip()
    if h_name not in never_heard:
        never_heard[h_name] = 1

for _ in range(M):
    s_name = sys.stdin.readline().strip()
    if s_name not in never_heard:
        never_heard[s_name] = 1
    else:
        never_heard[s_name] += 1

count = 0
never_heard_never_seen = []
for i in never_heard:
    if never_heard[i] > 1:
        count+= 1
        never_heard_never_seen.append(i)

never_heard_never_seen.sort()
print(count)
for j in never_heard_never_seen:
    print(j)