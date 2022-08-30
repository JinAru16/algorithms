from typing import Deque


def solution(s):
    answer = True
    a = Deque()
    for i in range(len(s)):
        if(len(a) == 0):
            a.append(s[i])
        elif(s[i]== "("):
            a.append(s[i])
        else:
            if(a[-1] == "("):
                a.pop()
            else:
                continue
    
    if(len(a) == 0):
        answer = True
    else:
        answer = False

    return answer