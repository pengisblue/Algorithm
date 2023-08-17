import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline


def permutation(idx, n, cnt, m):
    if cnt == m:

        return
    elif idx == n:
        return
    else:
        bit[idx] = numbers[idx]
        permutation(idx+1, n, cnt+1, m)
        bit[idx] = 0
        permutation(idx+1, n, cnt, m)
        return


N, M = map(int, input().split())
numbers = list(range(1, N+1))
bit = [0] * N
permutation(0, N, 0, M)
