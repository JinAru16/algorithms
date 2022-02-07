from operator import truediv


playerNumber = int(input())
playerList = []
for _ in range(playerNumber):
    playerName = input()
    playerList.append(playerName[0])

firstLetter = set(playerList)
answer = []

for i in firstLetter:
    if playerList.count(i) > 4:
        answer.append(i)

if len(answer) > 0:
    print(''.join(sorted(answer)))
else:
    print('PREDAJA')




'''
from multiprocessing.sharedctypes import Value


playerNumber = int(input())
letter_dic = {}
answer = ''

for i in range(playerNumber):
    playerName = str(input())
    firstLetter = playerName[0]
    if firstLetter not in letter_dic:
        letter_dic[firstLetter] = 1
    else:
        letter_dic[firstLetter] += 1

for key, value in letter_dic.items():
    if value > 4:
        answer += key


if len(answer) == 0:
    print('PREDAJA')
else:
    print(answer)
'''



