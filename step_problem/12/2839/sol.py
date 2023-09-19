import sys
sys.stdin = open('input5.txt')

N = int(input())
result = -1
five_cnt = N // 5
while five_cnt >= 0:
    if (N - (five_cnt * 5)) % 3 == 0:
        three_cnt = (N - (five_cnt * 5)) // 3
        result = five_cnt + three_cnt
        break
    five_cnt -= 1

print(result)
