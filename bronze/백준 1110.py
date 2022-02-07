num = int(input())
temp = num
new_num = 0
cycle_num = 0

while True:
    frontNumber = temp // 10
    backNumber = temp % 10
    mid_num= (frontNumber + backNumber) % 10
    temp = (backNumber * 10) + mid_num


    cycle_num = cycle_num + 1
    if(temp == num):
        break

print(cycle_num)