n, x = map(int, input().split())
nums = list(map(int, input().split()))

target = ' '.join([str(i) for i in nums if i < x])
print(target)