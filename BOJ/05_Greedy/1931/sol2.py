import sys


sys.stdin = open('input.txt')

_, *li = map(int, sys.stdin.read().split())
c = 0
print(sum((c := e) and 1 for s, e in sorted(zip(li[::2], li[1::2]), key=lambda x: (x[1], x[0])) if s >= c))
