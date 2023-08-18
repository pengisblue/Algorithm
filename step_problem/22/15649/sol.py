import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline


def combi(idx, n, cnt, m, result):
    if cnt == m:
        all_.append(result)
        return
    elif idx == n:
        return
    else:
        combi(idx+1, n, cnt+1, m, result+[numbers[idx]])
        combi(idx+1, n, cnt, m, result)
        return


def permu(idx, n):


N, M = map(int, input().split())
numbers = list(range(1, N+1))
all_ = []
permutation(0, N, 0, M, [])
print(all_)