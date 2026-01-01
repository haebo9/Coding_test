n= int(input())
nums = list(map(int,input().split()))

# print(min(nums),max(nums))

# N <= 1,000,000
# M은 비교 횟수 : 10^7
# 반복문 사용 도전 ; O(N+M) 
min_n = nums[0]
max_n = nums[0]
for i in nums: 
    if i > max_n:
        max_n = i
    elif i < min_n:
        min_n = i

print(min_n, max_n)