import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def seven(idx, sum_h, h_list):
    if sum(bit) == 2 and sum_h == 100:
        combi.append(h_list)
        return
    elif sum(bit) > 2:
        return
    elif idx == 9:
        return
    else:
        bit[idx] = 1
        seven(idx+1, sum_h-heights[idx], h_list+[idx])
        bit[idx] = 0
        seven(idx+1, sum_h, h_list)


heights = [int(input().rstrip()) for _ in range(9)]
heights.sort()
all_sum = sum(heights)
bit = [0] * 9
combi = []
seven(0, all_sum, [])

for i in range(9):
    if i in combi[0]:
        continue
    print(heights[i])
