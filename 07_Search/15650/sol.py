import sys
sys.stdin = open('input3.txt')
input = sys.stdin.readline


def combi(idx, cnt):
    if cnt == M:
        for i in range(N):
            if bit[i]:
                print(i+1, end=' ')
        print()
    elif idx == N:
        return
    else:
        bit[idx] = 1
        combi(idx+1, cnt+1)
        bit[idx] = 0
        combi(idx+1, cnt)


N, M = map(int, input().split())
numbers = list(range(1, N+1))
bit = [0] * N
combi(0, 0)
