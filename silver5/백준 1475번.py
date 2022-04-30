import sys

N = int(sys.stdin.readline())

a = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']for _ in range(N)]  
strd_N = str(N)
print(list(strd_N))

i = 0
j = 0
while True:
    if strd_N[i] in a[j]:
        a[j].remove[strd_N[i]]
        i += 1
        continue
    elif strd_N[i] not in a[j]:
        if (strd_N[i] == '6') and ('9' in a[j]):
            a[j].remove[strd_N[i]]
            i += 1
            continue
        elif (strd_N[i] == '9') and ('6' in a[j]):
            a[j].remove[strd_N[i]]
            i += 1
            continue
        else:
            j += 1
            continue
    if i == N -1:
        break

a.count(key = lambda x: len(x) != 10)
