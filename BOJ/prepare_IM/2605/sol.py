import sys
sys.stdin = open('input.txt')

N = int(input())
orders = list(map(int, input().split()))
result = []
# 순서를 담은 리스트를 student를 인덱스로 하여 순회
for student, order in enumerate(orders, 1):
    # 학생번호 - (뽑은순서+1) 을 인덱스로 result에 학생 삽입
    result.insert(student - (order+1), student)
print(*result)
