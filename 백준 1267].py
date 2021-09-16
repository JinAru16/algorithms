# 영식 요금제
# 민식 요금제

# 영식 = 0<시간<30초 : 10원
# 민식 = 0<시간<60초 : 15원

# 입력 첫줄에는 통화 목록의 갯수
# 입력 두번쨰 줄에는 통화 시간갯수

callNumber = int(input())
callTime = list(map(int, (input().split())))

youngsikPay = 0
minsikPay = 0


for i in range(callNumber):
    youngsikPay += ((callTime[i] // 30) + 1) * 10
    minsikPay += ((callTime[i] // 60) + 1) * 15

if youngsikPay < minsikPay:
    print("Y " + str(youngsikPay))
elif youngsikPay > minsikPay:
    print("M " +str(minsikPay))
else:
    print("Y M " + str(youngsikPay))


