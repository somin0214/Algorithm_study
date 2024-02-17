def solution(participant, completion):

    # 최대한 빠른 시간에 찾는게 관건 (시간복잡도)
    # 이름 순으로 정렬하자!
    participant.sort()
    completion.sort()
    
    for a, b in zip(participant, completion):
        if a!= b:
            print(a)
            return a
        
    # 포문을 다 돌고도 다 같았다면 참가자 마지막사람이 완주를 못한 것 
    return participant[-1]
    
        
            
    
    
    ## 효율성 문제에서 걸리는 식
    # for name in participant:
    #     if name not in completion:
    #         answer += name
    #         break
    #     if name in completion:
    #         idx = completion.index(name)
    #         completion.pop(idx)
