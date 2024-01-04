# 스택을 사용한 
def solution(s):
    answer = 0 
    new = []
    
    for i in s:
        if new and new[-1] == i:
            new.pop() 
        else:
            new.append(i)
    
    if len(new) == 0. :
        answer += 1
    return answer