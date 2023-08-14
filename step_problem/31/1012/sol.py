from collections import deque
import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    plants = [list(map(int, input().split())) for _ in range(K)]     # 배추 좌표
    visited = [0] * K
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    cnt = 0     # 배추흰지렁이 마리 수
    for plant in plants:
        i, j = plant[0], plant[1]


