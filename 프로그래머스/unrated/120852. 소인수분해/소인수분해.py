def solution(n):
    answer = []
    
    prime = 2
    while prime <= n:
        if n % prime == 0:
            if prime not in answer:
                answer.append(prime)
            
            n //= prime
        
        else:
            prime += 1

    print(answer)
    return answer