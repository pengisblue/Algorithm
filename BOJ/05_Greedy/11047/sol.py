import sys


sys.stdin = open('input.txt')

N, K = map(int, input().split())
A = list()
cnt = 0
for i in range(N):
    A.append(int(input()))

for i in range(N - 1, -1, -1):
    cnt += K // A[i]
    K = K % A[i]
    if not K:
        break

print(cnt)