import re
def solution(dartResult):
    # 점수(0-10), 보너스, 옵션(있을수도 없을 수도)
    # SDT : 해당 점수의 1,2,3제곱
    # * 해당점수와 바로 전 점수를 각각 2배로(곱하기 2), # 해당점수 마이너스 (곱하기 -1)
    answer = []
    score = 0 
    scores = re.findall(r'(\d+|\D)', dartResult) 
    # 2자리 이상 숫자 혹은 숫자 외 나머지인 경우 
    print(scores)
    
    for i in scores:
        if i.isdigit():
            answer.append(int(i))
        elif i == 'S':
            answer[-1] = answer[-1]**1
        elif i == 'D':
            answer[-1] = answer[-1]**2
        elif i == 'T':
            answer[-1] = answer[-1]**3
        elif i == '*':
            # 첫번째에 *가 나왔을 경우 첫번째 점수만 2배 됨
            if len(answer) == 1: 
                answer[-1] = answer[-1]*2
            else: 
                answer[-1] = answer[-1]*2
                answer[-2] = answer[-2]*2
            
        elif i == '#':
            answer[-1] = answer[-1]*(-1)
    
    return sum(answer)