import sys
sys.stdin = open('input.txt')


def comb(idx, n):
    global cnt
    if n == K:
        cnt += 1
        return

    if idx == N:
        return

    bit[idx] = 1
    comb(idx+1, n+1)
    bit[idx] = 0
    comb(idx+1, n)


N, K = map(int, input().split())
bit = [0] * N
cnt = 0
comb(0, 0)
print(cnt)
