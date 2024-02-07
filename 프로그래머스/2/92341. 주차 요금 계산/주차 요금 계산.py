import math
# 입차,출차 기준 누적시간 
def total_minutes(start_time, end_time):
    start_hour, start_minute = list(map(int, start_time.split(':')))
    end_hour, end_minute = list(map(int, end_time.split(':')))

    total_minutes_start = start_hour * 60 + start_minute
    total_minutes_end = end_hour * 60 + end_minute

    return total_minutes_end - total_minutes_start

def solution(fees, records):

    answer = []
    dic = {}
    
    for r in records:
        l = r.split() # 입출차기록 (시:분, 차량번호, 입차 혹은 출차)
        if l[1] not in dic:
            dic[l[1]] = []
            
        # 차별로 출차 기록 만들 딕셔너리 차번호: [입출차시간...]
        dic[l[1]].append(l[0]) 

    #### 주의 : 출차가 없으면 23:59에 출차한 것으로 정하기
    # 출차 기록없으면 기록 추가 
    for k, v in dic.items():
        if len(v) % 2 != 0:
            dic[k].append('23:59')

    # 차량번호가 적은것 부터 나열
    dic = {int(k): dic[k] for k in sorted(dic, key=int)}

    # 1. 차별로 누적주차 시간 구하기
    # 2. 기본 요금 + 올림(누적시간 - 기본시간 / 단위 시간) * 단위요금
    # 요금 (기본시간, 기본요금, 단위 시간, 단위 요금)
    a, b, c, d = fees
    total = 0
    pay = 0
    
    for i in dic.keys():
        print('딕셔너리 키값과 밸류 길이: ', i, len(dic[i]))
        new = dic[i]
        for j in range(0, len(dic[i]), 2):
            total += total_minutes(new[j], new[j+1])
        
        print('주차 시간 :', total)
        if total <= a:
            pay += b
        else: 
            pay = b + math.ceil((total-a)/c)*d # 올림하는 함수 적용
            print('주차비 :', pay)
        
        answer.append(pay)
    
        
        # 초기화
        total, pay = 0, 0

    return answer