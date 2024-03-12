import sys
sys.stdin = open('input.txt')

sq1 = list(map(int, input().split()))
sq2 = list(map(int, input().split()))
sq3 = list(map(int, input().split()))
sq4 = list(map(int, input().split()))

square = [(i, j) for i in range(sq1[1], sq1[3]) for j in range(sq1[0], sq1[2])]
square.extend([(i, j) for i in range(sq2[1], sq2[3]) for j in range(sq2[0], sq2[2])])
square.extend([(i, j) for i in range(sq3[1], sq3[3]) for j in range(sq3[0], sq3[2])])
square.extend([(i, j) for i in range(sq4[1], sq4[3]) for j in range(sq4[0], sq4[2])])
print(len(set(square)))
