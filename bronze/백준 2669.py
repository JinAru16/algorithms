coord = [[[0]for _ in range(100)] for _ in range(100)]


for _ in range(4):
    left_X,left_Y,right_X,right_Y = map(int, input().split())
    for i in range(left_X, right_X):
        for j in range(left_Y, right_Y):
            coord[i][j] = 1
        
count = 0

for m in range(100):
    for n in range(100):
        if coord[m][n] == 1:
            count += 1


print(count)
