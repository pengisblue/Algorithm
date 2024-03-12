A, B, V = map(int, input().split())
day = 1
up = (V-A) // (A-B)
if (V-A) % (A-B):
    day += 1
day += up

print(day)
