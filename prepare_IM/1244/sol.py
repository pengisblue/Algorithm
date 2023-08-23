import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def switch(num):
    if


N = int(input())
status = list(input().split())
M = int(input())
students = [list(map(int, input().split())) for _ in range(M)]
print(students)