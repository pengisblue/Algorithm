from itertools import permutations
import sys
sys.stdin = open('input3.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(range(1, N+1))
per = list(permutations(numbers, M))
for i in per:
    print(*i)
