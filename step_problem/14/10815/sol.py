import sys
sys.stdin = open('input.txt')

N = int(input())
numbers = list(map(int, input().split()))
dic_nums = {num: 1 for num in numbers}
M = int(input())
find = list(map(int, input().split()))
for i in find:
    print(dic_nums.get(i, 0), end=' ')
