import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
counting = [0] * 10001

for i in range(N):
    counting[int(input())] += 1

for i in range(1, 10001):
    if counting[i]:
        for j in range(counting[i]):
            print(i)
