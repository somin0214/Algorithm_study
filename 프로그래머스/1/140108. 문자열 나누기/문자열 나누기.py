def solution(s):
    answer = []
    # c = 0
    
    while len(s) > 0:
        x = s[0]
        for i in range(1, len(s)):
            new = s[:i+1]
            # x의 개수와 x 개수가 아닌 것들의 개수가 같을 때
            if new.count(x) == len(new) - new.count(x):
                answer.append(new)
                s = s[i+1:]
                # c += 1
                # print(c)
                break
        # 더이상 읽을 글자가 없다면 여태까지만 문자열로 분리하고 종료
        # 포문을 다 돌고 리스트에 더하기!!
        else:
            answer.append(s)
            break

            
    print(answer)
    return len(answer)