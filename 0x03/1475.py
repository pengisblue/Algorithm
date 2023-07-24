N = list(map(int,input()))
numbers = [0] * 9
for n in N:
    if n == 9:
        numbers[6] += 1
    else:
        numbers[n] += 1
if numbers[6] % 2 == 0: # round는 5사5입
    numbers[6] = numbers[6] // 2
else: numbers[6] = numbers[6] // 2 + 1
print(max(numbers))