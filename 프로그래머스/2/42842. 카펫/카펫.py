def solution(brown, yellow):
    total = brown + yellow
    # 일단 방정식으로 쉽게 계산해보자!
    # a >= b
    # yellow = (a-2)*(b-2)
    # brown = a*b- yellow = a*b - (ab-2a -2b +4) = 2a+2b -4
    # a*b = total 
    for b in range(3, total+1):
        
        if total % b == 0 :
            a = total / b 
            if a >= b and 2*a+2*b == brown + 4:
                break
            
    return [a, b]