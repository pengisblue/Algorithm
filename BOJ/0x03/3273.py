n = int(input())
numbers = list(map(int, input().split()))
x = int(input())
lst = [0] * x
cnt = 0

for number in numbers:
    if number > x:  # number가 x보다 크면 성립x
        continue
    pair = x - number
    if lst[pair - 1] == 1:
        cnt += 1
    lst[number-1] = 1

print(cnt)