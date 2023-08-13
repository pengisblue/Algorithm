import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))     # 큐스텍 자료구조 종류
B = list(map(int, input().split()))     # 자료구조 속 원소
M = int(input())
C = list(map(int, input().split()))     # 삽입할 원소
result = []
n = 0
idx = 0
while n < N:
    if A[idx] == 1:     # 스택 자료구조 pop
        A.pop(idx)
        B.pop(idx)
    else:
        idx += 1
    n += 1

for c in C:
    pop_v = c
    for i in range(len(B)):
        pop_v, B[i] = B[i], pop_v   # C의 원소와 입력된 원소를 교체
    result.append(pop_v)

print(*result)
