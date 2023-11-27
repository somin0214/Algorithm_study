def solution(n):
    
    # 3진법으로 바꾸기 
    answer = ''
    while n > 0:
        n, remainder = divmod(n, 3) # 몫과 나머지 튜플 형태로 나옴
        answer += str(remainder)

    # 이미 뒤집힌 상태임으로 바로 10진법으로 표현
    return int(answer, 3)