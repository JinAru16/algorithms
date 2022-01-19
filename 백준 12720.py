# 우유순서 : 딸 -> 초 -> 바 -> 딸
#          0 -> 1 -> 2 -> 0


store_number = int(input())

milk_type = list(map(int, input().split()))

count = 0

for i in range(store_number):
    if milk_type[i] == count % 3:
        count += 1
print(count)