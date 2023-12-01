def solution(d, budget):
    d.sort()
    
    if sum(d) <= budget:
        return len(d)
    
    else:
        for idx, value in enumerate(d):
            budget -= value
            if budget < 0:
                return idx