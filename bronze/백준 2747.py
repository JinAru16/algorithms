fibn = [0, 1]

n = int(input())

for i in range(2, n+1):
    fibn.append(fibn[-1] + fibn[-2])

print(fibn[-1])






