from collections import deque
import sys
sys.stdin = open('input.txt')

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def bfs():
    global days
    que = deque(tomato)
    while que:
        ni, nj, day = que.popleft()
        for idx in range(4):
            dx = ni + di[idx]
            dy = nj + dj[idx]
            if 0 <= dx < N and 0 <= dy < M and not box[dx][dy]:
                box[dx][dy] = 1
                que.append((dx, dy, day+1))
                if days < day + 1:
                    days = day + 1


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

tomato = []
days = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            tomato.append((i, j, 0))

bfs()
for i in range(N):
    for j in range(M):
        if not box[i][j]:
            days = -1
            break

print(days)