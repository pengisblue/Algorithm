import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def seven(idx, sum_h):
    if sum(bit) == 2 and sum_h == 100:
        for i in range(9):
            if not bit[i]:
                print(heights[i])
        return True
    elif sum(bit) > 2:
        return False
    elif idx == 9:
        return False
    else:
        bit[idx] = 1
        if seven(idx+1, sum_h-heights[idx]):
            return True
        bit[idx] = 0
        return seven(idx+1, sum_h)


heights = [int(input().rstrip()) for _ in range(9)]
heights.sort()
all_sum = sum(heights)
bit = [0] * 9
seven(0, all_sum)
