

def solution(elements):
    sum_list = []
    sum_list += elements # sum 1개씩일때 
    a = len(elements)
    for i in range(2, a+1):  # sum 2개씩일때부터 시작
        for j in range(a):
            m = (j+i-1)%a     # 인덱스가 순환되도록 하기
            new = sum_list[(i-2)*a+j] + sum_list[m]
            sum_list.append(new)
    
    return len(list(set(sum_list)))


