# p와 q로 이뤄진 숫자 P와  또 다른 숫자 K가 주워지는데 q 나 q가 k 보다 작으면 bad, 크면 good을 출력
# 답은 잘 나오는데 시간이 초과

P, K = map(int, input().split())

for p in range(2, P+1):
    quotient = P // p
    if P % p == 0:
        if quotient < K or p < K:
            print("BAD {}".format(+min(quotient, p)))
            break

        if quotient and p > K:
            print("GOOD")
            break
