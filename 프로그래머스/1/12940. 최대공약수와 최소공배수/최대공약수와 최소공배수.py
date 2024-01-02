# def solution(n, m):
#     a, b = sorted([n, m])
#     x, y = 0, 0
    
#     # 최대 공약수 구하기 
#     for i in range(1, b+1):
#         if a % i == 0 and b % i == 0:
#             x = i
    
#     # 최소 공배수 구하기 
#     for j in range(a, a*b + 1):
#         if j % a == 0 and j % b == 0:
#             y = j
#             break

#     return [x, y]

def solution(n, m):
    answer = []
    for i in range(max(m,n),m*n+1):
        if i%m==0 and i%n==0:
            answer.append(i)
            break

    if n>m:
        while n%m!=0:
                c=n%m
                n,m=m,c
        answer.append(m)
    else:
        while m%n!=0:
            c=m%n
            m,n=n,c
        answer.append(n)

    answer.sort()
    return answer