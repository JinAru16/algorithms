
testCastestCase = int(input())

for i in range(testCase):
    score_list = list(map(int, input().split()))
    total = 0
    count = 0

    avgScore = sum(score_list[1:]) / score_list[0]

    for score in score_list[1:]:
        if score > avgScore:
            count += 1
    answer = count / score_list[0] * 100

    print(f'{answer:.3f}%')

