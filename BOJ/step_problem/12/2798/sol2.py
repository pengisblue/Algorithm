import sys
sys.stdin = open('input2.txt')


def combi(idx, cnt, result):
    global blackjack
    if result > M:
        return
    elif cnt == 3:
        # result가 M보다 작으면서 blackjack보다 클 때 == blackjack보다 M에 가까울 때
        if result > blackjack:
            blackjack = result  # blackjack의 값 재할당
        return
    elif idx == N:
        return
    else:
        bit[idx] = 1
        combi(idx+1, cnt+1, result+numbers[idx])
        bit[idx] = 0
        combi(idx+1, cnt, result)


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
bit = [0] * N
blackjack = 0
combi(0, 0, 0)
print(blackjack)
