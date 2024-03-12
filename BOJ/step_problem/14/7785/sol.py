import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
record = {}
for _ in range(n):
    person, status = input().split()
    record[person] = status

record = dict(sorted(record.items(), reverse=True))
for person, status in record.items():
    if status == 'enter':
        print(person)
