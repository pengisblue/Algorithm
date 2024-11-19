import sys
import heapq


sys.stdin = open('input.txt')

N, *heap = map(int, sys.stdin.read().split())
heapq.heapify(heap)

result = 0
while len(heap) > 1:
    a, b = heapq.heappop(heap), heapq.heappop(heap)
    result += (a + b)
    heapq.heappush(heap, a + b)

print(result)
