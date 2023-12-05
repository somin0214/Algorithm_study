# 스트링 인덱스 범위가 넘어갈 때 어떻게 다룰 건지 생각필요
def solution(s, n):
    
    alpa2 = 'abcdefghijklmnopqrstuvwxyz'
    alpa1 = alpa2.upper()
    a = len(alpa1)
    answer = ''
    for i in s:
        if i.islower():
            b = (alpa2.index(i) + n) - a
            answer += alpa2[b]

        elif i.isupper():
            b = (alpa1.index(i) + n) - a
            answer += alpa1[b]

        else:   
            answer += ' '
            
    return answer

print(solution('   ABC DEFGHIGKLM NOPQRSTUVWXYZ   '  ,1))