'''
N, M = map(int, input().split())
arrs = []

for i in range(N):
    define_row = list(map(int, input().split()))
    arrs.append(define_row)

input_calculate_lines = int(input())

for _ in range(input_calculate_lines):
    i,j,x,y = map(int, input().split())
    total = 0 
    for a in range(i-1, x):
        for b in range(j-1, y):
            total += arrs[a][b]
    print(total)
'''


N,M = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]

input_calculate_lines = int(input())

dp = [[0]*(M + 1)for _ in range(N + 1)]
for i in range(N + 1):
    for j in range(M + 1):
        dp[i][j] = arr[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j -1]

for _ in range(input_calculate_lines):
    i,j,x,y = map(int, input().split())
    total = dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1]
    print(total)