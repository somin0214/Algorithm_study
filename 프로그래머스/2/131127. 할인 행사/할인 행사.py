def solution(want, number, discount):
    # 회원가입 후 10일간 혜택 제공
    # 리스트 10개씩 순회하면서 회원등록가능 날짜를 구하기
    
    answer = 0
    count = 0
    
    # 원하는 리스트 dic 만들기 
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]
    print(dic)
        
    # 10개씩 순회하면서 원하는 리스트와 같은 지 확인하기 
    for j in range(0, len(discount)-10 + 1):
        
        new = discount[j:j+10]
        
        for a, b in list(dic.items()):
            if a not in new or new.count(a) != b:
                break
            else:
                count += 1
        if count == len(dic):
            answer += 1
        
        # 카운트 초기화
        count = 0
    
    return answer