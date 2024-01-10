def solution(n, left, right):
    # left, right는 인덱스 
    answer = []
    
    for i in range(left, right+1):
        #(a,b)가 행렬의 인덱스 각각 n의 몫과 나머지
        a = i // n
        b = i % n
        new = max(a, b)
        answer.append(new+1)
            
    return answer