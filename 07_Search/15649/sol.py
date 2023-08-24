import sys
sys.stdin = open('input3.txt')
input = sys.stdin.readline


def permu(result):      # result : 순열을 담을 리스트
    if len(result) == M:
        print(*result)
    for i in numbers:
        if i not in result:
            result.append(i)    # i를 추가하고 
            permu(result)       # 재귀를 한 후
            result.pop()        # 원상복귀 -> 다음 for문 돌려야해서


N, M = map(int, input().split())
numbers = list(range(1, N+1))
permu([])
