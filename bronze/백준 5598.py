inputCode = list(input())
answerList = []
answer = ''

for i in range(len(inputCode)):
    transfered_number = 0
    if ord(inputCode[i]) < 68 :
        transfered_number = ord(inputCode[i]) + 23
    else:
        transfered_number = ord(inputCode[i]) - 3
    answerList.append(chr(transfered_number))


print(answer.join(answerList))

