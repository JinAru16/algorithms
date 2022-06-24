from  collections import deque


while True:
    N = str(input())
    if N == '.':
        break
    parentheses = deque()
    status = True

    for char in N:
        if char == '(' or char == '[':
            parentheses.append(char)
        elif char == ')':
            if not parentheses or parentheses[-1] == '[':
                status = False
                break
            elif parentheses[-1] == '(':
                parentheses.pop()
        elif char == ']':
            if not parentheses or parentheses[-1] == '(':
                status = False
                break
            elif parentheses[-1] == '[':
                parentheses.pop()
    
    if not parentheses and status == True:
        print('yes')
    else:
        print('no')






    
        
