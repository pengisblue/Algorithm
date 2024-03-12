import sys
sys.stdin = open('input.txt')


def facto(n):
    if n == 0 or n == 1:
        return 1

    else:
        return n * facto(n-1)


N = int(input())
print(facto(N))
