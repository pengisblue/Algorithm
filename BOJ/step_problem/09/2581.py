M = int(input())
N = int(input())
primes = []
for num in range(M, N+1):
    if num == 2:
        primes.append(2)
    elif num > 2:
        is_prime = True
        for i in range(2, num):
            if not num % i:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

if primes:
    print(sum(primes))
    print(primes[0])
else:
    print(-1)
