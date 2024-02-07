def solution(a, b):
    # 윤년이면 366일(2월 29일 포함)

    cal_list = []
    cal = ['FRI', 'SAT', 'SUN','MON', 'TUE', 'WED', 'THU'] 
    cal_list = cal*(366//7) + cal[:(366%7)]
    
    n = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    print(sum(n), len(cal_list))
    idx = sum(n[:a-1]) + b
    
    return cal_list[idx-1]