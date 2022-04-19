N = int(input())
a = []
for _ in range(N):
    input_number = int(input())
    a.append(input_number)

a.sort()
for i in range(len(a)):
    print(a[i])