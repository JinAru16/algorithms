
import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

a = []
for i in range(M, N+1):
    for k in range(2, i):
        
        if i % k != 0:
            continue
        else:
            break
        
  
    if i == 1:
        continue
    else:
        a.append(i)

sum_num = 0            
for i in a:
    sum_num += i

print(a)