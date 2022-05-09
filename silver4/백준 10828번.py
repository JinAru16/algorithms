import sys

N = int(sys.stdin.readline().strip())

a = []


for _ in range(N):
    order = sys.stdin.readline().split()
    if len(order) == 2:
        a.append(int(order[1]))
    elif 'pop' in order:
        if len(a) != 0:
            print(a[-1])
            a.pop()
        else:
            print(-1)
    elif 'size' in order:
        print(len(a))
        continue
    elif 'empty' in order:
        if len(a) == 0:
            print('1')
            continue
        else:
            print('0')
            continue
    elif 'top' in order:
        if len(a) != 0:
            print(a[-1])
            continue
        else:
            print('-1')
            continue
    else:
        continue
    
    