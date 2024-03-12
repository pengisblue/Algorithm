A = int(input())
B = int(input())
C = int(input())
number = A * B * C
number = str(number)
for i in range(10):
    print(number.count(f'{i}'))