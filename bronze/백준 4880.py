# 1항 2항 3항 주어짐
# 등비(GP) 인지 등차(AP)인지 알아맞히고
# 4항 구하셈셈

a, b, c = map(int, input().split())

if c-b == b-a and a:
    print("AP " + b-a)
elif b