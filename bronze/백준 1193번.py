franctionNumber = int(input())
bott = 1 # 분모
top = 1 # 분자

def countFraction(n):
    if n <= 1:
        return 1
    else:
        answer = n + countFraction(n-1)
        return answer

while countFraction(bott) < franctionNumber:
    countFraction(bott)
    bott += 1



print('{}/{}'.format(top, bott))
'''

풀이 실패

'''