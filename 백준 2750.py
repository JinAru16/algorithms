numbers = int(input())

number_list = []
for i in range(numbers):
    number = int(input())
    number_list.append(number)
number_list.sort()

for sortedNumber in number_list:
    print(sortedNumber)

