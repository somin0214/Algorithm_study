def solution(n, m):
    a, b = sorted([n, m])
    x, y = 0, 0
    
    # 최대 공약수 구하기 
    for i in range(1, b+1):
        if a % i == 0 and b % i == 0:
            x = i
    
    # 최소 공배수 구하기 
    for j in range(a, a*b + 1):
        if j % a == 0 and j % b == 0:
            y = j
            break

    return [x, y]