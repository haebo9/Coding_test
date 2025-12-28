def target(nums):
    max_num = 0
    max_cnt = 0
    for i in nums:
        temp_cnt = 0
        for j in nums: 
            if i==j:
                temp_cnt += 1
        if max_cnt < temp_cnt: 
            max_cnt = temp_cnt
            max_num = i
    return max_num, max_cnt

def result(max_num, max_cnt, max_3):
    if max_cnt ==3: 
        return 10000  + max_num*1000
    elif max_cnt ==2: 
        return 1000 + max_num*100
    else: 
        return max_3 * 100

nums = list(map(int, input().split()))
max_num, max_cnt = target(nums) 
max_3 = max(nums)
result = result(max_num, max_cnt, max_3)

print(result)