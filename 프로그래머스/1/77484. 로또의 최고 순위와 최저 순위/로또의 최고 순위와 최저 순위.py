def solution(lottos, win_nums):
    # 숫자 범위 1-46
    # 지워진게 0으로 표시
    # 최고순위 : 최대한 다 당첨번호로 바꾸기
    # 최저순위 : 최대한 다 미 당첨번호로 바꾸기 
    answer = []
    count = 0
    dic = {}
    
    # 당첨내용에 따른 로또 순위 딕셔너리
    rank = 0
    for i in range(6, 0, -1):
        rank += 1
        dic[i] = rank
        
    # 0인 경우도 추가
    dic[0] = 6
    print(dic)
    
    # 지워진거 채우기 전 일치하는 숫자 개수 
    for n in win_nums:
        count += lottos.count(n)
    print(count)
        
    #지워진 숫자의 개수
    zero_count = lottos.count(0)
    print(zero_count)
    
    # 만약 지워지기 진 것이 없을 경우
    if zero_count == 0:
        answer += [dic[count]]*2
    
    else:
    # 최대 맞출 수 있는 개수 = 지워진 숫자를 다 맞췄을 경우 
        total_count = count + zero_count
        answer.append(dic[total_count])
    
    # 최소 맞출 수 있는 개수 = 지워진 숫자를 다 틀렸을 경우
        answer.append(dic[count])
        
    return answer 