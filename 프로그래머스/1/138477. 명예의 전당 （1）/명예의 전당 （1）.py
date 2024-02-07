def solution(k, score):
    answer = [] # 발표 점수 리스트
    score_list =  [] # 명예의 전당 리스트 최대 k길이로 진행
    
    answer.append(score[0])
    score_list.append(score[0])
     
    for i in range(1, len(score)):
        # 명예의 전당일까지 최소값만 넣기 + 명예의 전당 업데이트 
        if i <= k-1:
            answer.append(min(score[:i+1]))
            score_list.append(score[i])
            score_list.sort(reverse=True)
        
        # 명예의 전당 일 이후
        else:
            if score_list[-1] < score[i]:
                score_list.append(score[i])
                score_list.sort(reverse=True)
                score_list = score_list[:-1]
            answer.append(score_list[-1])

        
    return answer 