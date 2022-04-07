aRow, aColumn = map(int, input().split())
A = []
B = []

for i in range(aRow):
    A.append(list(map(int, input().split())))

bRow, bColumn = map(int, input().split())

for i in range(bRow):
    B.append(list(map(int, input().split())))


answer = [[0 for _ in range(bColumn)]for _ in range(aRow)]

for j in range(aRow):
    for m in range(bColumn):
        k = 0
        temp = 0
        while k < aColumn:
            temp += A[j][k] * B[k][m]
            
            k += 1
        answer[j][m] = temp
for i in range(len(answer)):
    a = ""
    for j in range(len(answer[i])):
         a += str(answer[i][j])
         a += " "
    print(a)


    #answer_string = ""
    #print(answer_string.join(str(answer[i])))
    

