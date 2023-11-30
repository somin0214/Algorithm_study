def solution(name, yearning, photo):
    answer = []
    score = 0
    for n in photo:
        for a in n:
            if a in name:
                idx = name.index(a)
                score += yearning[idx]
        answer.append(score)
        score = 0
    
    return answer