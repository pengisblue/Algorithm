import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline


def winner(a, b):
    if a.count('4') != b.count('4'):
        if a.count('4') > b.count('4'):
            return 'A'
        else:
            return 'B'
    elif a.count('3') != b.count('3'):
        if a.count('3') > b.count('3'):
            return 'A'
        else:
            return 'B'
    elif a.count('2') != b.count('2'):
        if a.count('2') > b.count('2'):
            return 'A'
        else:
            return 'B'
    elif a.count('1') != b.count('1'):
        if a.count('1') > b.count('1'):
            return 'A'
        else:
            return 'B'
    else:
        return 'D'


N = int(input())    # 라운드 수
for i in range(N):
    result_A = input().split()[1:]
    result_B = input().split()[1:]
    print(winner(result_A, result_B))
