import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def switch(num):
    # 꺼져있으면 켜기
    if status[num] == '0':
        status[num] = '1'
    # 켜져있으면 끄기
    else:
        status[num] = '0'


N = int(input())    # 스위치 개수
status = list(input().split())  # 스위치 상태
M = int(input())    # 학생 수
students = [list(map(int, input().split())) for _ in range(M)]
for student, number in students:
    button = number - 1
    if student == 1:    # 남학생
        # number 의 배수가 되는 스위치 상태 변경
        while button < N:
            switch(button)
            button += number
    else:   # 여학생
        switch(button)      # number 스위치 상태 변경
        left, right = button-1, button+1
        # 대칭이 되는 좌, 우 스위치의 상태가 같은 연속적인 스위치 상태 변경
        while 0 <= left and right < N and status[left] == status[right]:
            switch(left)
            switch(right)
            left -= 1
            right += 1

for i in range(N):
    if (i+1) % 20 == 0:
        print(status[i])
    else:
        print(status[i], end=' ')
