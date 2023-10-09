from collections import deque
import sys
sys.stdin = open('input1.txt')
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))     # 큐스텍 자료구조 종류
B = list(map(int, input().split()))     # 자료구조 속 원소
M = int(input())
C = deque(list(map(int, input().split())))     # 삽입할 원소

for i in range(N):
    if A[i] == 0:
        C.appendleft(B[i])

for i in range(M):
    print(C.popleft(), end=' ')
