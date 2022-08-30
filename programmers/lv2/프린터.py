from collections import deque
import queue
a1=[2, 1, 3, 2]
b1=2

def solution(priorities, location):
    answer = 0
    maxNum = max(priorities)
    while True:
        a = priorities.pop(0)
        if (maxNum == a):
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
            maxNum = max(priorities)
        else:
            priorities.append(a)
            if location == 0:
                location = len(property) - 1
            else:
                location -= 1


    return answer
    

print(solution(a1, b1))