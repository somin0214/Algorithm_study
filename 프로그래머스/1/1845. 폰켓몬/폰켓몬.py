def solution(nums):
    answer = 0
    select_num = len(nums)/2
    poky_num = len(set(nums))
    if poky_num <= select_num:
        answer += poky_num
    else:
        answer += select_num
    return answer