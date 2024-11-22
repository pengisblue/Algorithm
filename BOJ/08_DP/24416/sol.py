import sys

sys.stdin = open('input.txt')

N = int(input())


def f1(n):
    if n == 1 or n == 2:
        return 1

    dp = [0] * (n + 1)
    dp[1] = dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print(f'{f1(N)} {N - 2}')
