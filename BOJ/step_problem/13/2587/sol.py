import sys
sys.stdin = open('input.txt')

nums = []
for _ in range(5):
    nums.append(int(input()))

nums.sort()
print(sum(nums)//5)
print(nums[2])