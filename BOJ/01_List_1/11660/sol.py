import sys
sys.stdin = open('input1.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
prefix_sums = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    numbers = list(map(int, input().split()))
    tmp = 0
    for j in range(1, N+1):
        tmp += numbers[j-1]
        upper_sum = prefix_sums[i-1][j]
        prefix_sums[i][j] = upper_sum + tmp

for k in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = prefix_sums[x2][y2] - prefix_sums[x1-1][y2] - prefix_sums[x2][y1-1] + prefix_sums[x1-1][y1-1]
    print(result)
