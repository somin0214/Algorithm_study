def solution(s):
    new = s.split(' ')
    answer_list = []
    a = ''
    for voca in new:
        for i in range(len(voca)):
            if i % 2 == 0:
                a += voca[i].upper()
            else:
                a += voca[i].lower()
        answer_list.append(a)
        a = ''
                
    return ' '.join(answer_list)