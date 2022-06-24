
import sys

N = int(sys.stdin.readline())

own_card = list(map(int, sys.stdin.readline().split()))
own_card.sort()

M = int(sys.stdin.readline())

find_card = list(map(int, sys.stdin.readline().split()))

k = {}

for i in own_card:
    if i not in k:
        k[i] = 1
    else:
        k[i] += 1
        

def bianry_search(arr, target, small, big):
    if small > big:
        return 0
    
    mid = (small + big) // 2
    
    if arr[mid] < target:
        return bianry_search(arr, target, mid + 1, big)
    elif arr[mid]  > target:
        return bianry_search(arr, target, small, mid - 1)
    
    else:
        return k.get(target)
    
    

for q in range(len(find_card)):
    answer = bianry_search(own_card, find_card[q], 0, len(own_card) - 1)
    print(answer, end=' ')