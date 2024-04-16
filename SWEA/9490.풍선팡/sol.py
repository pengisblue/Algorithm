import sys
sys.stdin = open('input1.txt')

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())
for t in range(1, T + 1):
    result = 0
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(N)]
    for n in range(N):
        for m in range(M):
            pang = board[n][m]
            repeat = board[n][m]
            for d in range(4):
                for r in range(1, repeat+1):
                    if 0 <= (n + di[d] * r) < N and 0 <= (m + dj[d] * r) < M:
                        pang += board[n + di[d] * r][m + dj[d] * r]

            if pang > result:
                result = pang

    print(f'#{t} {result}')



