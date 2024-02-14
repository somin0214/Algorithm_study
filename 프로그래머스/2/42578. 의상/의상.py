import math
def solution(clothes):
    count = 1

    dic = {}
    # 종류에 따라 한가지만 할 수 있으니
    # 각각 하나씩 착용했을 경우 + 종류별 경우의 수 

    
    # 종류 리스트 만들어서 중복률 계산하기 
    for i in clothes:
        b = i[1]
        if b not in dic.keys():
            dic[b] = 1

        else:
            dic[b] += 1
            
    for v in dic.values():
        count *= v + 1
    return count - 1


# 반례입니다.
# 입력값 〉 [["a", "A"], ["b", "B"], ["c", "C"]]
# 기댓값 〉 7
# a, b, c, abc, ab, ac, bc

# 입력값 〉 [["a", "A"], ["b", "B"], ["b2", "B"],["c", "C"]]
# 기대값 >

