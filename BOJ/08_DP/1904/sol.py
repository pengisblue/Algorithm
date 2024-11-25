import sys


sys.stdin = open('input.txt')


def dp(n):
    MOD = 15746

    if n == 1:
        return 1
    elif n == 2:
        return 2

    prev2, prev1 = 1, 2
    for i in range(3, n + 1):
        curr = (prev2 + prev1) % MOD
        prev2, prev1 = prev1, curr

    return prev1


N = int(input())
print(dp(N))
