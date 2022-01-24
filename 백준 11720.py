number_length = int(input())
numbers = ''
total = 0


numbers += input()

for i in range(len(numbers)):
    total += eval(numbers[i])
print(total)

