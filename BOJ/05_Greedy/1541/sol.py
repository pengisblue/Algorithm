import sys


sys.stdin = open('input.txt')

sentence = input()
transform = list()
number = ''
for word in sentence:
    if word.isdecimal():
        number += word
    else:
        transform.append(int(number))
        transform.append(word)
        number = ''
transform.append(int(number))

index = 1
while len(transform) > 1:
    if transform[index] == '+':
        transform[index - 1: index + 2] = [transform[index - 1] + transform[index + 1]]
    elif transform[index] == '-':
        index += 2

    if index >= len(transform):
        break

index = 1
while len(transform) > 1:
    transform[index - 1: index + 2] = [transform[index - 1] - transform[index + 1]]

print(*transform)
