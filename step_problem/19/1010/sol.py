import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    n, k = 1, 1
    for i in range(N):
        n *= (M-i)
        k *= (N-i)

    print(n//k)
