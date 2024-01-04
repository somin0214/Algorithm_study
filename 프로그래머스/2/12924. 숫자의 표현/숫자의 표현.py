def solution(n):
    answer = 1 # 자기 자신 스스로도 표현할 수 있기 때문
    
    for i in range(1, n//2 + 1): # 절반이상까지는 더할 필요 없음
        sum = 0
        
        while sum < n :
            sum += i
            
            if sum == n :
                answer += 1
                break
                
            i += 1
    
    return answer