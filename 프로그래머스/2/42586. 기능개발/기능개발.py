def solution(progresses, speeds):
    
    answer = []
    days = []
    

    # 배포 날짜 구하기
    for idx, p in enumerate(progresses):
        remain = int(100 - p)
        if remain % speeds[idx] == 0:
            day = int(remain//speeds[idx])
        else:
            day = int(remain//speeds[idx]) + 1
            
        days.append(day)

    count = 1
    front_day = days[0]
    for day in days[1:]:
        if front_day >= day:  # 이전 기능이 현재 기능보다 더 오래 걸리면 함께 배포됨
            count += 1
        else:  # 이전 기능이 현재 기능보다 짧게 걸리면 기능을 배포하고 초기화
            answer.append(count)
            count = 1
            front_day = day
    answer.append(count)  # 마지막으로 남은 기능 배포
    
    return answer
