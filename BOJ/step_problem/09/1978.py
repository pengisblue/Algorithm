N = int(input())
numbers = list(map(int, input().split()))
cnt_prime = 0
for number in numbers:
    if number == 2:
        cnt_prime += 1
    elif number != 1:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            cnt_prime += 1

print(cnt_prime)
