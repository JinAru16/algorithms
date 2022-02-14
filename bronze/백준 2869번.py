A, B, V = map(int,input().split())

answer = 0
count = 0
hight = V - A
if hight % (A - B) == 0:
    answer = int(hight / (A - B))
else:
    answer = int(hight / (A - B) + 1)

print(answer + 1)




