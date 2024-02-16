def solution(msg):
    answer = []
    
    # 압축 알고리즘 딕셔너리 생성
    dic = {}
    alpa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i, v in enumerate(alpa):
        dic[v] = i+1
        
 
    while True:
        # 인덱스가 넘기지 않도록 해당 글자가 사전에 있다면(보통 마지막)
        if msg in dic:
            answer.append(dic[msg])
            break
        
        for i in range(1, len(msg)):
        
            if msg[:i+1] not in dic:
                # 일단은 해당 글자 번호 출력
                answer.append(dic[msg[:i]])
                
                # 사전에 추가 
                dic[msg[:i+1]] = len(dic) + 1
                
                # 새롭게 할 때 글자부터 확인하기 
                msg = msg[i:]
                break
    return answer