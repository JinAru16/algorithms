import sys

N = int(sys.stdin.readline().strip())
queue = []

for _ in range(N):
    order = sys.stdin.readline().split()
    if len(order) == 2:
        queue.append(order[1])
    
    elif 'pop' in order:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.pop(0)
            
    
    elif 'size' in order:
        print(len(queue))
    
    elif 'empty' in order:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif 'front' in order:
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    
    elif 'back' in order:
        if len(queue):
            print(queue[-1])
        else:
            print(-1)
    else:
        continue