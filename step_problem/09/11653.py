N = int(input())
i = 2
while N > 1:    # N이 1이 되면 종료
    while N % i == 0:
        print(i)
        N /= i
    i += 1
