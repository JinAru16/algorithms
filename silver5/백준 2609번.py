
a, b = map(int, input().split())
def Euclid(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def lowest(a,b):
    answer = int((a * b)/(Euclid(a,b)))
    return answer


print(Euclid(a, b))
print(lowest(a, b))