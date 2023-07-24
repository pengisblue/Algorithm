N, k = map(int, input().split())
students = [[0] * 7, [0] * 7]
room = 0

for i in range(N):
    S, Y = map(int, input().split())
    students[S][Y] += 1

for s in range(2):
    for y in range(1, 7):
        if students[s][y] % k == 0:
            room += students[s][y] // k
        else:
            room += students[s][y] // k + 1

print(room)