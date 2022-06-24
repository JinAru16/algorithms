import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

queue = deque()

for i in range(1, N + 1):
    queue.append(i)

answer = deque()

index = K - 1

while len(queue) > 0:
    if index <= len(queue):
        for _ in range(K-1):
            queue.append(queue.popleft())
        answer.append(queue.popleft())
    elif index > len(queue):
        new_index = index % len(queue)
        for _ in range(new_index):
            queue.append(queue.popleft())
        answer.append(queue.popleft())


print("<",', '.join(str(x) for x in answer), ">", sep= "")


