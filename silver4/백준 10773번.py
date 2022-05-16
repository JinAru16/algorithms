import sys
K = int(sys.stdin.readline().strip())

stack = []
total = 0

for _ in range(K):
    call_number = int(sys.stdin.readline().strip())
    if call_number != 0:
        stack.append(call_number)
    else:
        if len(stack)>0:
            stack.pop()
        else:
            continue
for i in stack:
    total += i
print(total)
        