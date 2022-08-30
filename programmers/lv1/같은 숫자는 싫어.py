from collections import deque

arr2 = [1, 1, 3, 3, 0, 1, 1]
arr1 = [4, 4, 4, 3, 3]

def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if((arr[i-1] != arr[i])):
            answer.append(arr[i])
    return answer


print(solution(arr1))