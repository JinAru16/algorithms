inputLength = int(input())

inputString = input()

answer = 0

for i in range(inputLength):
    answer += (ord(inputString[i]) - 96) * (31 ** i)
print(answer % 1234567891)