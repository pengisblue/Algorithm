import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    square1 = [set(range(x1, p1+1)), set(range(y1, q1+1))]
    square2 = [set(range(x2, p2+1)), set(range(y2, q2+1))]
    and_row = square1[0] & square2[0]
    and_col = square1[1] & square2[1]
    if len(and_row) > 1 and len(and_col) > 1:   # 직사각형
        print('a')
    elif len(and_row) == 1 and len(and_col) == 1:     # 한 점만 만날 때
        print('c')
    elif len(and_row) == 0 or len(and_col) == 0:    # 공통부분이 없음
        print('d')
    else:    # 선분으로 겹칠 때
        print('b')
