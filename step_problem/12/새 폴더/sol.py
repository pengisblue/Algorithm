import sys
sys.stdin = open('input.txt')

N = int(input())
for num in range(1, N):
    result = num
    test = num
    while test > 10:
        result += test % 10
        test //= 10
    result += test
    if result == N:
        ans = num
        break
else:
    ans = 0

print(ans)
