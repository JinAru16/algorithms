N = int(input())

a = [x for x in range(1, N+1)]


while len(a) > 1:
    a.pop(0)
    a.append(a.pop(0))


print(a.pop(0))