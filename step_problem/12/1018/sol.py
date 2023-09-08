import sys
sys.stdin = open('input7.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().rstrip() for _ in range(N)]
# 올바른 체스판
chess = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]
result = 64
for i in range(N-7):
    for j in range(M-7):
        cnt = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                # 체스판과 보드 비교
                # board 인덱스는 변하지만 chess 인덱스는 변하지 않게 해야함
                if board[k][l] != chess[k-i][l-j]:
                    cnt += 1
        diff = min(cnt, 64-cnt)
        if diff < result:
            result = diff
print(result)
