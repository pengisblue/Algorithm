import sys


sys.stdin = open('input.txt')
input = sys.stdin.readline


def dp(k):
    p = [0] * max(6, k + 1)
    p[1] = p[2] = p[3] = 1
    p[4] = p[5] = 2

    if k > 5:
        for i in range(6, k + 1):
            p[i] = p[i - 1] + p[i - 5]
    return p


T = int(input())
cases = [int(input()) for i in range(T)]

max_n = max(cases)
P = dp(max_n)

for n in cases:
    print(P[n])
    