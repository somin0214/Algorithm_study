def solution(keymap, targets):
    # 만약에 키맵에 없다면 -1 리턴
    # 딕셔너리에서 없는 것만 인덱스를 저장하지!
    

    dic = {}
    # 키 딕셔너리 만들기 
    for key in keymap:
        for i, v in enumerate(key):
            if v not in dic.keys():
                dic[v] = i + 1
  
            else:
                if i + 1 < dic[v]:
                    dic[v] = i + 1

    answer = []
    # 타겟을 돌면서 누르는 횟수 더하기 
    for target in targets:
        a = 0
        for index, value in enumerate(target):
            if value in dic:
                a += dic[value]
            elif value not in dic:
                a = -1
                break
        answer.append(a)

        
    return answer