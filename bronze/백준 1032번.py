import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = [[0]*(n+1)]+[[0]+list(map(int,input().split())) for _ in range(n)]

print(board)