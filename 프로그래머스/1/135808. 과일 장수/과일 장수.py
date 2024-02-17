def solution(k, m, score):
    answer = 0
    score.sort()
    #print(score)
    #뒤에서부터 m개씩 리스트를 잘라서 

    
    # 시간복잡도가 문제인 듯
    while len(score) >= m:
        answer += min(score[-m:])*m
        del score[-m:]
    return answer