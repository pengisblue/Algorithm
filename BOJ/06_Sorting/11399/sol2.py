import sys


sys.stdin = open('input.txt')

# 카운팅 정렬
N = int(input())
P = list(map(int, input().split()))
max_num = max(P)
counts = [0] * (max_num + 1)
sorted_P = [0] * N

for i in range(N):
    counts[P[i]] += 1

for i in range(1, max_num + 1):
    counts[i] += counts[i - 1]

for i in range(N - 1, -1, -1):
    counts[P[i]] -= 1
    sorted_P[counts[P[i]]] = P[i]

result = sorted_P[0]

for i in range(1, N):
    sorted_P[i] += sorted_P[i - 1]
    result += sorted_P[i]

print(result)
