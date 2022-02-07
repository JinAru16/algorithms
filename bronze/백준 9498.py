# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.


a = map(int, input())

if a in range(90, 101):
    print("A")

elif a in range(80, 90):
    print("B")

elif a in range(70, 80):
    print("C")

elif a in range(60, 70):
    print("D")

else:
    print("F")