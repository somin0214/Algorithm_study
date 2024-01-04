def solution(n):
    answer = n
    a = bin(n)[2:]
    b = a.count('1')
    while answer >= n:
        answer += 1 
        c = bin(answer)[2:].count('1')
        if b == c:
            break
    
    return answer