# def solution(s):
#     new = s.split(' ')
#     answer_list = []
#     a = ''
#     for voca in new:
#         for i in range(len(voca)):
#             if i % 2 == 0:
#                 a += voca[i].upper()
#             else:
#                 a += voca[i].lower()
#         answer_list.append(a)
#         a = ''
                
#     return ' '.join(answer_list)
def solution(s):
    answer = []
    for i in s.split(' '):
        i=list(i)
        for k in range(len(i)):
            if k%2==0 or k==0:
                i[k]=i[k].upper()
            else:
                i[k]=i[k].lower()
        answer.append(''.join(i))
    return ' '.join(answer)