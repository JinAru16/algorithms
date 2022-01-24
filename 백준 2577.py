a = int(input())
b = int(input())
c = int(input())

multiply = list(str(a*b*c))

print(multiply)

for i in range(10):
    print(multiply.count(str(i)))
