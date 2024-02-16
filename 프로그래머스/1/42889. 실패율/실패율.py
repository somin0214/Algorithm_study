def solution(N, stages):
    # 전체 스테이지 수 
    # 사용자가 현재 멈춰있는 스테이지 번호 
    # 단, N+1 이미 다 클리어한 사람
    # 스테이지에 도달한 유저가 없으면 실패율 0

    
    # 모든 레벨의 실패율을 0값으로 지정
    dic = {}
    for l in range(1, N+1):
        dic[l] = 0
    
    print(dic)
    
    # 각 레벨 별 실패율 계산하여 딕셔너리에 저장
    for i in range(1, N+1):
        a, b = 0, 0 # 값 초기화
        for j in stages:
            if j > i :
                b += 1
            elif j == i:
                a += 1 # 리스트에 해당 레벨이 있는지 카운트 
                b += 1 # 그 숫자이상의 숫자 카운트
        
        if a !=0 and b !=0:
            dic[i] = a / b
    
    print(dic)
    
    # 딕셔너리 밸류로 내림차순
    answer = sorted(dic.items(), key = lambda x : x[1], reverse = True)
    print(answer)

        
    
    
    
    return [k for k, v in answer]