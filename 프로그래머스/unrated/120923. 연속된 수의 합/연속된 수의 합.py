def solution(num, total):
    answer = []
    middle_num = total // num 
    answer +=  [i for i in range(middle_num - (num-1)//2, middle_num + (num+2)//2, 1)]
    return answer