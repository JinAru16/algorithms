import sys

N = int(sys.stdin.readline().strip())
M = list(map(int, sys.stdin.readline().split()))

def judge_prime_num(k):
    if k <= 1:
        return False
    if k > 1:
        for i in range(2, k):
            if k % i == 0:
                return False
            else:
                continue

        return True


count = 0
for i in M:
    if judge_prime_num(i) == True:
        count += 1
    else:
        continue
print(count)