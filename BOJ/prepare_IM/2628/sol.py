import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

M, N = map(int, input().split())
C = int(input())
row = [0, N]
col = [0, M]
for _ in range(C):
    w, line = map(int, input().split())
    if w == 0:
        row.append(line)
    else:
        col.append(line)

row.sort()
col.sort()
max_v = 0
for i in range(len(row)-1):
    for j in range(len(col)-1):
        size = (row[i+1] - row[i]) * (col[j+1] - col[j])
        if max_v < size:
            max_v = size

print(max_v)
