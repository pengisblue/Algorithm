N = int(input())
A = list(map(int, input().split()))     # 큐스텍 자료구조 종류
B = list(map(int, input().split()))     # 자료구조 속 원소
M = int(input())
C = list(map(int, input().split()))     # 삽입할 원소
result = []
for c in C:
    pop_v = c
    for i in range(N):
        if A[i] == 0:
            c, B[i] = B[i], c