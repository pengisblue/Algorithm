location = []
for i in range(3):
    location.append(list(map(int, input().split())))

location = list(map(list, zip(*location)))
for x in set(location[0]):
    if location[0].count(x) == 1:
        X = x

for y in set(location[1]):
    if location[1].count(y) == 1:
        Y = y

print(X, Y)
