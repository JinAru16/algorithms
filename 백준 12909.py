numbers = list(map(int, input().split()))

positive_number = []

for number in numbers:
    if number > 0:
        positive_number.append(number)

print(len(positive_number))