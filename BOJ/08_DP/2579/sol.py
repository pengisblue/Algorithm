import sys


sys.stdin = open('input.txt')


def max_step(n, step_list):
    if n == 1:
        return step_list[0]
    elif n == 2:
        return step_list[0] + step_list[1]

    dp = [0] * n
    dp[0] = step_list[0]
    dp[1] = step_list[0] + step_list[1]
    dp[2] = max(step_list[0] + step_list[2], step_list[1] + step_list[2])

    for i in range(3, n):
        dp[i] = max(dp[i - 2] + step_list[i], dp[i - 3] + step_list[i - 1] + step_list[i])

    return dp[-1]


N = int(input())
stair = [int(input()) for _ in range(N)]
print(max_step(N, stair))
