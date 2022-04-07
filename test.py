A = [[1, 2], [3,5], [4, 5]]


for i in range(len(A)):
    b = ""
    for j in range(len(A[i])):
        b += str(A[i][j])
        b += " "
    print(b)

