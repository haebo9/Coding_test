def solution(numbers, hand):
    # 2개의 점이 한칸씩 이동 / 이동 가능범위 제한
    # 가운데 키패드 - 거리 계산 + 왼/오른손 잡이 구분
    
    # for 숫자 배열 앞에서 부터 읽어옴 
        # if 숫자 1,4,7 인경우 L 추가 
        # elif 숫자 3,6,9 인경우 R 추가
        # 그리고 각 손가락 위치 갱신 
        # else 숫자 2,5,8,0 인 경우 두 손가락과의 거리 계산 
            # 가까운 쪽 손가락 추가 
            # 동일하면 왼손잡이/오른손잡이에 해당하는 손가락 추가
    # 완성된 손가락 문자열 리턴
    
    dic = {
        "1":(0,3),"2":(1,3),"3":(2,3),
        "4":(0,2),"5":(1,2),"6":(2,2),
        "7":(0,1),"8":(1,1),"9":(2,1),
        "*":(0,0),"0":(1,0),"#":(2,0),
    }
    
    def distance(n,left,right, hand):
        # 거리 계산 - 가까운 손가락 반환
        n = str(n)
        def cal(a,b):
            a, b = dic[a], dic[b]
            return abs(a[0]-b[0]) + abs(a[1]-b[1])
        
        d_l = cal(n, left)
        d_r = cal(n, right)
        
        if d_l < d_r:
            return "L"
        elif d_l > d_r:
            return "R"
        else: 
            return ("L" if hand == "left" else "R")
    
    answer = ''
    left = "*"
    right = "#"
    for n in numbers: 
        if n in [1,4,7]:
            answer += "L"
            left = str(n)
        elif n in [3,6,9]:
            answer += "R"
            right = str(n)
        elif n in [2,5,8,0]:
            dist = distance(n, left, right, hand)
            answer += dist
            if dist == "L":
                left = str(n)
            else: 
                right = str(n)
    return answer