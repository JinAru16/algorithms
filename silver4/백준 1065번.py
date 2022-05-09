import sys
N = int(sys.stdin.readline().strip())
i = 0
while True:
    a = []
    if N >= 100:
        for j in range(1, 100):
            a.append(j)
        for i in range(100, N+1):
            hund = i % 10
            ten = (i // 10) % 10
            one = ((i // 10)//10)
            if (one - ten) == (ten - hund):
                a.append(i)
            else:
                continue
        break
    elif N < 100:
        for k in range(1, N+1):
            a.append(k)
        break

print(len(a))



            


