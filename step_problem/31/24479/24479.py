import sys
sys.stdin = open('input.txt')


def dfs(V, E, R):
    


N, M, R = map(int, input().split())
matrix = [[0]*N for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1
