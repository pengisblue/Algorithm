N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
B = list(map(int, input().split()))
B.sort()
for number in B:
    s_idx = 0
    e_idx = M - 1
    while s_idx >= e_idx:
        m_idx = (s_idx + e_idx)//2
        mid = A[m_idx]
        if mid > number:
            e_idx = m_idx -1
        elif mid < number:
            s_idx = m_idx + 1
        else:
            print(1)
            break
