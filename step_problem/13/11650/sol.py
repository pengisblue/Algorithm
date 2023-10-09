from queue import PriorityQueue
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

que = PriorityQueue()
N = int(input())
for i in range(N):
    que.put(tuple(map(int, input().split())))

for i in range(N):
    print(*que.get())
