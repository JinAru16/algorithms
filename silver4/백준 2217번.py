
from re import I


N = int(input())
a = []

for _ in range(N):
    weight = int(input())
    a.append(weight)


a.sort(reverse=True)
answer = []
i = 1
for j in a:
    b = j * i
    answer.append(b)
    i += 1
print(a)
print(answer)    
print(max(answer))