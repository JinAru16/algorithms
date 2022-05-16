import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    VPS = list(sys.stdin.readline().strip())
   
    leng = int(len(VPS))
    a = VPS.count("(")
    b = VPS.count(")")
    if a != b:
        print("NO")

    elif a == b:
        i = 0
        while True:
            if len(VPS) == 0:
                print("YES")
                break
            if VPS[i] == VPS[i+1]:
                i+=1
                continue
            if VPS[i] + VPS[i+1] =='()':
                VPS.remove(VPS[i])
                VPS.remove(VPS[i])
                if i == 0:
                    continue
                if len(VPS) == 0:
                    print("YES")
                    break
                i -= 1
                continue
            if len(VPS) != 0:
                print("NO")
                break
                

        
       
        