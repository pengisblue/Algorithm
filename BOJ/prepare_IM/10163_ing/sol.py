import sys
sys.stdin = open('input3.txt')
input = sys.stdin.readline

N = int(input())
# 각각의 사각형의 크기를 받는 리스트
sizes = [list(map(int, input().split())) for _ in range(N)]
squares = []    # 사각형들의 좌표값을 담을 리스트
for j, i, col, row in sizes:
    # 각 사각형들의 좌표를 set으로 받아서 square에 추가
    squares.append(set((x, y) for x in range(j, j+col) for y in range(i, i+row)))
for i in range(N-1):
    for j in range(i+1, N):
        # 사각형의 차집합을 구해서 보이는 면적 구하기
        squares[i] = squares[i] - squares[j]
for i in range(N):
    print(len(squares[i]))
