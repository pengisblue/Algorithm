import sys


sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
numbers = list()
for i in range(N):
    numbers.append(int(input()))

numbers.sort()
for i in range(N):
    print(numbers[i])
