total = int(input())
n = int(input())

def cal_total(n):
    result = 0
    for _ in range(n):
        price, cnt = map(int, input().split())
        result += price*cnt
    return result

print('Yes' if cal_total(n)==total else 'No')