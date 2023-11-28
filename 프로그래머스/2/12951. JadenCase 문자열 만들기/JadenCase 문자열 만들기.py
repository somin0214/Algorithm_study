def solution(s):
    answer = ''
    t = False
    for i in s:
        if i == ' ':
            answer += i
            t = False
        elif i.isdigit():
            answer += i
            t = True 
        elif t:
            answer += i.lower()
        else:
            answer += i.upper()
            t = True
            
    return answer
            
            


#입력값 〉   "  for the what 1what  "
#기댓값 〉   "  For The What 1what  "