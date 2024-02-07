def solution(s):
    # '},{' 기준으로 나누기!
    s = s[2:-2].split('},{')
    s.sort(key = lambda x : len(x)) # str 길이순으로 나열
    
    # 선언
    t = []
    answer = []
    
    for i in s:
        a = [int(num) for num in i.split(',')]
        t.append(a)


    answer.append(t[0][0])
    for i in range(1, len(t)):
        result = list(set(t[i]) - set(t[i-1])) # set에서만 리스트 내용을 뺄 수 있음)
        answer.append(result[0])

    return answer