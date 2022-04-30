

N = int(input())
a = []

while N > 0:
    if N >= 3:
        N -= 3
        a.append('SK')
        if N == 0:
            break
        
        if N >= 3:
            N -= 3
            a.append('CY')
            continue
            
        if N < 3:
            N -= 1
            a.append('CY')
            continue

    if N < 3:
        if N > 0:
            N -= 1
            a.append('SK')
            if N > 0:
                N -= 1
                a.append('CY')

                
            if N == 0:
                break

print(a[-1])
