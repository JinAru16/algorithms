from collections import deque
import sys

N = int(sys.stdin.readline().strip())

Deque = []

for _ in range(N):
    order = sys.stdin.readline().split()

    if 'push_front' in order:
        Deque.insert(0, order[-1])
    elif 'push_back' in order:
        Deque.append(order[-1])
    elif 'pop_front' in order:
        if len(Deque) < 1:
            print(-1)
        else:
            print(Deque.pop(0))
    elif 'pop_back' in order:
        if len(Deque) < 1:
            print(-1)
        else:
            print(Deque.pop(-1))
    elif 'size' in order:
        print(len(Deque))
    elif 'empty' in order:
        if len(Deque) == 0:
            print(1)
        else:
            print(0)
    elif 'front' in order:
        if len(Deque) > 0:
            print(Deque[0])
        else:
            print(-1)
    elif 'back' in order:
        if len(Deque) > 0:
            print(Deque[-1])
        else:
            print(-1)
    