N = int(input())
location = [list(map(int, input().split())) for i in range(N)]
location = list(map(list, zip(*location)))
result = (max(location[0]) - min(location[0])) * (max(location[1]) - min(location[1]))
print(result)

# X = []
# Y = []
# for _ in range(N):
#     x, y = map(int, input().split())
#     X.append(x)
#     Y.append(y)
#
# result = (max(X)-min(X)) * (max(Y)-min(Y))
# print(result)

# location = [list(map(int, input().split())) for i in range(N)]
# min_x, min_y, max_x, max_y = location[0][0], location[0][1], location[0][0], location[0][1]
# for i in range(N):
#     if min_x > location[i][0]:
#         min_x = location[i][0]
#     if min_y > location[i][1]:
#         min_y = location[i][1]
#     if max_x < location[i][0]:
#         max_x = location[i][0]
#     if max_y < location[i][1]:
#         max_y = location[i][1]
#
# result = (max_x-min_x) * (max_y-min_y)
# print(result)
