import sys

N = int(sys.stdin.readline())


if N != 1:
    i = 2
    a = []
    while N > 1:
        if N % i == 0:
            a.append(i)
            N /= i
            
        if N % i != 0:
            i += 1
            continue

    for i in range(len(a)):
        print(a[i])

elif N == 1:
    print()




