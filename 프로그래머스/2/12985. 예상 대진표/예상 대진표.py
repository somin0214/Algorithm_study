import math

def solution(n,a,b):
    count = 1
    a, b = min(a, b), max(a, b)

    #총 토너먼트 수만큼 반복
    while count <= n**1/2:
        
        if b % 2 == 0 and a % 2 == 1 and  b-a == 1:
            break
            
        count += 1
        a = math.ceil(a**1/2) # 제곱근을 하고 반올림해주기
        b = math.ceil(b**1/2)
        print(a, b)
    
        
    
    return count 