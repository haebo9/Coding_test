def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    # 시작위치 pos를 기준으로 commands에 따라 요청을 처리한 후 결과를 도출
    # 시작 끝에서 10초씩 앞뒤로 이동인데 이때 10초 이상 남아있는 지 확인하는 게 중요. 
    # 시간 형태가 "시간:분"의 형태라는 것을 명심 ; 60초당 1분 증가
    
    # 시간 추가 함수
    def add_time(time:list, num:int):
        temp_hour = time[0]
        temp_min = time[1]+num
        if temp_min >= 60: 
            temp_hour += 1
            temp_min = temp_min%60
        elif temp_min < 0:
            temp_hour -= 1
            temp_min = 60 + temp_min
        if temp_hour < 0: 
            temp_hour = 0
            temp_min = 0
        return [temp_hour, temp_min]
    
    # 오프닝 시간 범위 확인 함수 
    def check_range(time: list, op_st, op_ed):
        time_in_minutes = time[0] * 60 + time[1]
        op_st_in_minutes = op_st[0] * 60 + op_st[1]
        op_ed_in_minutes = op_ed[0] * 60 + op_ed[1]

        return (op_st_in_minutes <= time_in_minutes < op_ed_in_minutes)
    
    # 초기값 설정 (시작 위치)
    start = list(map(int, pos.split(":")))
    op_st = list(map(int, op_start.split(":")))
    op_ed = list(map(int, op_end.split(":")))
    vidio_en = list(map(int, video_len.split(":")))
    print("현재 시간:", start)
        
    # commands의 요소를 하나씩 읽어옴 
    for c in commands:
        print("명령:", c)
        
        # 현재 시간이 오프닝 구간 이내면 자동으로 오프닝 끝으로 이동
        if check_range(start, op_st, op_ed):
            start = op_ed 
    
    # 요소의 처리 규칙에 맞게 하나씩 처리 
        # next 인 경우 : 뒤로 10초 이동 
        if c == "next": 
            start = add_time(start, 10)
            
            if not check_range(start, [0,0], vidio_en):
                start = vidio_en
                
        # prev 인 경우 : 앞으로 10초 이동 
        elif c == "prev":
            start = add_time(start, -10)
        else: 
            print("wrong input")
            
        print(start)
        
    # 현재 시간이 오프닝 구간 이내면 자동으로 오프닝 끝으로 이동
    if check_range(start, op_st, op_ed):
        start = op_ed 
        
    
    answer = f"{start[0]:02d}:{start[1]:02d}"
    return answer