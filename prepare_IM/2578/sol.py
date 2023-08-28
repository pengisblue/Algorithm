import sys
sys.stdin = open('input.txt')

board = [list(map(int, input().split())) for _ in range(5)]
order = []
for _ in range(5):
    order.extend(list(map(int, input().split())))

numbers = [0] * 26
for i in range(5):
    for j in range(5):
        # 각 숫자의 좌표값을 숫자를 인덱스로 하는 리스트에 기록한다
        numbers[board[i][j]] = (i, j)

row = [0] * 5
col = [0] * 5
dia = [0] * 2

for idx in range(25):
    # 사회자가 부르는 숫자의 좌표를 가져온다
    i, j = numbers[order[idx]]
    row[i] += 1     # 행
    col[j] += 1     # 열
    if i == j:      # 우하향 대각선
        dia[0] += 1
    if i + j == 4:  # 좌하향 대각선
        dia[1] += 1
    # 한 줄을 다 체크하면 값이 5가 된다
    if row.count(5) + col.count(5) + dia.count(5) >= 3:
        print(idx+1)
        break
