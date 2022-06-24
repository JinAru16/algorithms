import sys

N = int(sys.stdin.readline().strip())

def factorial(num):
    if num > 0:
        return num * factorial(num - 1)
    if num == 0:
        return 1


a = str(factorial(N))
count_zero = 0


for i in range(len(a)):
    if a[- 1 - i] == '0':
        count_zero += 1
    else:
        break

print(count_zero)

