import sys
S = int(sys.stdin.readline())
total = 0
i = 0
while True:
    S -= i
    if S > 0:
        i += 1
        continue
    if S < 0:
        S += i
        i -= 1
        print(i)
        break
    if S == 0:
        print(i)
        break


