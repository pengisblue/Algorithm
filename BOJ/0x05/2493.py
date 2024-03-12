import sys
input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))
results = [0]
received = 0
top = heights[-1]






# for i in range(N - 1):
#     top = heights[-1]  # 확인할 탑
#     copyed = heights.copy()  # 탑 리스트를 복사해서
#     receive = False  # 수신 안됨
#     for i in range(len(heights)-1):
#         copyed.pop()         # 복사한 탑을 pop하며 top과 비교
#         if top < copyed[-1]:  # 레이저가 수신되면
#             tower = heights.index(copyed[-1]) + 1  # 몇 번째 탑인지 확인
#             receive = True  # 수신 됨
#             break
#     heights.pop()  # 다음 차례
        
#     if receive:
#         results.append(tower)
#     else:
#         results.append(0)

# results.append(0)  # 1번째 탑
# results.reverse()
# print(*results)