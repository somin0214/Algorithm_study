def solution(dots):
    ## 어떻게 평행인지 판단 : 기울기가 같다면 평행인걸 알 수 있다. 
    # 2개씩 비교했을 때 경우의 수는 3개 
    # 기울기 = y값 증가량 / x값 증가량 
    answer = 0
    # 01 VS 23
    if (dots[0][1]-dots[1][1]) / (dots[0][0]-dots[1][0]) == (dots[2][1]-dots[3][1]) / (dots[2][0]-dots[3][0]):
        answer += 1
    #02 VS 13
    elif (dots[0][1]-dots[2][1]) / (dots[0][0]-dots[2][0]) == (dots[1][1]-dots[3][1]) / (dots[1][0]-dots[3][0]):
        answer += 1
    
    #03 VS 12
    elif (dots[0][1]-dots[3][1]) / (dots[0][0]-dots[3][0]) == (dots[1][1]-dots[2][1]) / (dots[1][0]-dots[2][0]):
        answer += 1
    return answer