triangle = list(map(int, input().split()))
triangle.sort()
if triangle[0] + triangle[1] <= triangle[2]:
    triangle[2] = triangle[0] + triangle[1] - 1
print(sum(triangle))
