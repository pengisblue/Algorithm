arr = input().split('-')

sums = []
for i in arr:
    sums.append(sum(list(map(int,i.split('+')))))

ans = sums[0]
for i in sums[1:]:
    ans -= i

print(ans)
