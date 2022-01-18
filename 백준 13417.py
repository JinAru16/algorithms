
testCase = int(input())


for _ in range(testCase):
    charNumber = map(int, input())
    charString = list(map(str, input().split()))
    ans = [charString[0]]

    for i in range(1, len(charString)):
        left = ans[0]
        right = ans[-1]

        if charString[i] <= left:
            ans.insert(0, charString[i])
        else:
            ans.append(charString[i])
    print(''.join(ans))



1. 문자열 합치는 join 함수

'(문자열을 이어주는 문자)'.join(리스트)

lst = ['K', 'C', 'E']

#1. 따닥따닥 붙여서 잇는 경우
print(''.join(lst)) #KCE

#2. 띄어쓰기로 잇는 경우
print(' '.join(lst)) #K C E

#3. 별로 잇는 경우
print('*'.join(lst)) #K*C*E


출처: https://amber-chaeeunk.tistory.com/36 [채채씨의 학습 기록]

