from itertools import combinations
import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
cards = list(combinations(numbers, 3))
max_v = 0
for card in cards:
    sum_v = card[0] + card[1] + card[2]
    if sum_v > max_v and sum_v <= M:
        max_v = sum_v

print(max_v)
