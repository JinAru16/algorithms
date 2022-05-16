import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    VPS = sys.stdin.readline().strip()

    stack = []

    for paren in VPS:
        if paren == '(':
            stack.append(paren)
        else:
            if len(stack):
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        
        else:
            print('YES')