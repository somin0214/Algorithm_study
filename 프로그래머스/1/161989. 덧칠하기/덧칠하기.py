def solution(n, m, section):
    # 칠해야하는 길이 = 첫번째 - 마지막 +1

    answer = 0
    
    while len(section) > 0:
        fill = section[0] + m - 1
        # print('첫번째부터 채우기', fill)

        answer += 1
        # print('더하기')
        for i in range(len(section)):
            if section[0] <= fill:
                # print('삭제', section[0])
                section.pop(0) 
                continue
                
            else: 
                break
        # print('새로운 리스트', section)
    
    
    
    return answer