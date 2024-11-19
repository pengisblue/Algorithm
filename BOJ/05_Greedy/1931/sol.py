import sys


sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
times = list()
for i in range(N):
    s, e = map(int, input().split())
    times.append((s, e))

# times.sort()
times.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end = 0
for s, e in times:
    if s >= end:
        cnt += 1
        end = e

print(cnt)
