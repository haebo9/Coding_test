hh, mm = map(int, input().split())

def to_min(hh, mm):
    '''
    현재 시간을 입력 받은 뒤 45분 전의 시간을 반환
    '''
    total_min = hh*60 + mm
    add_45 = total_min - 45
    h, m = add_45//60, add_45%60
    if h <0 : h=23
    
    return h, m



h, m = to_min(hh, mm)
print(h, m)