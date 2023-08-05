N, K = map(int, input().split())
factors = [i for i in range(1, N+1) if N % i == 0]
if len(factors) < K:
    print(0)
else:
    print(factors[K-1])
