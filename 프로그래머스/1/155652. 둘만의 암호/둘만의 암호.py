
from string import ascii_lowercase
 
def solution(s, skip, index):
    
    # skip에 나온 알파벳을 리스트에서 삭제하기
    alpha = list(ascii_lowercase)
    for i in skip:
        idx = alpha.index(i)
        del alpha[idx]

    # 이제 인덱스를 가지고 새로운 암호 만들기 
    answer = ''
    for j in s:
        idx2 = alpha.index(j)
        answer += alpha[(idx2+index)%len(alpha)]
    return answer