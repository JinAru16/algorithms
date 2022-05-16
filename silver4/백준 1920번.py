import sys
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split(' ')))
A.sort()

M = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split(' ')))


def binary_search(num):
    small = 0
    big = N - 1

    while small <= big:
        mid = (small + big) // 2
        if A[mid] == num:
            return True

        if num > A[mid]:
            small = mid + 1
        elif num < A[mid]:
            big = mid - 1
        
for i in range(M):

    if binary_search(nums[i]):
        print(1)
    else:
        print(0)