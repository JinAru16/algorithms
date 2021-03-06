import sys
import math

T = int(sys.stdin.readline().strip())


for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    
    else:
        if r1 > distance + r2 or r2 > distance + r1 or distance > r1 + r2:
            print(0)
        elif abs(r1 - r2) == distance or r1 + r2 == distance:
            print(1)
        else:
            print(2)



