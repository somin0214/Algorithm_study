def solution(s):
    answer = [-1]
    for i in range(1, len(s)):
        if s[i] not in s[:i]:
            answer.append(-1)
        else:
            a =  i - s[:i].rfind(s[i]) # 오른쪽부터 동일한 것을 찾아 인덱스 리턴 
            answer.append(a)
    return answer
