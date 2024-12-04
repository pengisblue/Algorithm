import sys


sys.stdin = open('input.txt')


def find_max_sum(n, arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, n):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(current_sum, max_sum)

    return max_sum


N = int(input())
numbers = list(map(int, input().split()))

print(find_max_sum(N, numbers))
