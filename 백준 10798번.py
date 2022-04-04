
inputWord = []
arrLen = []

strLine = ""
for i in range(5):
    read_char = str(input())
    inputWord.append(read_char)
    arrLen.append(len(read_char))

for k in range(max(arrLen)):
    for j in range(5):
        if k < arrLen[j]:
            strLine += (inputWord[j][k])

print(strLine)